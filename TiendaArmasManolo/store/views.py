from django.shortcuts import render
from django.http import HttpResponse

def titulo(request):
    return HttpResponse("Bienvenido a Tienda De Armas Manolo") 
def about(request):
    return HttpResponse("D:\Cosas\TrabajoMarcas\AhoraSiProyectoFinalMarcas\AboutUs\SobreNosotros.html")
def AboutUs(request):
    context = {"../AboutUS/SobreNosotros.html"}
