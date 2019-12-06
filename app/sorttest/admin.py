from django.contrib import admin

from .forms import TitleForm
from .models import Title


@admin.register(Title)  # Зарегили модель в админке
class TitleAdmin(admin.ModelAdmin):
    list_display = ('date_added', 'title')  # те поля которые будут отображаться в админке
    form = TitleForm  # Наша форма с нужным нам интерфейсом