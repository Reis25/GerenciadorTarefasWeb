# Guia Rápido - Gerenciador de Tarefas Django

## Instalação Rápida

### 1. Instalar Python e pip

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Verificar instalação
python3 --version
pip3 --version
```

### 2. Configurar o Projeto

```bash
# Ir para o diretório do projeto
cd django_projeto

# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt
```

### 3. Configurar o Banco de Dados

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser
# Preencha: usuário, email, senha
```

### 4. Executar o Servidor

```bash
# Iniciar servidor de desenvolvimento
python manage.py runserver

# O servidor estará disponível em:
# http://localhost:8000/
```

### 5. Acessar o Sistema

- **Login**: http://localhost:8000/
- **Registro**: http://localhost:8000/registro/
- **Admin**: http://localhost:8000/admin/

## Primeiro Uso

1. Acesse http://localhost:8000/registro/
2. Crie sua conta de usuário
3. Faça login
4. Você será redirecionado para o Dashboard
5. Comece criando seu primeiro projeto ou tarefa!

## Comandos Úteis

```bash
# Executar servidor
python manage.py runserver

# Criar superusuário
python manage.py createsuperuser

# Aplicar migrações
python manage.py migrate

# Shell interativo
python manage.py shell
```

## Solução de Problemas

### Erro: "No module named django"
```bash
# Ative o ambiente virtual
source venv/bin/activate
pip install -r requirements.txt
```

### Erro: "Table doesn't exist"
```bash
# Execute as migrações
python manage.py migrate
```

### Porta 8000 em uso
```bash
# Use outra porta
python manage.py runserver 8080
```

## Recursos do Sistema

- ✅ CRUD completo de Tarefas
- ✅ Gerenciamento de Projetos
- ✅ Sistema de prioridades e status
- ✅ Comentários nas tarefas
- ✅ Upload de anexos
- ✅ Dashboard com estatísticas
- ✅ Filtros e busca
- ✅ Interface moderna e responsiva

## Próximos Passos

1. Explore o Dashboard
2. Crie alguns projetos
3. Adicione tarefas aos projetos
4. Experimente os filtros
5. Adicione comentários e anexos
6. Acesse o painel admin para gerenciamento avançado

---

Para documentação completa, consulte: **README_DJANGO.md**
