from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render( request, 'home.html')


from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(
        request, 'home.html', {'new_item_text': request.POST['item_text'], }
    )