from django.shortcuts import render
from registro_prestadores.models.models import Profesionales

def lista_profesionales(request):
    todos_profesionales = Profesionales.objects.all()  # Recuperamos todos los profesionales
    return render(request, 'lista_profesionales.html', {'profesionales': todos_profesionales})
