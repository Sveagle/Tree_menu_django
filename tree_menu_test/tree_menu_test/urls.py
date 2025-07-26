"""
URL configuration for tree_menu_test project.

"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('test-menu/', TemplateView.as_view(template_name='test_menu.html'),
         name='test_menu'),
]
