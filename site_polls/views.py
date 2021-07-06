from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from site_polls.api.data_collect import DataCollect
from site_polls.models import DataReturn
from site_polls.api.data_serializer import DataSerializer


def index(request):
    return HttpResponse("SISTEMA ESTÁ FUNCIONANDO!!!")


def get_data(request):
    if request.method == 'GET':
        # send_data = DataReturn.objects.all()
        data_collect = DataCollect(text1='FOI CARAI', text2='DISGRAÇAAAAAA')
        serializer = DataSerializer(data_collect)
        return JsonResponse(serializer.data, safe=False)
        # return JSONRenderer().render(serializer.data)
        # return HttpResponse(serializer.data)

    else:
        return HttpResponse("NÃO CAIU NO GET")
