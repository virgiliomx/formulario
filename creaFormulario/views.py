from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Formulario

# Create your views here.


def formulario_list(request):
    formularios = Formulario.objects.all()

    paginator = Paginator(formularios, 10)
    page_number = request.GET('page', 1)
    try:
        formulario = paginator.page(page_number)
    except PageNotAnInteger:
        formulario = paginator.page(1)
    except EmptyPage:
        formulario = paginator.page(paginator.num_pages)
    return render(request, 'creaFormulario/index.html', {'formulario': formulario})
