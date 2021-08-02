from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
from .forms import LeadForm

def lead_list(request):
    #return HttpResponse('home.html')
    leads = Lead.objects.all()
    context = {"leads":leads}
    return render(request, 'lead_list.html', context)

def lead_detail(request, pk):
    print(pk)
    # return HttpResponse('detail.html')
    lead = Lead.objects.get(id=pk)
    print(lead)
    context = {"lead":lead}
    return render(request, 'lead_detail.html', context)

def lead_create(request):
    context = {"form":LeadForm()}
    return render(request, 'lead_create.html', context)