from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Projeto(models.Model):
    """Model para organizar tarefas em projetos"""
    nome = models.CharField(max_length=200, verbose_name='Nome do Projeto')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projetos')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cor = models.CharField(max_length=7, default='#3498db', help_text='Cor em hexadecimal')

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-criado_em']

    def __str__(self):
        return self.nome

    def total_tarefas(self):
        return self.tarefas.count()

    def tarefas_concluidas(self):
        return self.tarefas.filter(concluida=True).count()

    def tarefas_pendentes(self):
        return self.tarefas.filter(concluida=False).count()


class Tarefa(models.Model):
    """Model principal para gerenciar tarefas"""

    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ]

    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
        ('cancelada', 'Cancelada'),
    ]

    titulo = models.CharField(max_length=200, verbose_name='Título')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADE_CHOICES,
        default='media',
        verbose_name='Prioridade'
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='pendente',
        verbose_name='Status'
    )
    concluida = models.BooleanField(default=False, verbose_name='Concluída')
    data_vencimento = models.DateField(null=True, blank=True, verbose_name='Data de Vencimento')
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name='tarefas',
        null=True,
        blank=True,
        verbose_name='Projeto'
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tarefas',
        verbose_name='Usuário'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    concluida_em = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        # Atualizar data de conclusão automaticamente
        if self.concluida and not self.concluida_em:
            self.concluida_em = timezone.now()
        elif not self.concluida:
            self.concluida_em = None

        # Sincronizar status com concluída
        if self.concluida:
            self.status = 'concluida'

        super().save(*args, **kwargs)

    def esta_atrasada(self):
        """Verifica se a tarefa está atrasada"""
        if self.data_vencimento and not self.concluida:
            return timezone.now().date() > self.data_vencimento
        return False

    def dias_para_vencimento(self):
        """Retorna quantos dias faltam para o vencimento"""
        if self.data_vencimento and not self.concluida:
            delta = self.data_vencimento - timezone.now().date()
            return delta.days
        return None


class Comentario(models.Model):
    """Model para comentários nas tarefas"""
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField(verbose_name='Comentário')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        ordering = ['criado_em']

    def __str__(self):
        return f'Comentário de {self.usuario.username} em {self.tarefa.titulo}'


class Anexo(models.Model):
    """Model para anexos nas tarefas"""
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE, related_name='anexos')
    arquivo = models.FileField(upload_to='anexos/%Y/%m/%d/', verbose_name='Arquivo')
    nome = models.CharField(max_length=255, verbose_name='Nome do Arquivo')
    enviado_em = models.DateTimeField(auto_now_add=True)
    enviado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Anexo'
        verbose_name_plural = 'Anexos'
        ordering = ['-enviado_em']

    def __str__(self):
        return self.nome
