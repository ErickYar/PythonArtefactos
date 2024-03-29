from django.shortcuts import render,redirect
from .models import Producto

# Create your views here.

def menu(request):
    return render(request,"app/menu.html")

def index(request):
    return render(request,"app/index.html")

def create(request):
    # crear objeto producto de la clase producto
    producto=Producto(producto=request.POST["producto"],
                    categoria=request.POST["categoria"],
                    fecha=request.POST["fecha"],
                    precio=request.POST["precio"],
                    stock=request.POST["stock"])
    # grabar producto en la BD
    producto.save()
    return redirect('/')

def read(request):
    productos=Producto.objects.all()
    #modificando el formato de fecha
    for p in productos:
        p.fecha='{:%d-%m-%Y}'.format(p.fecha)

    contexto={'productos':productos}
    
    return render(request,'app/result.html',contexto)


def delete(request,id):
    producto=Producto.objects.get(id=id)
    producto.delete()
    return redirect('/')

def edit(request,id):
    producto=Producto.objects.get(id=id)
    fe=producto.fecha
    producto.fecha='{:%Y-%m-%d}'.format(fe)
    contexto={'producto':producto}
    return render(request,'app/edit.html',contexto)

def update(request,id):
    producto=Producto.objects.get(id=id)
    # actualizar datos
    producto.producto=request.POST["producto"]
    producto.categoria=request.POST["categoria"]
    producto.fecha=request.POST["fecha"]
    producto.precio=request.POST["precio"]
    producto.stock=request.POST["stock"]
    # graba producto actualizado
    producto.save()
    return redirect('/')



