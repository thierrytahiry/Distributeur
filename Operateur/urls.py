from django.urls import path,include
from . import views

urlpatterns = [
	path('', views.login_view, name='login'),
    path('insertOp/', views.Operateur_form, name='operateur_insert'),
    path('<int:id>/', views.Operateur_form, name='operateur_update'),
    path('deleteOperateur/<int:id>/', views.Operateur_delete, name='operateur_delete'),
    path('listOperateur/', views.Operateur_list, name='operateur_list'),
    # path('login/', views.login_view, name='login'),
]