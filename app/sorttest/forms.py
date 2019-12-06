from django import forms

from .models import Title


class TitleForm(forms.ModelForm):  # Форма таблицы заголовков
    class Meta:
        model = Title
        fields = (
            # 'date_added',  # По тз отключаем редактирование данного поля (просто прячем его)
            'title',
        )
        widgets = {
            'title': forms.TextInput,
        }