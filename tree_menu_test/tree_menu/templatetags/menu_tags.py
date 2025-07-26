"""
Template tag для отображения древовидного меню.
"""

from django import template
from django.urls import NoReverseMatch
from ..models import Menu

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """
    Отображает древовидное меню по его имени.

    Аргументы:
        context (dict): Контекст шаблона с объектом запроса
        menu_name (str): Название меню для отображения

    Возвращает:
        dict: Контекст с древом меню и его названием

    Использование:
        {% load menu_tags %}
        {% draw_menu 'main_menu' %}
    """
    request = context['request']
    current_url = request.path_info

    try:
        menu = Menu.objects.prefetch_related('items').get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu_tree': [], 'menu_name': menu_name}

    menu_items = list(menu.items.all())

    active_item = None
    for item in menu_items:
        try:
            if item.get_url() == current_url:
                active_item = item
                break
        except NoReverseMatch:
            continue

    menu_tree = []
    item_dict = {}

    for item in menu_items:
        item_dict[item.id] = {
            'item': item,
            'children': [],
            'is_active': False,
            'is_expanded': False,
        }

    for item in menu_items:
        if item.parent_id is None:
            menu_tree.append(item_dict[item.id])
        else:
            parent = item_dict.get(item.parent_id)
            if parent:
                parent['children'].append(item_dict[item.id])

    if active_item:
        current = active_item
        while current:
            node = item_dict.get(current.id)
            if node:
                node['is_expanded'] = True
                node['is_active'] = True
            current = current.parent

        active_node = item_dict.get(active_item.id)
        if active_node:
            for child in active_node['children']:
                child['is_expanded'] = True

    return {
        'menu_tree': menu_tree,
        'menu_name': menu_name,
    }
