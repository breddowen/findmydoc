# API карта
./helper_functions/export-api-map.ps1
./helper_functions/export-api-map.ps1 -IncludeSchemas

# Контекст для AI
./helper_functions/export-context.ps1 -Module "users"
./helper_functions/export-context.ps1 -Module "agents" -IncludeSchemas
./helper_functions/export-context.ps1 -Module "users" -IncludeSchemas

# Структура проекта
./helper_functions/export-structure.ps1 -IncludeLineCounts
./helper_functions/export-structure.ps1
./helper_functions/export-structure.ps1 -IncludeDeploy

# Файлы сжато
python ./helper_functions/export_context.py backend --max-lines 1000 --output helper_functions/backend_context.txt
python ./helper_functions/export_context.py backend/app/modules/ai_agents/patients --max-lines 1000 --output helper_functions/patients_context.txt
python ./helper_functions/export_context.py backend/app/modules/ai_agents/superusers --max-lines 500 --output helper_functions/superusers_context.txt

python ./helper_functions/export_context.py
python ./helper_functions/export_context.py backend
python ./helper_functions/export_context.py backend/app/modules
python ./helper_functions/export_context.py backend --max-lines 1000 --output helper_functions/backend_context.txt
python ./helper_functions/export_context.py backend/app/modules/ai_agents
python ./helper_functions/export_context.py backend/app/modules --max-lines 1000 --output ai_context.txt


# Поиск по коду
./helper_functions/search-code.ps1 "create_payment"
./helper_functions/search-code.ps1 -BuildIndex

#
# Экспорт всех импортов (Python + JS/Vue)
./helper_functions/export-imports.ps1 -PythonOnly

# Только JS/Vue
./helper_functions/export-imports.ps1 -JSOnly

# С подробным выводом
./helper_functions/export-imports.ps1 -VerboseOutput

# Свой файл
./helper_functions/export-imports.ps1 -OutputFile "C:\temp\my-imports.md"