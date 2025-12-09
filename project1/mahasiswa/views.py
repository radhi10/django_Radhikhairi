from django.shortcuts import render
from .forms import MahasiswaForm
from .models import Mahasiswa
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/admin/login/')
def input_mahasiswa(request):
    pesan = ""
    if request.method == 'POST':
        form = MahasiswaForm(request.POST)
        if form.is_valid():
            form.save()
            pesan = "Data berhasil tersimpan"
            return redirect('mahasiswa:input_mahasiswa')
    else:
        form = MahasiswaForm()

    semua_mahasiswa = Mahasiswa.objects.all()
    return render(request, 'mahasiswa/input.html', {'form': form, 'pesan': pesan, 'semua_mahasiswa': semua_mahasiswa})


@login_required(login_url='/admin/login/')
def edit_mahasiswa(request, pk):
    mhs = get_object_or_404(Mahasiswa, pk=pk)
    if request.method == 'POST':
        form = MahasiswaForm(request.POST, instance=mhs)
        if form.is_valid():
            form.save()
            return redirect('mahasiswa:input_mahasiswa')
    else:
        form = MahasiswaForm(instance=mhs)
    return render(request, 'mahasiswa/edit.html', {'form': form, 'mhs': mhs})


@login_required(login_url='/admin/login/')
def delete_mahasiswa(request, pk):
    mhs = get_object_or_404(Mahasiswa, pk=pk)
    # Only allow deletion via POST (form from the list). For GET, redirect back.
    if request.method == 'POST':
        mhs.delete()
    return redirect('mahasiswa:input_mahasiswa')
