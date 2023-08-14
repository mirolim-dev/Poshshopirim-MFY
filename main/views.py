from django.shortcuts import render

from .models import Worker
# Create your views here.

def home(request):
    return render(request, 'index.html')


def workers_view(request):
    workers = Worker.objects.filter(is_active=True)
    context = {
        'workers': workers,
        }
    return render(request, 'about.html', context)