"""
WSGI config for gerenciador_tarefas project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gerenciador_tarefas.settings')

application = get_wsgi_application()
