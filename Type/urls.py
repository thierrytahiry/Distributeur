from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Type_form, name='type_insert'),
    path('<int:id>/', views.Type_form, name='type_update'),
    path('deleteType/<int:id>/', views.Type_delete, name='type_delete'),
    path('listType/', views.Type_list, name='type_list'),
]