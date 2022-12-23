from django.shortcuts import render
from django.http import HttpResponse
from .models import Ebook

# Create your views here.


def home(request):
    searchTerm = request.GET.get("searchEbook")
    if searchTerm:
        ebooks = Ebook.objects.filter(title__icontains=searchTerm)
    else:
        ebooks = Ebook.objects.all()
    return render(request, "home.html", {"searchTerm": searchTerm, "ebooks": ebooks})


def about(request):
    return HttpResponse("<h1>Welcome to About Page</h1>")


def signup(request):
    email = request.GET.get("email")
    return render(request, "signup.html", {"email": email})
