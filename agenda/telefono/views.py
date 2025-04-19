from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Contacto

def lista_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'lista_contactos.html', {'contactos': contactos})

def agregar_contactos(request):
    if request.method == 'POST':
        nom = request.POST['nombre']
        tel = request.POST['telefono']
        em = request.POST['email']
        Contacto.objects.create(nombre=nom, telefono=tel, email=em)
        return redirect('lista_contactos')
    return render(request, 'agregar_contactos.html')

def editar_contacto(request, id):
    #contacto = Contacto.objects.filter(id=id).first()
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        contacto.nombre = request.POST['nombre']
        contacto.telefono = request.POST['telefono']
        contacto.email = request.POST['email']
        contacto.save()
        return redirect('lista_contactos')
    return render(request, 'editar_contacto.html', {'contacto': contacto})
    
def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'eliminar_contacto.html', {'contacto': contacto})
    



# Create your views here.



def hola_mundo(request):
    html = """
    <h1>Hola Bienvenidos<h1>
    <p>
    CAMINO   A   DEVELOPER   PANAS
    </p>
    """
    
    return HttpResponse(html)
    


