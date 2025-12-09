from django.db import models


class Mahasiswa(models.Model):
    nama = models.CharField(max_length=200)
    npm = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    nohp = models.CharField(max_length=20, blank=True)
    jurusan = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Mahasiswa"
        verbose_name_plural = "Mahasiswas"

    def __str__(self):
        return f"{self.nama} ({self.npm})"
