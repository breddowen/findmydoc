#!/usr/bin/env python3

from __future__ import annotations

import argparse
import ast
import io
import sys
import tokenize
from pathlib import Path
from typing import Iterable


DEFAULT_OUTPUT = "context_export.txt"

EXCLUDED_DIRECTORY_NAMES = {
    ".git",
    ".idea",
    ".vscode",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "node_modules",
    "venv",
    ".venv",
    "env",
    ".env",
}


def read_python_file(path: Path) -> str:
    """
    Читает Python-файл с учетом coding cookie.
    """
    with tokenize.open(path) as file:
        return file.read()


def normalize_newlines(text: str) -> str:
    """
    Приводит переводы строк к Unix-формату.
    """
    return text.replace("\r\n", "\n").replace("\r", "\n")


def get_relative_display_path(path: Path, project_root: Path) -> str:
    """
    Формирует путь в формате:

    # ./backend/app/example.py
    """
    relative_path = path.resolve().relative_to(project_root.resolve())
    return "./" + relative_path.as_posix()


def has_path_header(first_line: str) -> bool:
    """
    Проверяет, является ли первая строка уже заголовком с путем к файлу.
    """
    stripped = first_line.strip()

    if not stripped.startswith("#"):
        return False

    value = stripped[1:].strip()

    return (
        value.startswith("./")
        or value.startswith("../")
        or value.startswith("/")
        or value.endswith(".py")
        or ".py " in value
    )


def remove_existing_path_header(source: str) -> str:
    """
    Удаляет первую строку, если это уже комментарий с путем к файлу.
    """
    lines = source.splitlines()

    if not lines:
        return source

    if has_path_header(lines[0]):
        return "\n".join(lines[1:])

    return source


def source_lines(source: str) -> list[str]:
    return source.splitlines()


def get_node_source(
    node: ast.AST,
    lines: list[str],
) -> str:
    """
    Возвращает исходный текст AST-ноды.
    """
    lineno = getattr(node, "lineno", None)
    end_lineno = getattr(node, "end_lineno", None)

    if lineno is None or end_lineno is None:
        return ""

    return "\n".join(lines[lineno - 1:end_lineno])


def get_indent(line: str) -> str:
    return line[: len(line) - len(line.lstrip())]


def find_function_colon(
    source: str,
    node: ast.FunctionDef | ast.AsyncFunctionDef,
) -> tuple[int, int] | None:
    """
    Находит двоеточие, заканчивающее сигнатуру функции.

    Возвращает позицию строки и символа.
    """
    lines = source.splitlines(keepends=True)

    start_line_index = node.lineno - 1

    if start_line_index >= len(lines):
        return None

    text_from_function = "".join(lines[start_line_index:])

    try:
        tokens = tokenize.generate_tokens(io.StringIO(text_from_function).readline)
    except (IndentationError, tokenize.TokenError):
        return None

    bracket_depth = 0
    found_function_keyword = False

    for token in tokens:
        token_type, token_string, start, _, _ = token

        if token_type == tokenize.NAME and token_string in {"def", "async"}:
            if token_string == "def":
                found_function_keyword = True
            continue

        if not found_function_keyword:
            continue

        if token_string in {"(", "[", "{"}:
            bracket_depth += 1
            continue

        if token_string in {")", "]", "}"}:
            bracket_depth -= 1
            continue

        if token_string == ":" and bracket_depth == 0:
            relative_line = start[0] - 1
            relative_column = start[1]

            absolute_line = start_line_index + relative_line

            return absolute_line, relative_column

    return None


def get_function_signature(
    source: str,
    node: ast.FunctionDef | ast.AsyncFunctionDef,
) -> str:
    """
    Извлекает функцию от начала def до двоеточия включительно.
    """
    lines = source.splitlines()

    colon_position = find_function_colon(source, node)

    if colon_position is None:
        return get_node_source(node, lines)

    colon_line, colon_column = colon_position

    result_lines = lines[node.lineno - 1: colon_line + 1]

    if result_lines:
        result_lines[-1] = result_lines[-1][: colon_column + 1]

    return "\n".join(result_lines)


def is_docstring_node(node: ast.AST) -> bool:
    """
    Проверяет, является ли нода docstring.
    """
    return (
        isinstance(node, ast.Expr)
        and isinstance(getattr(node, "value", None), ast.Constant)
        and isinstance(node.value.value, str)
    )


def get_function_docstring(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
    lines: list[str],
) -> str:
    """
    Возвращает исходный docstring функции.
    """
    if not node.body:
        return ""

    first_node = node.body[0]

    if not is_docstring_node(first_node):
        return ""

    return get_node_source(first_node, lines)


def iter_nested_return_like_nodes(
    function_node: ast.FunctionDef | ast.AsyncFunctionDef,
) -> Iterable[ast.AST]:
    """
    Ищет return, raise и yield внутри функции.

    Вложенные функции и классы пропускаются, чтобы return из них
    не считался return исходной функции.
    """
    result: list[ast.AST] = []

    def visit(node: ast.AST) -> None:
        if node is not function_node and isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
                ast.ClassDef,
            ),
        ):
            return

        if isinstance(node, (ast.Return, ast.Raise)):
            result.append(node)

        elif isinstance(node, ast.Yield):
            result.append(node)

        elif isinstance(node, ast.YieldFrom):
            result.append(node)

        for child in ast.iter_child_nodes(node):
            visit(child)

    for child in function_node.body:
        visit(child)

    return result


def get_last_return_like_node(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
    lines: list[str],
) -> str:
    """
    Возвращает последний по расположению return, raise или yield.
    """
    candidates = list(iter_nested_return_like_nodes(node))

    if not candidates:
        return ""

    candidates.sort(
        key=lambda item: (
            getattr(item, "end_lineno", 0),
            getattr(item, "end_col_offset", 0),
        )
    )

    return get_node_source(candidates[-1], lines)


def get_decorators(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
    lines: list[str],
) -> list[str]:
    """
    Возвращает декораторы функции.
    """
    result = []

    for decorator in node.decorator_list:
        decorator_source = get_node_source(decorator, lines)

        if decorator_source:
            result.append("@" + decorator_source)

    return result


def make_function_stub(
    source: str,
    node: ast.FunctionDef | ast.AsyncFunctionDef,
) -> str:
    """
    Формирует сокращенное представление функции.
    """
    lines = source.splitlines()

    parts: list[str] = []

    parts.extend(get_decorators(node, lines))

    signature = get_function_signature(source, node)

    if signature:
        parts.append(signature)

    docstring = get_function_docstring(node, lines)

    if docstring:
        parts.append(docstring)

    function_line = lines[node.lineno - 1]
    function_indent = get_indent(function_line)
    body_indent = function_indent + "    "

    parts.append(f"{body_indent}FUNCTION BODY")

    last_return = get_last_return_like_node(node, lines)

    if last_return:
        parts.append(last_return)

    return "\n".join(parts)


def get_top_level_imports(
    tree: ast.Module,
    source: str,
) -> list[str]:
    """
    Возвращает все верхнеуровневые импорты в исходном порядке.
    """
    lines = source.splitlines()
    imports = []

    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            value = get_node_source(node, lines)

            if value:
                imports.append(value)

    return imports


def get_top_level_classes(
    tree: ast.Module,
    source: str,
) -> list[str]:
    """
    Возвращает все верхнеуровневые классы полностью.
    """
    lines = source.splitlines()
    classes = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            value = get_node_source(node, lines)

            if value:
                classes.append(value)

    return classes


def get_top_level_functions(
    tree: ast.Module,
    source: str,
) -> list[str]:
    """
    Возвращает сокращенные верхнеуровневые функции.
    """
    functions = []

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.append(make_function_stub(source, node))

    return functions


def is_full_file_by_name(path: Path) -> bool:
    """
    Файлы models.py и schemas.py всегда выгружаются полностью.
    """
    return path.name.lower() in {
        "models.py",
        "schemas.py",
    }


def build_reduced_file(
    path: Path,
    source: str,
    display_path: str,
) -> str:
    """
    Формирует сокращенное представление одного файла.
    """
    source = normalize_newlines(source)

    try:
        tree = ast.parse(source, filename=str(path))
    except SyntaxError as error:
        return "\n".join(
            [
                f"# {display_path}",
                "",
                f"# SYNTAX ERROR: {error}",
                "",
                source.rstrip(),
            ]
        )

    parts: list[str] = [
        f"# {display_path}",
    ]

    imports = get_top_level_imports(tree, source)

    if imports:
        parts.append("")
        parts.extend(imports)

    classes = get_top_level_classes(tree, source)

    if classes:
        parts.append("")
        parts.extend(classes)

    functions = get_top_level_functions(tree, source)

    if functions:
        parts.append("")
        parts.extend(functions)

    return "\n".join(parts).rstrip()


def build_full_file(
    source: str,
    display_path: str,
) -> str:
    """
    Формирует полное представление файла.

    Если в исходном файле уже есть первая строка с путем,
    она заменяется на нормализованный путь.
    """
    source = normalize_newlines(source)
    source_without_header = remove_existing_path_header(source)

    result = f"# {display_path}\n"

    if source_without_header.strip():
        result += "\n" + source_without_header.rstrip()

    return result.rstrip()


def should_skip_path(path: Path) -> bool:
    """
    Проверяет, нужно ли пропустить путь.
    """
    return any(
        part in EXCLUDED_DIRECTORY_NAMES
        for part in path.parts
    )


def collect_python_files(input_path: Path) -> list[Path]:
    """
    Собирает Python-файлы из файла или директории.
    """
    if input_path.is_file():
        if input_path.suffix.lower() != ".py":
            return []

        return [input_path]

    if not input_path.is_dir():
        return []

    result = []

    for path in input_path.rglob("*.py"):
        if path.is_file() and not should_skip_path(path):
            result.append(path)

    return sorted(
        result,
        key=lambda item: item.as_posix().lower(),
    )


def count_file_lines(source: str) -> int:
    """
    Возвращает количество физических строк в файле.
    """
    return len(normalize_newlines(source).splitlines())


def build_file_context(
    path: Path,
    project_root: Path,
    max_lines: int | None,
) -> str:
    """
    Формирует контекст одного файла.
    """
    display_path = get_relative_display_path(path, project_root)
    source = read_python_file(path)
    line_count = count_file_lines(source)

    if max_lines is not None and line_count <= max_lines:
        return build_full_file(source, display_path)

    if is_full_file_by_name(path):
        return build_full_file(source, display_path)

    return build_reduced_file(
        path=path,
        source=source,
        display_path=display_path,
    )


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Экспортирует Python-файлы в полный или сокращенный "
            "контекст для передачи в AI."
        )
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help=(
            "Файл или директория для обработки. "
            "По умолчанию используется текущая директория."
        ),
    )

    parser.add_argument(
        "--max-lines",
        type=int,
        default=None,
        help=(
            "Максимальное количество строк для полного вывода. "
            "Если параметр не указан, все файлы обрабатываются "
            "в сокращенном режиме, кроме models.py и schemas.py."
        ),
    )

    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help=f"Путь к выходному файлу. По умолчанию: {DEFAULT_OUTPUT}",
    )

    return parser.parse_args()


def main() -> int:
    args = parse_arguments()

    if args.max_lines is not None and args.max_lines < 1:
        print(
            "Ошибка: значение --max-lines должно быть больше нуля.",
            file=sys.stderr,
        )
        return 1

    project_root = Path.cwd().resolve()
    input_path = (project_root / args.path).resolve()

    if not input_path.exists():
        print(
            f"Ошибка: путь не существует: {input_path}",
            file=sys.stderr,
        )
        return 1

    files = collect_python_files(input_path)

    if not files:
        print(
            "Ошибка: Python-файлы не найдены.",
            file=sys.stderr,
        )
        return 1

    result_parts: list[str] = []

    for file_path in files:
        try:
            context = build_file_context(
                path=file_path,
                project_root=project_root,
                max_lines=args.max_lines,
            )
        except Exception as error:
            display_path = get_relative_display_path(
                file_path,
                project_root,
            )

            context = "\n".join(
                [
                    f"# {display_path}",
                    "",
                    f"# EXPORT ERROR: {error}",
                ]
            )

        result_parts.append(context.rstrip())

    output_path = Path(args.output)

    if not output_path.is_absolute():
        output_path = project_root / output_path

    output_path.parent.mkdir(parents=True, exist_ok=True)

    output_path.write_text(
        "\n\n".join(result_parts) + "\n",
        encoding="utf-8",
    )

    print(f"Готово. Обработано файлов: {len(files)}")
    print(f"Результат сохранен в: {output_path}")

    if args.max_lines is None:
        print(
            "Режим: сокращенный вывод; "
            "models.py и schemas.py выгружены полностью."
        )
    else:
        print(
            f"Полностью выгружены файлы размером до "
            f"{args.max_lines} строк."
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())