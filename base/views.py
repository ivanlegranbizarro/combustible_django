from django.http import HttpResponse


def primera_vista(request):
    return HttpResponse("Hola mundo")
