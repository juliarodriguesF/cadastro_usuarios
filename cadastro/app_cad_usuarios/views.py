from django.shortcuts import render
from .models import Usuarios

def home (request):
    return render(request, 'usuarios/home.html')

def usuarios (request):
    #salvar as informações no banco de dados
    novo_usuario = Usuarios()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.save()
    #exibir todos os usuarios ja cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuarios.objects.all()
    }
    #retornar os dados para a pagina de listagem de usuarios
    return render (request, 'usuarios/usuarios.html', usuarios)


