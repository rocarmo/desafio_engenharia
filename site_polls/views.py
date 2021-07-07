from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from site_polls.api.data_collect import DataImport
from site_polls.models import DataReturn
from site_polls.api.data_serializer import DataSerializer


def index(request):
    return HttpResponse("SISTEMA ESTÁ FUNCIONANDO!!!")


def get_data(request):
    if request.method == 'GET':
        data_collect = DataImport
        serializer = DataSerializer(data_collect)
        return JsonResponse(serializer.data, safe=False)

    else:
        return HttpResponse("NÃO CAIU NO GET")
