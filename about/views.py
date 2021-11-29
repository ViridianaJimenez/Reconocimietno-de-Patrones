from django.http import request
from django.shortcuts import render
from home import views
from home.models import Tejido

# Create your views here.
def about(request):
    L=Tejido.objects.get_queryset()
    mat = views.matrizDist(L)
    grafo=[]
    
    if request.method == "POST":
        grafo = procesaGrafo(mat,int(request.POST['valorUmbral']))


    template_name="about/about.html"
    return render(request,template_name,{"mat":mat,"grafo":grafo})

def procesaGrafo(matriz, umbral):
    grafo=[]
    comparadorDos = 1

    for lista in matriz:
        comparador = 1
        for valor in lista:

            if comparadorDos < comparador or comparadorDos==comparador:
                if valor > umbral:
                    grafo.append([str(comparadorDos)+"-"+str(comparador), 1])
                else:
                    grafo.append([str(comparadorDos)+"-"+str(comparador), 0])

            comparador += 1
        comparadorDos += 1

    return grafo