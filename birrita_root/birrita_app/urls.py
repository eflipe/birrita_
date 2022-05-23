from django.urls import path
from . import views
from .views import BeersListView

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', BeersListView.as_view(), name='list_view'),
]
