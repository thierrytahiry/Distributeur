from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Dab_form, name='dab_insert'),
    path('<int:id>/', views.Dab_form, name='dab_update'),
    path('edit/<int:id>/', views.Dab_Edit_form, name='dab_edit'),
    path('deleteDab/<int:id>/', views.Dab_delete, name='dab_delete'),
    path('listDab/', views.Dab_list, name='dab_list'),
]