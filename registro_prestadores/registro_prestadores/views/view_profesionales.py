from django.shortcuts import render
from itertools import cycle
from registro_prestadores.models.models import Profesionales, Antecedentes

def validar_rut(rut, dv):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    mod = (-s) % 11
    if mod == 10:
        return 'K'
    elif mod == 11:
        return '0'
    else:
        return str(mod)

def detalle_profesional(request):
    rut_dv = request.GET.get('rut', '').strip()
    context = {}

    if not rut_dv:
        context['error'] = 'Por favor ingrese un RUT.'
        return render(request, 'index.html', context)

    parts = rut_dv.split('-')
    if len(parts) == 2:
        rut, dv = parts
        try:
            rut = int(rut)  # Intenta convertir el RUT a entero
            dv_calculado = validar_rut(rut, dv)
            if dv.upper() == dv_calculado:
                try:
                    profesional = Profesionales.objects.get(Rut=rut, Dv=dv)
                    antecedentes = Antecedentes.objects.filter(IdProfesional=profesional.IdProfesional)
                    context['profesional'] = profesional
                    context['antecedentes'] = antecedentes
                    return render(request, 'detalle_profesional.html', context)
                except Profesionales.DoesNotExist:
                    context['error'] = 'No se encontró al profesional.'
            else:
                context['error'] = 'RUT inválido.'
        except ValueError:
            context['error'] = 'RUT inválido.'
    else:
        context['error'] = 'RUT inválido.'

    return render(request, 'index.html', context)