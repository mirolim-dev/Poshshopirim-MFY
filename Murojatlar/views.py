from django.shortcuts import render

from .models import Appeal
# Create your views here.

def contact(request):
    if request.POST:
        pass
    
    context = {
        
    }
    return render(request, 'contact.html', context)