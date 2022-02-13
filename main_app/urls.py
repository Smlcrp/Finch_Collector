from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('ducks/', views.DuckList.as_view(), name='duck_list'),
    path('ducks/new/', views.DuckCreate.as_view(), name='duck_create'),
    path('ducks/<int:pk>/', views.DuckDetail.as_view(), name='duck_detail'),
    path('ducks/<int:pk>/update', views.DuckUpdate.as_view(), name="duck_update"),
    path('ducks/<int:pk>/delete', views.DuckDelete.as_view(), name='duck_delete')
]