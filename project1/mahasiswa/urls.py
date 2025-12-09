from django.urls import path
from . import views

app_name = 'mahasiswa'

urlpatterns = [
    path('input/', views.input_mahasiswa, name='input_mahasiswa'),
    path('edit/<int:pk>/', views.edit_mahasiswa, name='edit_mahasiswa'),
    path('delete/<int:pk>/', views.delete_mahasiswa, name='delete_mahasiswa'),
]
