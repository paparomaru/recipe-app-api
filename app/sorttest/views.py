from django.views.generic import ListView

from .models import Title


class TitleListView(ListView):  #Для вывода переопределяем стандартный класс ListViews и в шаблоне попользуем object_list
    template_name = 'sorttest/title_list.html'   # Расположение файла шаблона
    queryset = Title.objects.order_by('-date_added')   # Запрашиваем все записи и применяем к ним обратную сортировку по полю date_add