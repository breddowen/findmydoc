<!-- ./frontend/app/components/content/RichTextEditor.vue -->
<script setup>
import { useEditor, EditorContent } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'
import Link from '@tiptap/extension-link'
import Underline from '@tiptap/extension-underline'
import Placeholder from '@tiptap/extension-placeholder'

const model = defineModel({
  type: String,
  default: '',
})

const props = defineProps({
  placeholder: {
    type: String,
    default: 'Введите текст...',
  },
  minHeight: {
    type: String,
    default: '24rem',
  },
  disabled: {
    type: Boolean,
    default: false,
  },
})

const editor = useEditor({
  content: model.value,

  editable: !props.disabled,

  extensions: [
    StarterKit.configure({
      heading: {
        levels: [2, 3, 4],
      },
    }),

    Underline,

    Link.configure({
      openOnClick: false,
      autolink: true,
      linkOnPaste: true,
      HTMLAttributes: {
        rel: 'noopener noreferrer',
        target: '_blank',
      },
    }),

    Placeholder.configure({
      placeholder: props.placeholder,
    }),
  ],

  onUpdate({ editor: currentEditor }) {
    model.value = currentEditor.getHTML()
  },
})

watch(
  () => model.value,
  (newValue) => {
    if (!editor.value) return

    const currentValue = editor.value.getHTML()

    if (newValue !== currentValue) {
      editor.value.commands.setContent(
        newValue || '',
        {
          emitUpdate: false,
        },
      )
    }
  },
)

watch(
  () => props.disabled,
  (value) => {
    editor.value?.setEditable(!value)
  },
)

function setLink() {
  if (!editor.value) return

  const previousUrl =
    editor.value.getAttributes('link').href || ''

  const url = window.prompt(
    'Введите адрес ссылки',
    previousUrl,
  )

  if (url === null) return

  if (!url.trim()) {
    editor.value
      .chain()
      .focus()
      .extendMarkRange('link')
      .unsetLink()
      .run()

    return
  }

  editor.value
    .chain()
    .focus()
    .extendMarkRange('link')
    .setLink({
      href: url.trim(),
    })
    .run()
}

function clearFormatting() {
  editor.value
    ?.chain()
    .focus()
    .clearNodes()
    .unsetAllMarks()
    .run()
}

onBeforeUnmount(() => {
  editor.value?.destroy()
})
</script>

<template>
  <div
    class="border-base-300 bg-base-100 overflow-hidden rounded-2xl border"
    :class="{
      'opacity-60': disabled,
    }"
  >
    <div
      v-if="editor"
      class="border-base-300 bg-base-200 flex flex-wrap gap-1 border-b p-2"
    >
      <button
        type="button"
        class="btn btn-square btn-sm"
        :class="{
          'btn-primary': editor.isActive('bold'),
          'btn-ghost': !editor.isActive('bold'),
        }"
        title="Жирный"
        :disabled="disabled"
        @click="editor.chain().focus().toggleBold().run()"
      >
        <Icon
          name="lucide:bold"
          class="size-4"
        />
      </button>

      <button
        type="button"
        class="btn btn-square btn-sm"
        :class="{
          'btn-primary': editor.isActive('italic'),
          'btn-ghost': !editor.isActive('italic'),
        }"
        title="Курсив"
        :disabled="disabled"
        @click="editor.chain().focus().toggleItalic().run()"
      >
        <Icon
          name="lucide:italic"
          class="size-4"
        />
      </button>

      <button
        type="button"
        class="btn btn-square btn-sm"
        :class="{
          'btn-primary': editor.isActive('underline'),
          'btn-ghost': !editor.isActive('underline'),
        }"
        title="Подчёркнутый"
        :disabled="disabled"
        @click="editor.chain().focus().toggleUnderline().run()"
      >
        <Icon
          name="lucide:underline"
          class="size-4"
        />
      </button>

      <div class="divider divider-horizontal mx-0" />

      <button
        v-for="level in [2, 3, 4]"
        :key="level"
        type="button"
        class="btn btn-sm"
        :class="{
          'btn-primary': editor.isActive(
            'heading',
            { level },
          ),
          'btn-ghost': !editor.isActive(
            'heading',
            { level },
          ),
        }"
        :title="`Заголовок ${level}`"
        :disabled="disabled"
        @click="
          editor
            .chain()
            .focus()
            .toggleHeading({ level })
            .run()
        "
      >
        H{{ level }}
      </button>

      <div class="divider divider-horizontal mx-0" />

      <button
        type="button"
        class="btn btn-square btn-sm"
        :class="{
          'btn-primary': editor.isActive('bulletList'),
          'btn-ghost': !editor.isActive('bulletList'),
        }"
        title="Маркированный список"
        :disabled="disabled"
        @click="
          editor
            .chain()
            .focus()
            .toggleBulletList()
            .run()
        "
      >
        <Icon
          name="lucide:list"
          class="size-4"
        />
      </button>

      <button
        type="button"
        class="btn btn-square btn-sm"
        :class="{
          'btn-primary': editor.isActive('orderedList'),
          'btn-ghost': !editor.isActive('orderedList'),
        }"
        title="Нумерованный список"
        :disabled="disabled"
        @click="
          editor
            .chain()
            .focus()
            .toggleOrderedList()
            .run()
        "
      >
        <Icon
          name="lucide:list-ordered"
          class="size-4"
        />
      </button>

      <button
        type="button"
        class="btn btn-square btn-sm"
        :class="{
          'btn-primary': editor.isActive('blockquote'),
          'btn-ghost': !editor.isActive('blockquote'),
        }"
        title="Цитата"
        :disabled="disabled"
        @click="
          editor
            .chain()
            .focus()
            .toggleBlockquote()
            .run()
        "
      >
        <Icon
          name="lucide:quote"
          class="size-4"
        />
      </button>

      <button
        type="button"
        class="btn btn-square btn-sm"
        :class="{
          'btn-primary': editor.isActive('codeBlock'),
          'btn-ghost': !editor.isActive('codeBlock'),
        }"
        title="Блок кода"
        :disabled="disabled"
        @click="
          editor
            .chain()
            .focus()
            .toggleCodeBlock()
            .run()
        "
      >
        <Icon
          name="lucide:code-2"
          class="size-4"
        />
      </button>

      <button
        type="button"
        class="btn btn-square btn-sm"
        :class="{
          'btn-primary': editor.isActive('link'),
          'btn-ghost': !editor.isActive('link'),
        }"
        title="Ссылка"
        :disabled="disabled"
        @click="setLink"
      >
        <Icon
          name="lucide:link"
          class="size-4"
        />
      </button>

      <div class="ml-auto flex gap-1">
        <button
          type="button"
          class="btn btn-square btn-ghost btn-sm"
          title="Отменить"
          :disabled="
            disabled
            || !editor.can().chain().focus().undo().run()
          "
          @click="editor.chain().focus().undo().run()"
        >
          <Icon
            name="lucide:undo-2"
            class="size-4"
          />
        </button>

        <button
          type="button"
          class="btn btn-square btn-ghost btn-sm"
          title="Повторить"
          :disabled="
            disabled
            || !editor.can().chain().focus().redo().run()
          "
          @click="editor.chain().focus().redo().run()"
        >
          <Icon
            name="lucide:redo-2"
            class="size-4"
          />
        </button>

        <button
          type="button"
          class="btn btn-square btn-ghost btn-sm"
          title="Очистить форматирование"
          :disabled="disabled"
          @click="clearFormatting"
        >
          <Icon
            name="lucide:eraser"
            class="size-4"
          />
        </button>
      </div>
    </div>

    <EditorContent
      :editor="editor"
      class="rich-text-editor"
      :style="{
        '--editor-min-height': minHeight,
      }"
    />
  </div>
</template>

<style>
.rich-text-editor .tiptap {
  min-height: var(--editor-min-height);
  padding: 1rem;
  outline: none;
  line-height: 1.7;
}

.rich-text-editor .tiptap p {
  margin: 0.75rem 0;
}

.rich-text-editor .tiptap h2 {
  margin: 1.5rem 0 0.75rem;
  font-size: 1.5rem;
  font-weight: 700;
}

.rich-text-editor .tiptap h3 {
  margin: 1.25rem 0 0.625rem;
  font-size: 1.25rem;
  font-weight: 700;
}

.rich-text-editor .tiptap h4 {
  margin: 1rem 0 0.5rem;
  font-size: 1.125rem;
  font-weight: 600;
}

.rich-text-editor .tiptap ul {
  margin: 0.75rem 0;
  list-style: disc;
  padding-left: 1.5rem;
}

.rich-text-editor .tiptap ol {
  margin: 0.75rem 0;
  list-style: decimal;
  padding-left: 1.5rem;
}

.rich-text-editor .tiptap blockquote {
  margin: 1rem 0;
  border-left: 0.25rem solid var(--color-primary);
  padding-left: 1rem;
  opacity: 0.8;
}

.rich-text-editor .tiptap pre {
  overflow-x: auto;
  border-radius: 0.75rem;
  background: var(--color-base-300);
  padding: 1rem;
}

.rich-text-editor .tiptap a {
  color: var(--color-primary);
  text-decoration: underline;
}

.rich-text-editor .tiptap p.is-editor-empty:first-child::before {
  pointer-events: none;
  float: left;
  height: 0;
  color: color-mix(
    in oklab,
    currentColor 40%,
    transparent
  );
  content: attr(data-placeholder);
}
</style>