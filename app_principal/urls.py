from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('eventos/', views.evento_list, name='evento_list'),
    path('eventos/new/', views.evento_create, name='evento_create'),
    path('eventos/<int:pk>/edit/', views.evento_update, name='evento_update'),
    path('eventos/<int:pk>/delete/', views.evento_delete, name='evento_delete'),

]