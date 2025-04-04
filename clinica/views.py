from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico
from .forms import MedicoForm

def lista_de_medicos(request, pk):
    Medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instace=medico)
        if form.is_valid():
            form.save()
            return redirect('lista_de_medicos')
    else:
          form = MedicoForm()
    return render(request, 'Medico/criar_consulta.html', {'form': form})


def criar_consulta(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_de_medicos')
    else:
        form = MedicoForm()
    return render(request, 'Medico/criar_consulta.html', {'form': form})




# Create your views here.
