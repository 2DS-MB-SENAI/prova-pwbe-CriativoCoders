from django.urls import path
from .views import lista_de_medicos, criar_consulta

urlpatterns = [
    path('lista', lista_de_medicos, name='lista_de_medicos'),
    path('criar/', criar_consulta, name='criar_consulta'),
]