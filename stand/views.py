from django.shortcuts import render,get_object_or_404, redirect
from reservas.models import Stand
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from stand.form import StandForm
from django.urls import reverse_lazy
from django.contrib.messages import views


class listastand(ListView):
   
    template_name ='core/listastand.html'
    model = Stand
    context_object_name = 'stand'
    paginate_by = 2

#criar
class CriarStand(views.SuccessMessageMixin,CreateView):

    model = Stand
    form_class = StandForm
    template_name = 'core/formstand.html'
    success_url = reverse_lazy('stand:listastand')
    success_message = "Stand criado com sucesso!"


class Delete(views.SuccessMessageMixin,DeleteView):
    model = Stand
    template_name = 'core/apagarstand.html'
    success_url = reverse_lazy("stand:listastand")
    context_object_name= "stand"
    success_message = "Stand deletado com sucesso!"


class StandUpdateView(views.SuccessMessageMixin,UpdateView):
  model = Stand
  form_class = StandForm
  success_url = reverse_lazy("stand:listastand")
  template_name = "core/formstand.html"
  success_message = "Stand atualizado com sucesso!"


class StandDetalhe(DetailView):
    model = Stand
    template_name = "core/detalharstand.html"
  
