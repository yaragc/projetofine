from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect
from .models import Reserva,Stand
from .forms import ReservaForm,StandForm
from  django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from django.urls import reverse_lazy
from django.contrib.messages import views

class index(TemplateView):
    template_name = "core/index.html"
    
class formstand(TemplateView):
    template_name = "core/formstand.html"
    
class listastand(TemplateView):
    template_name = "core/listastand.html"
    
class Detalhar(DetailView):
    model = Reserva
    template_name = "core/detalhar.html"  
    context_object_name = 'reservas'

class Listar(ListView):
    template_name = "reservas/listar.html"
    model = Reserva
    context_object_name = 'reservas'
    paginate_by = 3


class Cadastrar(views.SuccessMessageMixin, CreateView):
  form_class = ReservaForm
  template_name = "reservas/form.html"
  success_url = reverse_lazy("listar")
  success_message = "Reserva cadastrada com sucesso!"
  
class Apagar(views.SuccessMessageMixin, DeleteView):
  model = Reserva
  template_name = "reservas/apagar.html"
  success_url = reverse_lazy("listar")
  success_message = "Reserva removida com sucesso!"
  
class Editar(views.SuccessMessageMixin, UpdateView):
  model = Reserva
  form_class = ReservaForm
  template_name = "reservas/form.html"
  success_url = reverse_lazy("listar")
  success_message = "Reserva atualizada com sucesso!" 
  
