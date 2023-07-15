from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Lead


def home_page(request):
    leads = Lead.objects.all()
    context = {
        "name" : "joe",
        "age"  : 35,
        "leads": leads
    }
    return render(request, "second_page.html", context)