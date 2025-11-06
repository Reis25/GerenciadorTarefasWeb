from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Tarefa, Projeto, Comentario


class ProjetoModelTest(TestCase):
    """Testes para o model Projeto"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.projeto = Projeto.objects.create(
            nome='Projeto Teste',
            descricao='Descrição do projeto teste',
            usuario=self.user,
            cor='#FF0000'
        )

    def test_projeto_criacao(self):
        """Testa se o projeto é criado corretamente"""
        self.assertEqual(self.projeto.nome, 'Projeto Teste')
        self.assertEqual(self.projeto.usuario, self.user)
        self.assertEqual(self.projeto.cor, '#FF0000')

    def test_projeto_str(self):
        """Testa a representação em string do projeto"""
        self.assertEqual(str(self.projeto), 'Projeto Teste')


class TarefaModelTest(TestCase):
    """Testes para o model Tarefa"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.projeto = Projeto.objects.create(
            nome='Projeto Teste',
            usuario=self.user
        )
        self.tarefa = Tarefa.objects.create(
            titulo='Tarefa Teste',
            descricao='Descrição da tarefa',
            prioridade='alta',
            status='pendente',
            usuario=self.user,
            projeto=self.projeto
        )

    def test_tarefa_criacao(self):
        """Testa se a tarefa é criada corretamente"""
        self.assertEqual(self.tarefa.titulo, 'Tarefa Teste')
        self.assertEqual(self.tarefa.prioridade, 'alta')
        self.assertEqual(self.tarefa.status, 'pendente')
        self.assertFalse(self.tarefa.concluida)

    def test_tarefa_str(self):
        """Testa a representação em string da tarefa"""
        self.assertEqual(str(self.tarefa), 'Tarefa Teste')

    def test_tarefa_conclusao(self):
        """Testa a marcação de tarefa como concluída"""
        self.tarefa.concluida = True
        self.tarefa.save()
        self.assertTrue(self.tarefa.concluida)
        self.assertEqual(self.tarefa.status, 'concluida')
        self.assertIsNotNone(self.tarefa.concluida_em)


class ViewsTest(TestCase):
    """Testes para as views"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.projeto = Projeto.objects.create(
            nome='Projeto Teste',
            usuario=self.user
        )
        self.tarefa = Tarefa.objects.create(
            titulo='Tarefa Teste',
            usuario=self.user,
            projeto=self.projeto
        )

    def test_login_view(self):
        """Testa a view de login"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tarefas/login.html')

    def test_registro_view(self):
        """Testa a view de registro"""
        response = self.client.get(reverse('registro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tarefas/registro.html')

    def test_dashboard_requer_login(self):
        """Testa se o dashboard requer autenticação"""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)  # Redirect para login

    def test_dashboard_com_login(self):
        """Testa o dashboard com usuário autenticado"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tarefas/dashboard.html')

    def test_lista_tarefas_com_login(self):
        """Testa a listagem de tarefas com usuário autenticado"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('lista_tarefas'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tarefa Teste')

    def test_criar_tarefa(self):
        """Testa a criação de uma nova tarefa"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('criar_tarefa'), {
            'titulo': 'Nova Tarefa',
            'descricao': 'Descrição',
            'prioridade': 'media',
            'status': 'pendente',
        })
        self.assertEqual(Tarefa.objects.filter(titulo='Nova Tarefa').count(), 1)

    def test_lista_projetos_com_login(self):
        """Testa a listagem de projetos com usuário autenticado"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('lista_projetos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Projeto Teste')
