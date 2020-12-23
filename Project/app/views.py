from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1 align='center'>Home Page<h1>")

def about(request):
    return HttpResponse("<h1 align='center'>About<h1>")

def contact(request):
    return HttpResponse("<h1 align='center'>Contact Me<h1>")
