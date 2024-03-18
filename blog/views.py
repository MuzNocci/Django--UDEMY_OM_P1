from django.shortcuts import render
from django.http import HttpResponse


def blog(request):
    
    return HttpResponse('Blog.')


def exemplo(resquest):

    return HttpResponse('Exemplo do blog.')