from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the news index.")

def index123(request):
    return HttpResponse("Hello, world. You're at the news index.12312312312")