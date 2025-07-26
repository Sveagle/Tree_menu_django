"""
Модуль тестирования для приложения tree_menu.

Содержит тесты:
- MenuModelTest: Тесты модели Menu
- MenuItemModelTest: Тесты модели MenuItem
- MenuTagsTest: Тесты template tag для меню
"""

from django.test import TestCase, RequestFactory
from .models import Menu, MenuItem
from .templatetags.menu_tags import draw_menu


class MenuModelTest(TestCase):
    """Тесты для модели Menu."""

    @classmethod
    def setUpTestData(cls):
        cls.menu = Menu.objects.create(name="Main", slug="main")

    def test_menu_creation(self):
        """Тест создания меню."""
        self.assertEqual(self.menu.name, "Main")
        self.assertEqual(self.menu.slug, "main")


class MenuItemModelTest(TestCase):
    """Тесты для модели MenuItem."""

    @classmethod
    def setUpTestData(cls):
        cls.menu = Menu.objects.create(name="Test", slug="test")
        cls.item = MenuItem.objects.create(
            menu=cls.menu,
            title="Item 1",
            url="/test/",
            order=1
        )

    def test_menu_item_creation(self):
        """Тест создания пункта меню."""
        self.assertEqual(self.item.title, "Item 1")
        self.assertEqual(self.item.menu.name, "Test")


class MenuTagsTest(TestCase):
    """Тесты для template tag draw_menu."""

    @classmethod
    def setUpTestData(cls):
        cls.factory = RequestFactory()
        cls.menu = Menu.objects.create(name="Main", slug="main")
        cls.item = MenuItem.objects.create(
            menu=cls.menu,
            title="Home",
            url="/",
            order=1
        )

    def test_draw_menu_with_items(self):
        """Тест работы тега draw_menu с пунктами меню."""
        request = self.factory.get('/')
        context = {'request': request}
        result = draw_menu(context, 'main')
        self.assertIn('menu_tree', result)
