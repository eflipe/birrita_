from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import BeersList, BreweryList, BreweriesList


class BreweryListView(ListView):
    model = BreweryList
    template_name = 'birrita_app/list_view.html'
    context_object_name = 'brewery_list'


class BreweryListDetail(ListView):
    model = BreweryList
    template_name = 'birrita_app/detail_view.html'
    context_object_name = 'brewery_list'
    ordering = ['price']
    # queryset = BreweriesList.objects.filter(id=self.kwargs['id'])

    def get_queryset(self):
        qs = self.model.objects.filter(brewery=self.kwargs['pk'])
        qs = qs.order_by("-beer_type", '-data_date')
        return qs

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context['book_list'] = Book.objects.all()
        qs = self.model.objects.filter(brewery=self.kwargs['pk']).order_by('-beer_type', '-data_date')
        price_perc_list = []
        context['calc_perc'] = '-'
        # print("context['price'] --->", context['price'])
        if len(qs) > 1:
            try:
                for index, item in enumerate(qs):
                    # price_perc_list
                    if item.beer_type == qs[index+1].beer_type:
                        calc_perc = ((item.price - qs[index+1].price) / qs[index+1].price)*100
                        price_perc_list.append(round(calc_perc))
                    else:
                        price_perc_list.append('-')
            except IndexError:
                price_perc_list.append('-')

            context['calc_perc'] = price_perc_list
        return context


class BreweryListCreate(SuccessMessageMixin, CreateView):
    model = BreweryList
    form = BreweryList
    fields = "__all__"
    template_name = 'birrita_app/create_view.html'
    context_object_name = 'brewery_list'
    success_message = 'Registro creado!'

    def get_success_url(self):
        return reverse('list_view')


class BreweryListUpdate(SuccessMessageMixin, UpdateView):
    model = BreweryList
    form = BreweryList
    fields = "__all__"
    template_name = 'birrita_app/update_view.html'
    context_object_name = 'brewery_list'
    success_message = 'Registro actualizado!'

    def get_success_url(self):
        return reverse('list_view')


class BreweryListDelete(SuccessMessageMixin, DeleteView):
    model = BreweryList
    form = BreweryList
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Deleted!'
        messages.success(self.request, success_message, extra_tags='danger')
        return reverse('list_view')


class BeersListCreate(SuccessMessageMixin, CreateView):
    model = BeersList
    form = BeersList
    fields = "__all__"
    template_name = 'birrita_app/add_beer.html'
    context_object_name = 'beer_list'

    def get_success_url(self):
        return reverse('create_view')


class BreweriesListCreate(SuccessMessageMixin, CreateView):
    model = BreweriesList
    form = BreweriesList
    fields = "__all__"
    template_name = 'birrita_app/add_brewery.html'
    context_object_name = 'brewery_list'

    def get_success_url(self):
        return reverse('create_view')


def index(request):
    template = 'birrita_app/index.html'
    return render(request, template)
