from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Ebook, Review
from .forms import ReviewForm

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


def detail(request, ebook_id):
    ebook = get_object_or_404(Ebook, pk=ebook_id)
    return render(request, "detail.html", {"ebook": ebook})


def createreview(request, ebook_id):
    ebook = get_object_or_404(Ebook, pk=ebook_id)
    if request.method == "GET":
        return render(
            request, "createreview.html", {"form": ReviewForm(), "ebook": ebook}
        )
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.ebook = ebook
            newReview.save()
            return redirect("detail", newReview.ebook.id)
        except ValueError:
            return render(
                request,
                "createreview.html",
                {"form": ReviewForm(), "error": "bad data passed in"},
            )
