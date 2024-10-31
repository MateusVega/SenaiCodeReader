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
        print("local:", request.POST.get("local"))
        ferramenta = ferramentas()
        ferramenta.numero = request.POST.get("numero")
        ferramenta.nome = request.POST.get("nome")
        ferramenta.local = request.POST.get("local")
        ferramenta.instrutor = request.POST.get("instrutor")
        ferramenta.status = "off"
        ferramenta.save()
        return render(request, 'reader/add.html', {'ferramentas': ferramentas.objects.all().values()})

@csrf_exempt
def off_to_on(request):
    if request.method == "POST":
        decodetext = request.POST.get("decodetext", "")
        if decodetext:
            ferramenta = ferramentas.objects.get(numero=decodetext)
            ferramenta.status = "on"
            ferramenta.save()

def reset(request):
    ferramentas.objects.filter(status="on").update(status="off")
    return render(request, 'reader/index.html', {'ferramentas': ferramentas.objects.all().values()})

@csrf_exempt
def delete_line(request):
    if request.method == 'POST':
        dbline_id = request.POST.get('dbline')
        print(dbline_id)
        ferramentas.objects.filter(id=dbline_id).delete()
        return JsonResponse({'status': 'success', 'deleted_id': dbline_id})