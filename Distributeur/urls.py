"""Distributeur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Operateur.urls')),
    path('Agence/', include('Agence.urls')),
    path('Carte/', include('Carte.urls')),
    path('Client/', include('Client.urls')),
    path('Compte/', include('Compte.urls')),
    path('Dab/', include('Dab.urls')),
    path('Operateur/', include('Operateur.urls')),
    path('Ravitailler/', include('Ravitailler.urls')),
    path('Ticket/', include('Ticket.urls')),
    path('Transaction/', include('Transaction.urls')),
    path('Type/', include('Type.urls')),
]
