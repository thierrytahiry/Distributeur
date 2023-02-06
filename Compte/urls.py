from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Compte_form, name='compte_insert'),
    path('<int:id>/', views.Compte_form, name='compte_update'),
    path('deleteCompte/<int:id>/', views.Compte_delete, name='compte_delete'),
    path('listCompte/', views.Compte_list, name='compte_list'),
]