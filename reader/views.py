from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ferramentas

def scan(request):
    return render(request, 'reader/index.html', {'ferramentas': ferramentas.objects.all().values()})

def add(request):
    return render(request, 'reader/add.html', {'ferramentas': ferramentas.objects.all().values()})

@csrf_exempt
def save_qr_data(request):
    if request.method == "POST":
        decodetext = request.POST.get("decodetext", "")
        
        if decodetext:
            ferramenta = ferramentas()
            ferramenta.nome = request.POST.get("decodetext", "")
            ferramenta.status = "off"
            ferramenta.save()
            return JsonResponse({"status": "success", "message": "QR code saved successfully"})
    
    return JsonResponse({"status": "error", "message": "No data provided"})

@csrf_exempt
def off_to_on(request):
    if request.method == "POST":
        decodetext = request.POST.get("decodetext", "")
        
        if decodetext:
            ferramenta = ferramentas.objects.get(nome=decodetext)
            ferramenta.status = "on"
            ferramenta.save()
            ferramenta_atualizada = ferramentas.objects.get(nome=decodetext)
            print(f"Status atualizado: {ferramenta_atualizada.status}")
            return JsonResponse({"status": "success", "message": "QR code saved successfully"})
    
    return JsonResponse({"status": "error", "message": "No data provided"})