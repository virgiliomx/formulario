from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.templatetags.static import static
from django.urls import reverse
from .models import Registro, Requisito, Titulo
from .forms import RegistroForm, RequisitoForm, ContestacionForm, TituloForm
from inventores.views import Inventor


def listaRegistros(request):
    registros = Registro.objects.all()
    paginator = Paginator(registros, 20)
    page_number = request.GET.get('page', 1)
    try:
        registros = paginator.page(page_number)
    except PageNotAnInteger:
        registros = paginator.page(1)
    except EmptyPage:
        registros = paginator.page(paginator.num_pages)
    return render(request, 'registros/index.html', {'registros': registros})


def nuevoRegistro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            if '/a/' in registro.folio:
                registro.figura = 'Patente'
            elif '/u/' in registro.folio:
                registro.figura = 'Modelo de Utilidad'
            elif '/f/' in registro.folio:
                registro.figura = 'Diseño Industrial'
            registro.save()
            return redirect("registros:listaRegistros")
    else:
        form = RegistroForm()
    return render(request, 'registros/nuevo.html', {'form': form})


def nuevoRequisito(request, slug, ultimo):
    registro = get_object_or_404(Registro, slug=slug)
    if request.method == 'POST':
        form = RequisitoForm(request.POST, ultimo=ultimo)
        if form.is_valid():
            requisito = form.save(commit=False)
            requisito.registro = registro
            requisito.save()
            return redirect("registros:detalleRegistro",  registro.slug)
    else:
        form = RequisitoForm(ultimo=ultimo)

    return render(request, 'registros/requisito.html', {'registro': registro, 'form': form})


def detalleRegistro(request, slug):
    forma = False
    registro = get_object_or_404(Registro, slug=slug)
    requisitos = Requisito.objects.filter(registro=registro)
    ultimo = requisitos.last()
    inventores = Inventor.objects.filter(registros=registro)
    for requisito in requisitos:
        if requisito.tipo == "FORMAS":
            forma = True
    return render(request, 'registros/detalle.html', {'registro': registro, 'requisitos': requisitos, 'forma': forma, 'ultimo': ultimo, 'inventores': inventores})


def borraRegistro(request, slug):
    registro = get_object_or_404(Registro, slug=slug)
    registro.delete()
    return HttpResponseRedirect(reverse('registros:listaRegistros'))


def nuevaContestacion(request, requisito_id):
    requisito = get_object_or_404(Requisito, pk=requisito_id)
    registro = get_object_or_404(Registro, requisito=requisito)
    print(registro.slug)
    if request.method == 'POST':
        form = ContestacionForm(request.POST)
        if form.is_valid():
            contestacion = form.save(commit=False)
            contestacion.requisito = requisito
            contestacion.save()
            return redirect('registros:detalleRegistro', registro.slug)
    else:
        form = ContestacionForm()
    return render(request, 'registros/contestacion.html', {'registro': registro, 'form': form, 'requisito': requisito})


def nuevoTitulo(request, slug):
    registro = get_object_or_404(Registro, slug=slug)
    if request.method == 'POST':
        form = TituloForm(request.POST)
        if form.is_valid():
            titulo = form.save(commit=False)
            titulo.registro = registro
            titulo.save()
            return redirect('registros:detalleRegistro', registro.slug)
    else:
        form = TituloForm()
    return render(request, 'registros/titulo.html', {'registro': registro, 'form': form})
