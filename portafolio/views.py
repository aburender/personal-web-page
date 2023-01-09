from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Mensaje
# Create your views here.

class MensajeCreateView(SuccessMessageMixin, CreateView):
    success_url = '/'
    success_message = "Tu mensaje se a enviado exitosamente!"
    model = Mensaje
    template_name = "portafolio/contactame.html"
    fields = ['nombre', 'email', 'mensaje']
    