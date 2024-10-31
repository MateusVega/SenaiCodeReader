from django.urls import path
from . import views

app_name = "reader"
urlpatterns = [
    path('', views.scan, name='scan'),
    path('add/', views.add, name='add'),
    path('save_qr_data/', views.save_qr_data, name='save_qr_data'),
    path('off_to_on/', views.off_to_on, name='off_to_on'),
    path('reset/', views.reset, name='reset'),
    path('delete_line/', views.delete_line, name='delete_line'),
]