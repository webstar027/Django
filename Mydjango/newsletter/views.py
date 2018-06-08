from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm
# Create your views here.
def home(request):
    title = "Django for {% request.user %}"
    form = SignUpForm()
    context = {
        "title": title,
        "Signupform": form
    }
    return render(request, "home.html", context)
