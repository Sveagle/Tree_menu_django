"""
Модуль моделей для древовидного меню.

Содержит модели:
- Menu - для хранения меню
- MenuItem - для хранения пунктов меню
"""

from django.db import models
from django.urls import reverse, NoReverseMatch
from django.utils.text import slugify


class Menu(models.Model):
    """Модель для хранения меню."""

    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название меню'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Слаг меню'
    )

    class Meta:
        """Мета-класс для модели Menu."""
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self) -> str:
        """Строковое представление модели."""
        return str(self.name)

    def save(self, *args, **kwargs):
        """Сохраняет модель, генерируя slug при необходимости."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class MenuItem(models.Model):
    """Модель для хранения пунктов меню."""

    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Меню'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Родительский пункт'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название пункта'
    )
    url = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='URL или named URL'
    )
    named_url = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Named URL'
    )
    order = models.IntegerField(
        default=0,
        verbose_name='Порядок'
    )

    class Meta:
        """Мета-класс для модели MenuItem."""
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ['order']

    def __str__(self) -> str:
        """Строковое представление модели."""
        return str(self.title)

    def get_url(self) -> str:
        """Возвращает URL для пункта меню.

        Проверяет named_url, затем url, возвращает '/' по умолчанию.
        """
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return self.url or '/'
        return self.url or '/'
