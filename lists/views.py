from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#home_page = None

def home_page(request):
#    pass
#    return HttpResponse()
    return HttpResponse('<html><title>Django-tdd</title></html>')
