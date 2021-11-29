from django.urls import path

from project_files.project_polls import views

urlpatterns = [
    path('', views.index, name='index'),
]