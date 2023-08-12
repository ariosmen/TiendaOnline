from django.urls import path
from tienda import views

urlpatterns = [
    path('tienda', views.tienda, name='tienda'),
]
