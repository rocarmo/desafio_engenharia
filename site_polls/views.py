from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from site_polls.models import DataReturn
from site_polls.api.data_serializer import DataSerializer


def index(request):
    return HttpResponse("SISTEMA ESTÁ FUNCIONANDO!!!")


def get_data(request):
    if request.method == 'GET':
        send_data = DataReturn.objects.all()
        serializer = DataSerializer(send_data)
        return JsonResponse(serializer.data, safe=False)
    else:
        pass

# Create your views here.
