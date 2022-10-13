
from django.urls import path
from . import views #arquivo views que ainda não utilizamos

urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),
    path('listar_categorias', views.listar_categorias, name='listar_categorias'), 
    path('listar_autores', views.listar_autores, name='listar_autores'), 
    path('livro/<int:id>/', views.detalhar_livro, name='detalhar_livro'), 
    path('livro/novo/', views.cadastrar_livro, name='cadastrar_livro'),
    path('livro/editar/<int:id>/', views.editar_livro, name='editar_livro'),
    path('buscar_livro', views.buscar_livro, name='buscar_livro'),
    #rotas do login e logout
    path('page_login', views.page_login, name='page_login'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
    path('logout_usuario', views.logout_usuario, name='logout_usuario'),
]