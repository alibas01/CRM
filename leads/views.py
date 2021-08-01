from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    #return HttpResponse('home.html')
    return render(request, 'second_page.html', {})
