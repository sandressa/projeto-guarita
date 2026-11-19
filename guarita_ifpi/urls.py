from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alunos.urls')), 
    # A linha do 'acesso' abaixo está desativada com o # para não dar erro
    # path('acesso/', include('acesso.urls')), 
]