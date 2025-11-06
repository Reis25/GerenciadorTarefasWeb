from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tarefa, Projeto, Comentario, Anexo


class TarefaForm(forms.ModelForm):
    """Formulário para criar e editar tarefas"""

    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'prioridade', 'status', 'data_vencimento', 'projeto', 'concluida']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título da tarefa'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descrição detalhada da tarefa (opcional)'
            }),
            'prioridade': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'data_vencimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'projeto': forms.Select(attrs={'class': 'form-control'}),
            'concluida': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['projeto'].queryset = Projeto.objects.filter(usuario=user)
            self.fields['projeto'].required = False


class ProjetoForm(forms.ModelForm):
    """Formulário para criar e editar projetos"""

    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'cor']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do projeto'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descrição do projeto (opcional)'
            }),
            'cor': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'color'
            }),
        }


class ComentarioForm(forms.ModelForm):
    """Formulário para adicionar comentários"""

    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Adicione um comentário...'
            }),
        }


class AnexoForm(forms.ModelForm):
    """Formulário para upload de anexos"""

    class Meta:
        model = Anexo
        fields = ['arquivo', 'nome']
        widgets = {
            'arquivo': forms.FileInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do arquivo'
            }),
        }


class RegistroForm(UserCreationForm):
    """Formulário de registro de usuário"""
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class FiltroTarefaForm(forms.Form):
    """Formulário para filtrar tarefas"""
    busca = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar tarefas...'
        })
    )
    prioridade = forms.ChoiceField(
        required=False,
        choices=[('', 'Todas as prioridades')] + list(Tarefa.PRIORIDADE_CHOICES),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    status = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos os status')] + list(Tarefa.STATUS_CHOICES),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    projeto = forms.ModelChoiceField(
        required=False,
        queryset=Projeto.objects.none(),
        empty_label='Todos os projetos',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['projeto'].queryset = Projeto.objects.filter(usuario=user)
