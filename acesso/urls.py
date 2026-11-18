from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_acesso, name='registrar_acesso'),
    path('historico/', views.historico_acesso, name='historico_acesso'),
]