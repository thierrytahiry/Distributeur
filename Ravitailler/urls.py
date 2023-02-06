from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Ravitailler_form, name='ravitailler_insert'),
    path('<int:id>/', views.Ravitailler_form, name='ravitailler_update'),
    path('deleteRavitailler/<int:id>/', views.Ravitailler_delete, name='ravitailler_delete'),
    path('listRavitailler/', views.Ravitailler_list, name='ravitailler_list'),
]