# 🌳 Древовидное меню для Django

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://python.org)
[![Django](https://img.shields.io/badge/Django-3.2%2B-green)](https://djangoproject.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Простое и эффективное решение для создания древовидных меню в Django-проектах с минимальными затратами ресурсов.

## 🚀 Быстрый старт

### Установка
1. Добавьте приложение в проект:
```bash
python manage.py startapp tree_menu
```

2. Добавьте в `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'tree_menu',
]
```

3. Примените миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```

## 🛠 Использование

### 1. Создание меню
1. Зайдите в админ-панель (`/admin`)
2. Создайте новое меню (например, "main_menu")
3. Добавьте пункты меню с указанием иерархии

### 2. Вставка в шаблон
```html
{% load menu_tags %}
{% draw_menu 'main_menu' %}
```

## ⚙️ Конфигурация

### Модели
| Модель      | Описание                          |
|-------------|-----------------------------------|
| `Menu`      | Контейнер меню (название, slug)   |
| `MenuItem`  | Пункты меню с древовидной структурой |

### Параметры тега
```html
{% draw_menu 'menu_name' [template='custom_template.html'] [css_class='my-class'] %}
```

## 🎨 Примеры

### Базовая реализация
```html
<div class="navigation">
  {% load menu_tags %}
  {% draw_menu 'main_menu' %}
</div>
```

### Стилизация
```css
/* Пример CSS стилей */
.menu {
  list-style: none;
  padding: 0;
  font-family: Arial, sans-serif;
}

.menu-item {
  margin: 8px 0;
  position: relative;
}

.menu-item a {
  text-decoration: none;
  color: #333;
  padding: 6px 12px;
  display: block;
  transition: all 0.3s ease;
}

.menu-item a:hover {
  background-color: #f5f5f5;
}

.submenu {
  padding-left: 20px;
  display: none;
}

.menu-item.active > .submenu,
.menu-item.expanded > .submenu {
  display: block;
}

.active > a {
  font-weight: bold;
  color: #2c83b6;
}
```

## ✨ Особенности

- **Автоматическая активность** - подсветка текущего раздела
- **Named URLs** - поддержка именованных маршрутов
- **Оптимизация** - всего 1 SQL-запрос на меню
- **Гибкость** - кастомизация через шаблоны
- **Админка** - удобное управление через стандартный интерфейс Django

## 🧪 Тестирование
```bash
python manage.py test tree_menu
```
## 🛠 Тестирование админ-панели

### Доступ в админку
1. Создайте суперпользователя (если еще нет):
   ```bash
   python manage.py createsuperuser

## 📦 Требования

- Python 3.7+
- Django 3.2+

## 📄 Лицензия

Проект распространяется под лицензией [MIT](LICENSE).