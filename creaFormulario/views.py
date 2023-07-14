from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import openpyxl
from .models import Formulario

# Create your views here.


def formulario_list(request):
    formularios = Formulario.objects.all()
    print(formularios.count())

    paginator = Paginator(formularios, 10)
    page_number = request.GET.get('page', 1)
    try:
        formulario = paginator.page(page_number)
    except PageNotAnInteger:
        formulario = paginator.page(1)
    except EmptyPage:
        formulario = paginator.page(paginator.num_pages)

    return render(request, 'creaFormulario/index.html', {'formulario': formulario})


def cargaExcel(request):

    def boo(value):
        if value == "Sí":
            return True
        return False

    def dat(value):
        if value == "":
            return None
        return value

    if "GET" == request.method:
        return render(request, 'creaFormulario/cargaExcel.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting all sheets
        # sheets = wb.sheetnames
        # getting a particular sheet
        # worksheet = wb["Sheet1"]
        # getting active sheet
        hoja = wb.active
        # print(hoja)

        # reading a cell

        excel_data = []
        for i in range(2, hoja.max_row+1):
            # Hace split al campo de título, para no crear subcarpetas
            # titulo_e = (hoja.cell(i, 6).value).split("/", 1)
            # Valida valores boleanos para ser ingresados al modelo
            divulgacion_e = boo(hoja.cell(i, 12).value)
            invencion_e = boo(hoja.cell(i, 28).value)
            convenios_e = boo(hoja.cell(i, 30).value)
            mercado_e = boo(hoja.cell(i, 33).value)
            interes_e = boo(hoja.cell(i, 37).value)
            discovery_e = boo(hoja.cell(i, 39).value)
            compromiso_e = boo(hoja.cell(i, 42).value)
            contacto_e = boo(hoja.cell(i, 35).value)

            # Fechas
            fecha_1 = dat(hoja.cell(i, 14))
            fecha_2 = dat(hoja.cell(i, 15))
            fecha_3 = dat(hoja.cell(i, 16))

            formulario = Formulario(email_institucional=hoja.cell(i, 4).value,
                                    # titulo=titulo_e,
                                    titulo=hoja.cell(i, 6).value,
                                    nombre=hoja.cell(i, 5).value,
                                    email=hoja.cell(i, 4).value,
                                    telefono=hoja.cell(i, 9).value,
                                    contacto=hoja.cell(i, 10).value,
                                    email_adicional=hoja.cell(i, 11).value,
                                    divulgacion=divulgacion_e,
                                    divulgacion_info=hoja.cell(i, 13).value,
                                    divulgacion_fecha_1=fecha_1,
                                    divulgacion_fecha_2=fecha_2,
                                    divulgacion_fecha_3=fecha_3,
                                    divulgacion_evidencia=hoja.cell(
                                        i, 17).value,
                                    keywords=hoja.cell(i, 18).value,
                                    area_aplicacion=hoja.cell(i, 19).value,
                                    tipo_invencion=hoja.cell(i, 20).value,
                                    descripcion=hoja.cell(i, 21).value,
                                    problematica=hoja.cell(i, 22).value,
                                    relevantes=hoja.cell(i, 23).value,
                                    ocurrencia=hoja.cell(i, 24).value,
                                    obvia=hoja.cell(i, 25).value,
                                    financiamiento=hoja.cell(i, 26).value,
                                    financiamiento_especifique=hoja.cell(
                                        i, 27).value,
                                    invencion_involucramiento=invencion_e,
                                    involucrameinto=hoja.cell(i, 29).value,
                                    convenios=convenios_e,
                                    convenios_tipo=hoja.cell(i, 31).value,
                                    necesidad=hoja.cell(i, 32).value,
                                    mercado=mercado_e,
                                    mercado_especifique=hoja.cell(i, 34).value,
                                    contacto_empresa=contacto_e,
                                    contacto_especifique=hoja.cell(
                                        i, 36).value,
                                    interes=interes_e,
                                    interes_especifique=hoja.cell(i, 38).value,
                                    discovery=discovery_e,
                                    discovery_especifique=hoja.cell(
                                        i, 40).value,
                                    informacion_tecnica=hoja.cell(i, 41).value,
                                    compromiso=compromiso_e)
            excel_data.append(formulario)
            print(formulario.divulgacion_evidencia)
            # formulario.save()
        # iterating over the rows and
        # getting value from each cell in row
        """for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
                print(cell.value)
            excel_data.append(row_data)"""
        # print(excel_data)

        return render(request, 'creaFormulario/cargaExcel.html', {"excel_data": excel_data})
