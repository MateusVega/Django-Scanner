from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ferramentas

def scanning(request):
    return render(request, 'Scanning/index.html', {'ferramentas': ferramentas.objects.all().values()})

@csrf_exempt
def save_qr_data(request):
    if request.method == "POST":
        decodetext = request.POST.get("decodetext", "")
        
        if decodetext:
            ferramenta = ferramentas()
            ferramenta.nome = request.POST.get("decodetext", "")
            ferramenta.status = "off"
            ferramenta.save()
            return JsonResponse({"status": "success", "message": "QR code saved successfully"}) and render(request, 'Scanning/index.html', {'ferramentas': ferramentas.objects.all().values()})
    
    return JsonResponse({"status": "error", "message": "No data provided"})