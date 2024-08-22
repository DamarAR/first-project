from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_todo, name='add'),
    path('complete/<todo_id>', views.complete_todo, name='complete'),
    path('delete/<todo_id>', views.delete_todo, name='delete'),


    path('profile/', views.profile, name='profile'),

    path('data-json/', views.data_json, name='data-json'),
]