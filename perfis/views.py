from django.shortcuts import render
from perfis.models import Perfil

def index(request):
  return render(request, 'index.html')

def exibir(request, perfil_id):

  perfil = Perfil()

  if perfil_id == '1':
    perfil = Perfil('Lucas Dias', 'lucas@lucas.com.br', '7777777', 'X')

  if perfil_id == '2':
    perfil = Perfil('Pedro Silva', 'pedro@pedro.com.br', '888888', 'Y')

  return render(request, 'perfil.html', { "perfil" : perfil})