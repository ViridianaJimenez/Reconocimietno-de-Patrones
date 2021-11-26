from django.shortcuts import render
from .models import Tejido

# Create your views here.

def home(request):
    L=Tejido.objects.get_queryset()  

    #listProcesada = procesaLista(L)

    matrizDat = matrizDist(L)
    diccionario = {'lista':L,'matrizDat':matrizDat,}
    template_name = "home/index.html"
    return render(request, template_name, diccionario)

def procesaLista(lista):
    lista1=[]
    for elemento in lista:
        valor = elemento.temperatura**2 + elemento.inflamacion**2 + elemento.color**2
        res = valor**0.5
        if res > 100:
            lista1.append(res)
    return lista1

def matrizDist(lista):
    tamaño = len(lista)
    matrizVacia = []
    contador = 0
    for i in range(tamaño):
        matrizVacia.append([0]*tamaño)
    for fila in matrizVacia:
        for columna in range(len(fila)):
            valorResultado = 0
            valorResultado = (lista[columna].temperatura - lista[contador].temperatura)**2+(lista[columna].color - lista[contador].color)**2+(lista[columna].inflamacion - lista[contador].inflamacion)**2
            formato = valorResultado**0.5
            matrizVacia[contador][columna] = round(formato,3)
        contador += 1
    return matrizVacia