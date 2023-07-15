from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_page(request):
    # return render(request, "second_page.html")
    return render(request, "leads/home_page.html")