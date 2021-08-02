from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

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

# def lead_create(request):
#   form = LeadForm()
#   if request.method == 'POST':
#     print('receiving a post request')
#     form = LeadForm(request.POST)
#     if form.is_valid():
#       print('form is valid')
#       print(form.cleaned_data)
#       first_name = form.cleaned_data['first_name']
#       last_name = form.cleaned_data['last_name']
#       age = form.cleaned_data['age']
#       phoned = form.cleaned_data['phoned']
#       source = form.cleaned_data['source']
#       agent = Agent.objects.first()
#       Lead.objects.create(first_name=first_name, last_name=last_name, age=age, phoned=phoned, source=source, agent=agent)
#       print('Lead has created')
#       return redirect('/leads')
#   context = {"form":form}
#   return render(request, 'lead_create.html', context)

def lead_create(request):
  form = LeadModelForm()
  if request.method == 'POST':
    print('receiving a post request')
    form = LeadModelForm(request.POST)
    if form.is_valid():
      print('form is valid')
      print(form.cleaned_data)
      form.save()
      print('Lead has created')
      return redirect('/leads')
  context = {"form":form}
  return render(request, 'lead_create.html', context)