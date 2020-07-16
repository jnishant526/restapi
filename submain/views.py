from django.shortcuts import render 
from django.http import HttpResponse
# Create your views here.
def User(request):
    return HttpResponse('This is usrlogin login')