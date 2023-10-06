from django.urls import path
from stand.views import listastand, CriarStand, Delete, StandUpdateView, StandDetalhe

app_name= "stand"

urlpatterns = [
    path('listastand/', listastand.as_view(), name ="listastand"),
    path('formstand/', CriarStand.as_view(), name ='formstand'),
    path('updateStand/<int:pk>/', StandUpdateView.as_view(), name ="updateStand"),
    path('apagarstand/<int:pk>/', Delete.as_view(), name ="apagarstand"),
    path('detalharstand/<int:pk>/', StandDetalhe.as_view(), name='detalharstand'),

]
