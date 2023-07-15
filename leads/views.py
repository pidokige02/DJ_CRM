from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Lead


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)


def lead_detail(request, pkk):
    lead = Lead.objects.get(id=pkk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)