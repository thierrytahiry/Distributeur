from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Client_form, name='client_insert'),
    path('<int:id>/', views.Client_form, name='client_update'),
    path('deleteClient/<int:id>/', views.Client_delete, name='client_delete'),
    path('listClient/', views.Client_list, name='client_list'),
]