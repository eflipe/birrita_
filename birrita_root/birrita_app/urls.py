from django.urls import path
from .views import BreweryListView, BreweryListCreate, BreweryListDelete, BreweryListDetail, BreweryListUpdate, BeersListCreate, BreweriesListCreate

urlpatterns = [
    # path('', views.index, name='index'),
    path('', BreweryListView.as_view(), name='list_view'),
    path('detail/<int:pk>', BreweryListDetail.as_view(), name='detail_view'),
    path('create/', BreweryListCreate.as_view(), name='create_view'),
    path('create/add/', BeersListCreate.as_view(), name='add_beer'),
    path('create/add_brewery/', BreweriesListCreate.as_view(), name='add_brewery'),
    path('edit/<int:pk>', BreweryListUpdate.as_view(), name='edit_view'),
    path('delete/<int:pk>', BreweryListDelete.as_view(), name='delete_view'),
]
