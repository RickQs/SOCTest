from django.shortcuts import redirect, render
from app.forms import ExamesForm, FieldFormat
from app.models import Exames
from django.core.paginator import Paginator


def home(request):
    # Criação sem paginação
    search = request.GET.get('search')
    if search:
        data = {'db': Exames.objects.filter(paciente__icontains=search).order_by('paciente','exame'), 'searched': True} # filtra por modelos que contenham a string search, sendo __icontains case insensitive
        # all = Exames.objects.filter(paciente__icontains=search).order_by('paciente','exame')
        # paginator = Paginator(all, 2)
        # pages = request.GET.get('page')
        # data = {'db': paginator.get_page(pages), 'searched': True}
    else:
        # data = {'db': Exames.objects.all().order_by('paciente','exame')}
        all = Exames.objects.all().order_by('paciente','exame')
        paginator = Paginator(all, 5)
        pages = request.GET.get('page')
        data = {'db': paginator.get_page(pages)}

    # Paginação
    # all = Exames.objects.all() # recebe todos os registros do banco
    # paginator = Paginator(all, 2) # recebe os registros e exibe 2 por página
    # pages = request.GET.get('page') # pega via método GET o parâmetro 'page' da nossa URL
    # data = {'db': paginator.get_page(pages)}
    return render(request, 'index.html', data)

def form(request):
    data = {'form': FieldFormat()}
    return render(request, 'form.html', data)

def create(request):
    form = ExamesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {'db': Exames.objects.get(pk=pk)}
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Exames.objects.get(pk=pk) # recebe chave primária
    data['form'] = ExamesForm(instance=data['db']) # instance vai ser de acordo com a pk, pra gerar o formulário
    return render(request, 'form.html', data)

def update(request, pk):
    data = {'db': Exames.objects.get(pk=pk)}
    form = ExamesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Exames.objects.get(pk=pk)
    db.delete()
    return redirect('home')    