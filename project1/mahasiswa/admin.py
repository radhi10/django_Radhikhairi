from django.contrib import admin
from .models import Mahasiswa


@admin.register(Mahasiswa)
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'npm', 'email', 'nohp', 'jurusan')
    search_fields = ('nama', 'npm', 'email')
    list_filter = ('jurusan',)
    ordering = ('-id',)
    list_per_page = 25
