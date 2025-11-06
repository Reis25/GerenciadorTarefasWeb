# GerenciadorTarefasWeb

Gerenciador de tarefas para pequenos projetos. As atividades terão um CRUD completo para serem gerenciadas.

## Implementações Disponíveis

### 🐍 Django (Recomendado)

Sistema completo de gerenciamento de tarefas desenvolvido com Django framework.

**Recursos:**
- ✅ CRUD completo de Tarefas e Projetos
- ✅ Sistema de autenticação (Login/Registro)
- ✅ Dashboard com estatísticas
- ✅ Prioridades e status de tarefas
- ✅ Comentários e anexos
- ✅ Filtros e busca avançada
- ✅ Interface moderna e responsiva (Bootstrap 5)
- ✅ Painel administrativo

**Documentação:**
- [Documentação Completa](django_projeto/README_DJANGO.md)
- [Guia Rápido](django_projeto/QUICKSTART.md)

**Início Rápido:**
```bash
cd django_projeto
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse: http://localhost:8000/

---

### 🐘 PHP (Documentação)

Documentação e exemplos de PHP com LAMP stack.

**Localização:** `PHP/`

**Instruções:**
- [Instalação LAMP no Ubuntu](PHP/Instrucoes.md)

---

## Tecnologias

### Django
- Python 3.8+
- Django 5.0.1
- SQLite/PostgreSQL/MySQL
- Bootstrap 5
- jQuery

### PHP
- PHP 7.4+
- MySQL
- Apache
- HTML/CSS

## Licença

Veja o arquivo [LICENSE](LICENSE) para mais detalhes. 
