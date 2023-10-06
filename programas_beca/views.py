from django.shortcuts import render

def registrar_programa_beca(request):
    if request.method == 'POST':
        # Procesar el formulario y guardar el programa de beca en la base de datos
        # Aquí deberías agregar la lógica para guardar el programa de beca en tu base de datos
        return render(request, 'programas_beca/registrar_programa_beca.html', {'success_message': 'Programa de Beca registrado exitosamente.'})

    return render(request, 'programas_beca/registrar_programa_beca.html')
