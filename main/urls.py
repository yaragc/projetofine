
# from django.contrib import admin
# from django.urls import path
# from reservas.views import index, cadastrar_reserva,listar_reservas, mais, detalhar, apagar, editar, sobre
# from django.conf.urls.static import static
# from django.conf import settings


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', index,name='index'),
#     path('form/', cadastrar_reserva,name='cadastrar'),
#     path('listar/', listar_reservas,name='listar'),
#     path('mais/',mais, name='mais'),
#     path('detalhe/<int:id>/', detalhar, name='detalhar'),
#     path('editar/<int:id>/', editar, name='editar'),
#     path('apagar/<int:id>/', apagar, name='apagar'),
#     path('sobre_nos/', sobre, name='sobre'),
# ] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path
from reservas.views import Cadastrar, Apagar, Listar, Editar, Index, Sobre, Mais, Detalhar
from stand.views import listastand, CriarStand, Delete, StandUpdateView, StandDetalhe
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(),name='index'),
    path('form/', Cadastrar.as_view(),name='cadastrar'),
    path('listar/', Listar.as_view(),name='listar'),
    path('mais/',Mais.as_view(), name='mais'),
    path('editar/<int:pk>/', Editar.as_view(), name='editar'),
    path('apagar/<int:pk>/',Apagar.as_view(), name='apagar'),
    path('detalhar/<int:pk>/', Detalhar.as_view(), name='detalhar'),
    path('sobre/', Sobre.as_view(), name='sobre'),
    path('listastand/', listastand.as_view(), name ="listastand"),
    path('formstand/', CriarStand.as_view(), name ='formstand'),
    path('updateStand/<int:pk>/', StandUpdateView.as_view(), name ="updateStand"),
    path('apagarstand/<int:pk>/', Delete.as_view(), name ="apagarstand"),
    path('detalharstand/<int:pk>/', StandDetalhe.as_view(), name='detalharstand'),

] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
