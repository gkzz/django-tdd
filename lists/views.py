"""
from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render( request, 'home.html')
"""

from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    if request.method == 'POST': 
        return HttpResponse(request.POST['item_text'])
    
    return render(request, 'home.html')