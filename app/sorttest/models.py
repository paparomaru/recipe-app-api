from django.db import models
from django.utils import timezone


class Title(models.Model):
    date_added = models.DateTimeField(
        verbose_name='Дата создания',  # Наименование в админке
        default=timezone.now,  # Сохранянем дату создания записи по умолчанию
    )
    title = models.CharField(
        verbose_name='Заголовок',  # Наименование в админке
        max_length=200,  # Обязательное поле максимального размера поля
    )

    def __str__(self):
        return f'#{self.date_added} {self.title}' # Читабельный вывод в заголовке

    class Meta:
        verbose_name = 'Заголовок'  # Наименование всей таблицы в админке
        verbose_name_plural = 'Заголовки'  # т.к. LANGUAGE_CODE = 'en-us' пропишим и множественное число
