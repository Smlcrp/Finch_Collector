from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('ducks/', views.DuckList.as_view(), name='duck_list'),
    path('ducks/new/', views.DuckCreate.as_view(), name='duck_create'),
]