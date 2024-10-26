from django.http import HttpResponse
from django.shortcuts import render
from .models import ferramentas

def scanning(request):
    return render(request, 'Scanning/index.html', {'ferramentas': ferramentas.objects.all().values()})