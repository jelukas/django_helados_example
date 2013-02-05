# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from .models import Helado

def listar_helados(request):
    helados = Helado.objects.all()
    return render_to_response('gestor/listar_helados.html',{'helados': helados},context_instance=RequestContext(request))