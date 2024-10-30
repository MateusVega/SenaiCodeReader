from django.urls import path
from . import views

urlpatterns = [
    path('', views.scan, name='scanning'),
    path('add/', views.add, name='add'),
    path('save_qr_data/', views.save_qr_data, name='save_qr_data')
]