from django.urls import path
from reservas.views import Cadastrar, Apagar, Listar, Editar, Index, Sobre, Mais, Detalhar
from django.conf.urls.static import static
from django.conf import settings

app_name= "reservas"

urlpatterns = [
    path('', Index.as_view(),name='index'),
    path('form/', Cadastrar.as_view(),name='cadastrar'),
    path('listar/', Listar.as_view(),name='listar'),
    path('mais/',Mais.as_view(), name='mais'),
    path('editar/<int:pk>/', Editar.as_view(), name='editar'),
    path('apagar/<int:pk>/',Apagar.as_view(), name='apagar'),
    path('detalhar/<int:pk>/', Detalhar.as_view(), name='detalhar'),
    path('sobre/', Sobre.as_view(), name='sobre'),

] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
