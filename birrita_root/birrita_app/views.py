from django.shortcuts import render
from django.views.generic.list import ListView
from .models import BeersList


class BeersListView(ListView):
    model = BeersList
    template_name = 'birrita_app/list_view.html'
    context_object_name = 'beers_list'


def index(request):
    template = 'birrita_app/index.html'
    return render(request, template)
