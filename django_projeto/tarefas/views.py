from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db.models import Q, Count
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Tarefa, Projeto, Comentario, Anexo
from .forms import (
    TarefaForm, ProjetoForm, ComentarioForm,
    AnexoForm, RegistroForm, FiltroTarefaForm
)


# Views de Autenticação
def registro_view(request):
    """View para registro de novos usuários"""
    if request.user.is_authenticated:
        return redirect('lista_tarefas')

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.username}! Sua conta foi criada com sucesso.')
            return redirect('lista_tarefas')
    else:
        form = RegistroForm()

    return render(request, 'tarefas/registro.html', {'form': form})


def login_view(request):
    """View para login de usuários"""
    if request.user.is_authenticated:
        return redirect('lista_tarefas')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo de volta, {user.username}!')
            next_url = request.GET.get('next', 'lista_tarefas')
            return redirect(next_url)
        else:
            messages.error(request, 'Usuário ou senha incorretos.')

    return render(request, 'tarefas/login.html')


@login_required
def logout_view(request):
    """View para logout"""
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    return redirect('login')


# Dashboard
@login_required
def dashboard(request):
    """Dashboard principal com estatísticas"""
    usuario = request.user

    # Estatísticas gerais
    total_tarefas = Tarefa.objects.filter(usuario=usuario).count()
    tarefas_concluidas = Tarefa.objects.filter(usuario=usuario, concluida=True).count()
    tarefas_pendentes = Tarefa.objects.filter(usuario=usuario, concluida=False).count()
    total_projetos = Projeto.objects.filter(usuario=usuario).count()

    # Tarefas por prioridade
    tarefas_urgentes = Tarefa.objects.filter(usuario=usuario, prioridade='urgente', concluida=False).count()
    tarefas_alta = Tarefa.objects.filter(usuario=usuario, prioridade='alta', concluida=False).count()

    # Tarefas atrasadas
    from django.utils import timezone
    tarefas_atrasadas = Tarefa.objects.filter(
        usuario=usuario,
        concluida=False,
        data_vencimento__lt=timezone.now().date()
    ).count()

    # Tarefas recentes
    tarefas_recentes = Tarefa.objects.filter(usuario=usuario).order_by('-criado_em')[:5]

    # Projetos com mais tarefas
    projetos = Projeto.objects.filter(usuario=usuario).annotate(
        num_tarefas=Count('tarefas')
    ).order_by('-num_tarefas')[:5]

    context = {
        'total_tarefas': total_tarefas,
        'tarefas_concluidas': tarefas_concluidas,
        'tarefas_pendentes': tarefas_pendentes,
        'total_projetos': total_projetos,
        'tarefas_urgentes': tarefas_urgentes,
        'tarefas_alta': tarefas_alta,
        'tarefas_atrasadas': tarefas_atrasadas,
        'tarefas_recentes': tarefas_recentes,
        'projetos': projetos,
    }

    return render(request, 'tarefas/dashboard.html', context)


# CRUD de Tarefas
@login_required
def lista_tarefas(request):
    """Lista todas as tarefas do usuário com filtros"""
    tarefas = Tarefa.objects.filter(usuario=request.user)

    # Aplicar filtros
    form = FiltroTarefaForm(request.GET, user=request.user)
    if form.is_valid():
        busca = form.cleaned_data.get('busca')
        if busca:
            tarefas = tarefas.filter(
                Q(titulo__icontains=busca) | Q(descricao__icontains=busca)
            )

        prioridade = form.cleaned_data.get('prioridade')
        if prioridade:
            tarefas = tarefas.filter(prioridade=prioridade)

        status = form.cleaned_data.get('status')
        if status:
            tarefas = tarefas.filter(status=status)

        projeto = form.cleaned_data.get('projeto')
        if projeto:
            tarefas = tarefas.filter(projeto=projeto)

    # Ordenação
    ordenacao = request.GET.get('ordem', '-criado_em')
    tarefas = tarefas.order_by(ordenacao)

    context = {
        'tarefas': tarefas,
        'form': form,
    }

    return render(request, 'tarefas/lista_tarefas.html', context)


@login_required
def criar_tarefa(request):
    """Cria uma nova tarefa"""
    if request.method == 'POST':
        form = TarefaForm(request.POST, user=request.user)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            tarefa.save()
            messages.success(request, 'Tarefa criada com sucesso!')
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(user=request.user)

    return render(request, 'tarefas/form_tarefa.html', {'form': form, 'titulo': 'Nova Tarefa'})


@login_required
def editar_tarefa(request, pk):
    """Edita uma tarefa existente"""
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('detalhes_tarefa', pk=tarefa.pk)
    else:
        form = TarefaForm(instance=tarefa, user=request.user)

    return render(request, 'tarefas/form_tarefa.html', {
        'form': form,
        'titulo': 'Editar Tarefa',
        'tarefa': tarefa
    })


@login_required
def detalhes_tarefa(request, pk):
    """Mostra os detalhes de uma tarefa"""
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)
    comentarios = tarefa.comentarios.all()
    anexos = tarefa.anexos.all()

    if request.method == 'POST':
        if 'comentario' in request.POST:
            form_comentario = ComentarioForm(request.POST)
            if form_comentario.is_valid():
                comentario = form_comentario.save(commit=False)
                comentario.tarefa = tarefa
                comentario.usuario = request.user
                comentario.save()
                messages.success(request, 'Comentário adicionado!')
                return redirect('detalhes_tarefa', pk=pk)
        elif 'anexo' in request.POST:
            form_anexo = AnexoForm(request.POST, request.FILES)
            if form_anexo.is_valid():
                anexo = form_anexo.save(commit=False)
                anexo.tarefa = tarefa
                anexo.enviado_por = request.user
                anexo.save()
                messages.success(request, 'Anexo enviado!')
                return redirect('detalhes_tarefa', pk=pk)

    form_comentario = ComentarioForm()
    form_anexo = AnexoForm()

    context = {
        'tarefa': tarefa,
        'comentarios': comentarios,
        'anexos': anexos,
        'form_comentario': form_comentario,
        'form_anexo': form_anexo,
    }

    return render(request, 'tarefas/detalhes_tarefa.html', context)


@login_required
def deletar_tarefa(request, pk):
    """Deleta uma tarefa"""
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)

    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa deletada com sucesso!')
        return redirect('lista_tarefas')

    return render(request, 'tarefas/confirmar_delete.html', {'objeto': tarefa, 'tipo': 'tarefa'})


@login_required
@require_POST
def toggle_tarefa(request, pk):
    """Toggle do status de conclusão da tarefa (AJAX)"""
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)
    tarefa.concluida = not tarefa.concluida
    tarefa.save()

    return JsonResponse({
        'success': True,
        'concluida': tarefa.concluida
    })


# CRUD de Projetos
@login_required
def lista_projetos(request):
    """Lista todos os projetos do usuário"""
    projetos = Projeto.objects.filter(usuario=request.user).annotate(
        num_tarefas=Count('tarefas'),
        tarefas_concluidas_count=Count('tarefas', filter=Q(tarefas__concluida=True))
    )

    return render(request, 'tarefas/lista_projetos.html', {'projetos': projetos})


@login_required
def criar_projeto(request):
    """Cria um novo projeto"""
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.usuario = request.user
            projeto.save()
            messages.success(request, 'Projeto criado com sucesso!')
            return redirect('lista_projetos')
    else:
        form = ProjetoForm()

    return render(request, 'tarefas/form_projeto.html', {'form': form, 'titulo': 'Novo Projeto'})


@login_required
def editar_projeto(request, pk):
    """Edita um projeto existente"""
    projeto = get_object_or_404(Projeto, pk=pk, usuario=request.user)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto atualizado com sucesso!')
            return redirect('lista_projetos')
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'tarefas/form_projeto.html', {
        'form': form,
        'titulo': 'Editar Projeto',
        'projeto': projeto
    })


@login_required
def detalhes_projeto(request, pk):
    """Mostra os detalhes de um projeto"""
    projeto = get_object_or_404(Projeto, pk=pk, usuario=request.user)
    tarefas = projeto.tarefas.all()

    context = {
        'projeto': projeto,
        'tarefas': tarefas,
    }

    return render(request, 'tarefas/detalhes_projeto.html', context)


@login_required
def deletar_projeto(request, pk):
    """Deleta um projeto"""
    projeto = get_object_or_404(Projeto, pk=pk, usuario=request.user)

    if request.method == 'POST':
        projeto.delete()
        messages.success(request, 'Projeto deletado com sucesso!')
        return redirect('lista_projetos')

    return render(request, 'tarefas/confirmar_delete.html', {'objeto': projeto, 'tipo': 'projeto'})
