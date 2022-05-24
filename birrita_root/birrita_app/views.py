from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import BeersList


class BeersListView(ListView):
    model = BeersList
    template_name = 'birrita_app/list_view.html'
    context_object_name = 'beers_list'


class BeersListDetail(DetailView):
    model = BeersList
    template_name = 'birrita_app/detail_view.html'
    context_object_name = 'beers_list'


class BeersListCreate(SuccessMessageMixin, CreateView):
    model = BeersList
    form = BeersList
    fields = "__all__"
    template_name = 'birrita_app/create_view.html'
    context_object_name = 'beers_list'
    success_message = 'Registro creado!'

    def get_success_url(self):
        return reverse('list_view')


class BeersListUpdate(SuccessMessageMixin, UpdateView):
    model = BeersList
    form = BeersList
    fields = "__all__"
    template_name = 'birrita_app/update_view.html'
    context_object_name = 'beers_list'
    success_message = 'Registro actualizado!'

    def get_success_url(self):
        return reverse('list_view')


class BeersListDelete(SuccessMessageMixin, DeleteView):
    model = BeersList
    form = BeersList
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Deleted!'
        messages.success(self.request, (success_message))
        return reverse('list_view')


def index(request):
    template = 'birrita_app/index.html'
    return render(request, template)
