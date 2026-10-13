from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from django.contrib import messages
from .models import Paciente
from .forms import PacienteForm

def index(request):
    busca = request.GET.get('busca', '').strip()
    
    if busca:
        pacientes = Paciente.objects.filter(nome__icontains=busca)
    else:
        pacientes = Paciente.objects.all()

    # Cálculo das estatísticas via ORM
    total_pacientes = Paciente.objects.count()
    
    if total_pacientes > 0:
        idade_media_dict = Paciente.objects.aggregate(Avg('idade'))
        idade_media = round(idade_media_dict['idade__avg'], 1)
        
        # Identificação dos pacientes mais novo e mais velho
        paciente_mais_novo = Paciente.objects.order_by('idade').first()
        paciente_mais_velho = Paciente.objects.order_by('-idade').first()
    else:
        idade_media = 0
        paciente_mais_novo = None
        paciente_mais_velho = None

    form = PacienteForm()

    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente cadastrado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao cadastrar paciente. Verifique os dados informados.')

    context = {
        'pacientes': pacientes,
        'total_pacientes': total_pacientes,
        'idade_media': idade_media,
        'paciente_mais_novo': paciente_mais_novo,
        'paciente_mais_velho': paciente_mais_velho,
        'busca': busca,
        'form': form,
    }
    
    return render(request, 'pacientes/index.html', context)

def deletar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        messages.success(request, 'Paciente removido com sucesso!')
    return redirect('index')