from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("SISTEMA ESTÁ FUNCIONANDO!!!")
# Create your views here.
