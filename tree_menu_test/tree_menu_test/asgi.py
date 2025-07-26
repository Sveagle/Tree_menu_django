"""
ASGI config for tree_menu_test project.

"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tree_menu_test.settings')

application = get_asgi_application()
