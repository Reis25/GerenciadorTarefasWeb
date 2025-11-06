# Gerenciador de Tarefas - Django

Sistema completo de gerenciamento de tarefas desenvolvido com Django, incluindo CRUD completo, sistema de autenticação, projetos, comentários e anexos.

## Recursos

### Funcionalidades Principais

- **Autenticação de Usuários**
  - Registro de novos usuários
  - Login/Logout
  - Área restrita por usuário

- **Gerenciamento de Tarefas (CRUD Completo)**
  - Criar, listar, editar e deletar tarefas
  - Definir prioridades (Baixa, Média, Alta, Urgente)
  - Definir status (Pendente, Em Andamento, Concluída, Cancelada)
  - Data de vencimento
  - Marcar como concluída
  - Sistema de filtros e busca

- **Gerenciamento de Projetos**
  - Criar e organizar projetos
  - Agrupar tarefas por projeto
  - Acompanhamento de progresso
  - Cores personalizadas para projetos

- **Recursos Adicionais**
  - Sistema de comentários nas tarefas
  - Upload de anexos
  - Dashboard com estatísticas
  - Alertas de tarefas atrasadas
  - Interface responsiva e moderna
  - Design com Bootstrap 5

## Tecnologias Utilizadas

- **Backend**: Django 5.0.1
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript/jQuery
- **Banco de Dados**: SQLite (padrão, pode ser alterado)
- **Ícones**: Font Awesome 6
- **Python**: 3.8+

## Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- virtualenv (recomendado)

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/GerenciadorTarefasWeb.git
cd GerenciadorTarefasWeb/django_projeto
```

2. **Crie um ambiente virtual**
```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute as migrações**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crie um superusuário (admin)**
```bash
python manage.py createsuperuser
```

Siga as instruções para criar o usuário administrador.

6. **Colete os arquivos estáticos**
```bash
python manage.py collectstatic --noinput
```

7. **Execute o servidor de desenvolvimento**
```bash
python manage.py runserver
```

8. **Acesse o sistema**

Abra seu navegador e acesse:
- **Aplicação**: http://localhost:8000/
- **Painel Admin**: http://localhost:8000/admin/

## Estrutura do Projeto

```
django_projeto/
├── gerenciador_tarefas/        # Configurações do projeto
│   ├── __init__.py
│   ├── settings.py             # Configurações principais
│   ├── urls.py                 # URLs principais
│   ├── wsgi.py                 # WSGI config
│   └── asgi.py                 # ASGI config
├── tarefas/                    # App principal
│   ├── migrations/             # Migrações do banco
│   ├── templates/              # Templates HTML
│   │   └── tarefas/
│   │       ├── base.html       # Template base
│   │       ├── dashboard.html  # Dashboard
│   │       ├── login.html      # Login
│   │       ├── registro.html   # Registro
│   │       ├── lista_tarefas.html
│   │       ├── detalhes_tarefa.html
│   │       ├── form_tarefa.html
│   │       ├── lista_projetos.html
│   │       ├── detalhes_projeto.html
│   │       ├── form_projeto.html
│   │       └── confirmar_delete.html
│   ├── __init__.py
│   ├── admin.py                # Configuração do admin
│   ├── apps.py                 # Configuração do app
│   ├── models.py               # Modelos de dados
│   ├── views.py                # Views (lógica)
│   ├── urls.py                 # URLs do app
│   └── forms.py                # Formulários
├── manage.py                   # Script de gerenciamento
├── requirements.txt            # Dependências
└── README_DJANGO.md           # Esta documentação
```

## Modelos de Dados

### Projeto
- Nome
- Descrição
- Usuário (FK)
- Cor
- Timestamps

### Tarefa
- Título
- Descrição
- Prioridade (Baixa/Média/Alta/Urgente)
- Status (Pendente/Em Andamento/Concluída/Cancelada)
- Data de vencimento
- Projeto (FK, opcional)
- Usuário (FK)
- Concluída (boolean)
- Timestamps

### Comentário
- Tarefa (FK)
- Usuário (FK)
- Texto
- Data

### Anexo
- Tarefa (FK)
- Arquivo
- Nome
- Enviado por (FK)
- Data

## URLs Principais

- `/` - Login
- `/registro/` - Registro de usuário
- `/dashboard/` - Dashboard principal
- `/tarefas/` - Lista de tarefas
- `/tarefas/nova/` - Criar tarefa
- `/tarefas/<id>/` - Detalhes da tarefa
- `/tarefas/<id>/editar/` - Editar tarefa
- `/tarefas/<id>/deletar/` - Deletar tarefa
- `/projetos/` - Lista de projetos
- `/projetos/novo/` - Criar projeto
- `/projetos/<id>/` - Detalhes do projeto
- `/admin/` - Painel administrativo

## Uso

### Criar uma Tarefa

1. Faça login no sistema
2. Clique em "Nova Tarefa" no dashboard ou na lista de tarefas
3. Preencha os campos:
   - Título (obrigatório)
   - Descrição (opcional)
   - Prioridade
   - Status
   - Data de vencimento (opcional)
   - Projeto (opcional)
4. Clique em "Salvar"

### Criar um Projeto

1. Acesse "Projetos" no menu lateral
2. Clique em "Novo Projeto"
3. Preencha:
   - Nome do projeto
   - Descrição
   - Cor (escolha uma cor para identificação visual)
4. Clique em "Salvar"

### Filtrar Tarefas

Na lista de tarefas, você pode filtrar por:
- Busca por texto
- Prioridade
- Status
- Projeto

### Adicionar Comentários

1. Acesse os detalhes de uma tarefa
2. Role até a seção de comentários
3. Digite seu comentário
4. Clique em "Adicionar Comentário"

## Painel Administrativo

O Django Admin oferece uma interface poderosa para gerenciar:
- Usuários
- Tarefas
- Projetos
- Comentários
- Anexos

Acesse: http://localhost:8000/admin/

## Personalização

### Alterar o Banco de Dados

Por padrão, o projeto usa SQLite. Para usar MySQL ou PostgreSQL:

1. Instale o driver apropriado:
```bash
# PostgreSQL
pip install psycopg2-binary

# MySQL
pip install mysqlclient
```

2. Edite `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # ou mysql
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '5432',  # 3306 para MySQL
    }
}
```

### Alterar a Secret Key

Para produção, altere a `SECRET_KEY` em `settings.py`:

```python
SECRET_KEY = 'sua-chave-secreta-super-segura'
```

### Configurar para Produção

1. Desative o DEBUG:
```python
DEBUG = False
```

2. Configure os ALLOWED_HOSTS:
```python
ALLOWED_HOSTS = ['seudominio.com', 'www.seudominio.com']
```

3. Configure arquivos estáticos e de mídia
4. Use um servidor WSGI como Gunicorn
5. Configure um servidor web (Nginx/Apache)

## Comandos Úteis

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Executar servidor
python manage.py runserver

# Coletar arquivos estáticos
python manage.py collectstatic

# Shell interativo do Django
python manage.py shell

# Resetar banco de dados (CUIDADO!)
python manage.py flush
```

## Segurança

- Senhas são hasheadas com PBKDF2
- Proteção CSRF habilitada
- XSS protection
- Validação de formulários
- Autenticação baseada em sessão

## Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença especificada no arquivo LICENSE.

## Suporte

Para dúvidas ou problemas:
- Abra uma issue no GitHub
- Entre em contato através do e-mail do desenvolvedor

## Autor

Desenvolvido como sistema de gerenciamento de tarefas completo com Django.

---

**Versão**: 1.0.0
**Data**: 2025
**Framework**: Django 5.0.1
