from django.urls import path
from . import views

urlpatterns = [
    # Autenticação
    path('', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Tarefas
    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),
    path('tarefas/nova/', views.criar_tarefa, name='criar_tarefa'),
    path('tarefas/<int:pk>/', views.detalhes_tarefa, name='detalhes_tarefa'),
    path('tarefas/<int:pk>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('tarefas/<int:pk>/deletar/', views.deletar_tarefa, name='deletar_tarefa'),
    path('tarefas/<int:pk>/toggle/', views.toggle_tarefa, name='toggle_tarefa'),

    # Projetos
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('projetos/novo/', views.criar_projeto, name='criar_projeto'),
    path('projetos/<int:pk>/', views.detalhes_projeto, name='detalhes_projeto'),
    path('projetos/<int:pk>/editar/', views.editar_projeto, name='editar_projeto'),
    path('projetos/<int:pk>/deletar/', views.deletar_projeto, name='deletar_projeto'),
]
