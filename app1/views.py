from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def HomePage(request):
    return HttpResponse("Hi")