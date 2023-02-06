from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Ticket_form, name='ticket_insert'),
    path('<int:id>/', views.Ticket_form, name='ticket_update'),
    path('deleteTicket/<int:id>/', views.Ticket_delete, name='ticket_delete'),
    path('listTicket/', views.Ticket_list, name='ticket_list'),
]