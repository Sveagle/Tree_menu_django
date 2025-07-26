"""
Модуль административного интерфейса для управления древовидными меню.

Предоставляет кастомизированные интерфейсы для моделей Menu и MenuItem:
- Встроенное редактирование пунктов меню
- Автоматическая генерация slug
- Оптимизированные запросы к БД
- Удобная фильтрация и сортировка

Для работы требует зарегистрированные модели Menu и MenuItem.
"""

from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    """Класс для встроенного редактирования пунктов меню.

    Позволяет добавлять и редактировать пункты меню непосредственно
    на странице редактирования самого меню.
    """
    model = MenuItem
    extra = 1
    fields = ('title', 'parent', 'url', 'named_url', 'order')
    ordering = ('order',)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Административный интерфейс для управления меню.

    Обеспечивает:
    - Автоматическое создание slug из названия
    - Встроенное редактирование пунктов меню
    - Оптимизированные запросы к базе данных
    """
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    inlines = (MenuItemInline,)

    def get_queryset(self, request):
        """Оптимизирует запросы, предзагружая связанные пункты меню."""
        return super().get_queryset(request).prefetch_related('items')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Административный интерфейс для управления пунктами меню.

    Предоставляет:
    - Фильтрацию по принадлежности к меню
    - Сортировку по меню и порядку
    - Поиск по названию и URL
    - Оптимизированные запросы к БД
    """
    list_display = ('title', 'menu', 'parent', 'url', 'named_url', 'order')
    list_filter = ('menu',)
    ordering = ('menu', 'order')
    search_fields = ('title', 'url', 'named_url')

    def get_queryset(self, request):
        """Оптимизирует запросы, предзагружая связанные меню и
        родительские пункты.
        """
        return super().get_queryset(request).select_related('menu', 'parent')
