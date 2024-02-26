from django.shortcuts import render, redirect
from .models import Usuario


def home(request):
    return render(request, 'usuarios/home.html')


def usuarios(request):
    #Salvar os dados da tela para o banco de dados.
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #Exibir todos os usuarios ja cadastrados em uma nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
     
    #Retornar os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/usuarios.html', usuarios)



def editar(request, id):
    usuario = Usuario.objects.get(id_usuario=id)
    context = {'usuario': usuario}
    return render(request, 'usuarios/update.html', context)


def update(request, id):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        nome = request.POST.get("nome")
        idade = request.POST.get("idade")
        
        # Obter o usuário a ser atualizado
        pessoa = Usuario.objects.get(id_usuario=user_id)
        
        # Atualizar os campos do usuário
        pessoa.nome = nome
        pessoa.idade = idade
        pessoa.save()
        
        return redirect('visualizacao')
 


def delete(request, id):
    pessoa = Usuario.objects.get(id_usuario=id)
    pessoa.delete()
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)

def visualizacao(request):
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)


def cadastro_login(request):
    return render(request, 'usuarios/cadastro_login.html')

def login(request):
    return render(request, 'usuarios/login.html')
