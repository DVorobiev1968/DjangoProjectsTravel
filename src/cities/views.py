from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from cities.forms import HtmlForm, CityForm
from cities.models import City

__all__ = (
    'home', 'CityDetailView', 'CityCreateView', 'CityUpdateView',
    'CityDeleteView', 'CityListView'
)


def home(request, pk=None):
    if request.method == 'POST':
        # вывод в консоль, т.к. файл отображения уже задан
        form = CityForm(request.POST)
        # проверим все ли типы данных заявленных в форме корректны, в том числе уникальность
        # в случае успеха выведем данные в консоль
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    # pk будет передаваться через адресную строку
    if pk:
        # используем метод filter для того чтобы не было ошибки если зададим несуществующий pk
        # city=City.objects.filter(id=pk).first()
        # этот метод уже возвратит ошибку и его нужно использовать с конструкцией try... exception, чтобы такую ошибку ловить
        # city = City.objects.get(id=pk)
        # либо получаем ошибку о несуществующем объекте через функцию фреймворка django
        city = get_object_or_404(City, id=pk)
        context = {'object': city}
        return render(request, 'cities/detail.html', context)
    form = CityForm()
    qs = City.objects.all()
    lst = Paginator(qs, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, 'form': form}
    # context = {'object_list': qs, 'form': form}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')


class CityDeleteView(DeleteView):
    model = City
    # для плдтверждения удаления перенаправляем на специальную для этого страницу
    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')

    # либо делаем безусловное удаление
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CityListView(ListView):
    paginate_by = 2
    model = City
    template_name = 'cities/home.html'
