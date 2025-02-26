from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def HomePage(request):
    return render(request,'app1/index.html')

def Update(request):
    return render(request,'app1/update.html')