"""
ASGI config for gerenciador_tarefas project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gerenciador_tarefas.settings')

application = get_asgi_application()
