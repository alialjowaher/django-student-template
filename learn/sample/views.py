from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>hello to my sample app</h1>")    



