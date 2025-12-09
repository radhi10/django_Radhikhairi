from django.urls import path
from . import views

app_name = 'AppMahasiswa'

urlpatterns = [
    path('', views.index, name='index'),
]
