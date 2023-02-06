from django.urls import path,include
from . import views

urlpatterns = [
    path('carteInsert', views.Carte_form, name='carte_insert'),
    path('<int:id>/', views.Carte_form, name='carte_update'),
    path('deleteCarte/<int:id>/', views.Carte_delete, name='carte_delete'),
    path('listCarte/', views.Carte_list, name='carte_list'),
    path('formecarte/', views.formecarte, name='num_carte'),
    path('formenip/', views.formenip, name='code_nip'),
    path('', views.index, name='index'),
    # path('', views.DabDispo, name='dab_dispo'),
]