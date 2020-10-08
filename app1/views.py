from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def first_func(self):
    output = "<h1>Hello first App</h1> <a href = '/second'>Second Page</a>"
    return HttpResponse(output)

def second_func(self):
    return HttpResponse("<h1>Hello first App second page</h1> <a href = '/'>Main Page</a>")