from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Agence_form, name='agence_insert'),
    path('<int:id>/', views.Agence_form, name='agence_update'),
    path('deleteAgence/<int:id>/', views.Agence_delete, name='agence_delete'),
    path('listAgence/', views.Agence_list, name='agence_list'),
]