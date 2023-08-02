from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.templatetags.static import static
from django.urls import reverse
from docx import Document
import openpyxl
from .models import Registro, Requisito, Titulo


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
    pass


def detalleRegistro(request, slug):
    registro = get_object_or_404(Registro, slug=slug)
    return render(request, 'registros/detalle.html', {'registro': registro})
