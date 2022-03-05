import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import apps.routing 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channels.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        apps.routing.websocket_urlpatterns
    )
})
