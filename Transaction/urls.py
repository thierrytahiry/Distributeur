from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Transaction_form, name='transaction_insert'),
    path('<int:id>/', views.Transaction_form, name='transaction_update'),
    path('deleteTransaction/<int:id>/', views.Transaction_delete, name='transaction_delete'),
    path('listTransaction/', views.Transaction_list, name='transaction_list'),
    path('pageChoix/', views.PageChoix, name='page_choix'),
    path('pageRetirer/', views.PageRetirer, name='page_retirer'),
    path('pageDepot/', views.PageDepot, name='page_depot'),
    path('pageSolde/', views.PageSolde, name='page_solde'),
    path('autreMontant/', views.AutreMontant, name='autre_montant'),
    path('pageReçus/',views.PageReçus, name ='page_reçus'),
    path('pageRelever/',views.PageRelever, name ='page_relever'),
    path('pageChart/',views.PageChart, name='page_chart')
]