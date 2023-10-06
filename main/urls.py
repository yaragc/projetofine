from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('stand/', include ('stand.urls', namespace='stand')),
    path('', include ('reservas.urls', namespace='reservas'))
] 