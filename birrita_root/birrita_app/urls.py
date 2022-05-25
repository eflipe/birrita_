from django.urls import path
from . import views
from .views import BeersListView, BeersListCreate, BeersListDelete, BeersListDetail, BeersListUpdate

urlpatterns = [
    # path('', views.index, name='index'),
    path('', BeersListView.as_view(), name='list_view'),
    path('detail/<int:pk>', BeersListDetail.as_view(), name='detail_view'),
    path('create/', BeersListCreate.as_view(), name='create_view'),
    path('edit/<int:pk>', BeersListUpdate.as_view(), name='edit_view'),
    path('delete/<int:pk>', BeersListDelete.as_view(), name='delete_view'),
]
