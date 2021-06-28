from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_board_data/', views.get_data, name='get_board_data'),
]
