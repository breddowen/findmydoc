Удалить:


backend/app/modules/test_styles/

frontend/app/utils/test-styles.js
frontend/app/stores/test-styles.js
frontend/app/plugins/test-styles.client.js
frontend/app/middleware/test-styles.js
frontend/app/pages/settings/test-styles.vue
frontend/app/components/test-styles/
Удалить точки подключения с пометкой TEST_STYLES:

импорт и include_router в backend/app/main.py;
пункт навигации в frontend/app/composables/useAppNavigation.js;
<TestStylesNavbarActions /> в frontend/app/components/layout/Navbar.vue.
Оставшиеся записи localStorage больше ни на что влиять не будут. При желании их можно удалить по префиксу mentalme_test_styles_.

Важно: если вы начнёте менять исходный main.css ещё до удаления студии, поднимите STYLE_VERSION в frontend/app/utils/test-styles.js. Это не позволит старому локальному варианту незаметно перекрывать уже обновлённые базовые стили.