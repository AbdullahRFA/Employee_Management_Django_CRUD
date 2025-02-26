from django.shortcuts import render,HttpResponse,redirect
from .forms import EmployeForm
# Create your views here.
def HomePage(request):
    form = EmployeForm()
    return render(request,'app1/index.html',{"form":form})

def Update(request):
    return render(request,'app1/update.html')