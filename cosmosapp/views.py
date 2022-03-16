#from turtle import distance
#from audioop import reverse
#from django.http import HttpResponse, HttpResponseRedirect
from audioop import reverse
import cmath
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import PlanetsData
from .models import Planets
# Create your views here.
global cm

def add_show(request):
    if request.method == 'POST':
        fm = PlanetsData(request.POST)
        if fm.is_valid():
            #fm.save()
            nm = fm.cleaned_data['name']
            di = fm.cleaned_data['distance']
            st = fm.cleaned_data['stars']
            reg = Planets(name=nm, distance=di, stars=st)
            reg.save() 
            fm = PlanetsData()
           
    else:
        fm = PlanetsData()
        # cm = Planets.objects.all() 
        # print(cm)

    return render(request,'cosmosapp/dbaddandshow.html', {'form':fm})

def add_list(request):
    cm = Planets.objects.all() 
    return render(request, 'cosmosapp/dblist.html',{'cmd':cm})

def add_update(request , id):
    if request.method == 'POST':
        pi = Planets.objects.get(pk=id)
        fm = PlanetsData(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Planets.objects.get(pk=id)
        fm = PlanetsData(instance=pi)
    return render(request,'cosmosapp/updateplanets.html', {'form': fm})


def delete_data(request, id):
    
    pi = Planets.objects.get(pk=id)
    pi.delete()
    return redirect('show')
    
