from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"app/index.html")

def resultado(request):
     #recuperar datos de la pagina html
    nombre=request.GET["ddlproducto"]
    pre=float(request.GET["txtprecio"])
    cant=int(request.GET["txtcantidad"])
    #procesar
    tot=pre*cant
    igv=tot*0.18
    total=tot+igv
    contexto={'nombre':nombre,'precio':pre,'cantidad':cant,'impuesto':igv,'total':total}
    return render(request,"app/resultado.html",contexto)
