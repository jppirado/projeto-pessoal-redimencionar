
from .models import tratarImagem
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy 
from django.contrib import messages

from django.views.generic import TemplateView
from PIL import Image


# Create your views here.

class IndexView(CreateView):
    
    model = tratarImagem
    template_name = 'home.html'
    fields = ['imagem' ,'x' , 'y' , ]
    success_url = reverse_lazy('successurl')


class SuccessPageView( TemplateView ):
    template_name = 'success_page.html'


