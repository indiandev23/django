from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')
   # return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')

    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        contact= Contact(name=name, email=email, password=password, address=address)
        contact.save()
    return render(request, 'contact.html')