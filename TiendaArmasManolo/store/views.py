from django.shortcuts import render
from django.http import HttpResponse

def titulo(request):
    return HttpResponse("Bienvenido a Tienda De Armas Manolo") 
