from django.shortcuts import render, HttpResponse
from datetime import datetime
from app.models import Contact
from django.contrib import messages

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
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        contact = Contact(firstname=firstname, lastname=lastname, email=email, phone=phone, msg=msg, date=datetime.today())
        contact.save()
        messages.success(request, 'Messege sended to admin !')
    return render(request, 'contact.html', context)
