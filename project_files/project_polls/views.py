from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá mundo! O projeto funcionou e está de pé através do docker!!!!")
