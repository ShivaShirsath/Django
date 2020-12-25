from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context={
        "data":"Home"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("<h1 align='center'>Home Page<h1>")

def about(request):
    context={
        "data":"About"
    }
    return render(request, 'about.html', context)
    
def contact(request):
    context={
        "data":"Contact"
    }
    return render(request, 'contact.html', context)
