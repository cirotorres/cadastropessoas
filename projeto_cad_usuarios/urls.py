
from django.urls import path
from app_cad_usuarios import views



urlpatterns = [
    # rota, view responsável, nome de referência
    # ex: usuarios.com(não tem nada após o end principal, então deixa sem nada '')
    path('', views.home, name='home'),

    # ex: usuarios.com/usuarios
    #path('usuarios/')

   
    path('usuarios/', views.usuarios, name='listagem_usuarios'),

    path('editar/<int:id>/', views.editar, name='editar'),

    path('update/<int:id>', views.update, name="update"),
    
    path('delete/<int:id>/', views.delete, name='delete'),
    
    path('listacompleta/', views.visualizacao, name='visualizacao'),

    # path ('auth/', views.auth, name='auth'),
    path ('cadastro_/', views.cadastro_login, name='cadastro_login'),
    
    path ('login/', views.login, name='login')

]
