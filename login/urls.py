from django.urls import path
from . import views

app_name = "login"
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
]