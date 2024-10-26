from django.http import HttpResponse
from django.template import loader

def scanning(request):
    template = loader.get_template('Scanning/index.html')
    return HttpResponse(template.render())