from django.http import HttpResponse
from .models import city
from django.shortcuts import render
from .forms import Addcity


def index(request):
    if request.method == 'POST':
        form_data = Addcity(request.POST)
        if form_data.is_valid():
            form_data.save()
    form_add = Addcity
    City = city.objects.all()
    return render(request, 'index.html', {'city': City, 'form': form_add})

