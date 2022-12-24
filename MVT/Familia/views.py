from django.shortcuts import render

from django.http import HttpResponse

import datetime
from Familia.models import familia

def create_family(request):
    new_family = familia.objects.create(name='Juan Perez', age = 20, married=False, birth=datetime.date(2002, 10, 10))
    new_family2 = familia.objects.create(name='Jose Perez', age = 22, married=False, birth=datetime.date(2000, 11, 12))
    new_family3 = familia.objects.create(name='Laura Perez', age = 30, married=True, birth=datetime.date(1992, 10, 20))
    print(new_family)
    print(new_family2)
    print(new_family3)
    return HttpResponse('Se creo el nuevo grupo familiar')


def list_family(request):
    all_family = familia.objects.all()
    print(all_family)
    context={'familia':all_family,}
    return render(request, 'list_family.html', context=context)


def delete_all_rows(request):
    familia.objects.all().delete()
    return HttpResponse('Se borro el grupo familiar')
