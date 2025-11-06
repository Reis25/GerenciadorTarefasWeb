from django.contrib import admin
from .models import Projeto, Tarefa, Comentario, Anexo


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'usuario', 'total_tarefas', 'tarefas_concluidas', 'criado_em']
    list_filter = ['criado_em', 'usuario']
    search_fields = ['nome', 'descricao']
    date_hierarchy = 'criado_em'


class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 1


class AnexoInline(admin.TabularInline):
    model = Anexo
    extra = 1


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'projeto', 'prioridade', 'status', 'concluida', 'data_vencimento', 'usuario', 'criado_em']
    list_filter = ['prioridade', 'status', 'concluida', 'criado_em', 'data_vencimento']
    search_fields = ['titulo', 'descricao']
    date_hierarchy = 'criado_em'
    inlines = [ComentarioInline, AnexoInline]

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'descricao', 'projeto', 'usuario')
        }),
        ('Status e Prioridade', {
            'fields': ('status', 'prioridade', 'concluida')
        }),
        ('Datas', {
            'fields': ('data_vencimento', 'concluida_em')
        }),
    )


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['tarefa', 'usuario', 'texto', 'criado_em']
    list_filter = ['criado_em']
    search_fields = ['texto']


@admin.register(Anexo)
class AnexoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tarefa', 'enviado_por', 'enviado_em']
    list_filter = ['enviado_em']
    search_fields = ['nome']
