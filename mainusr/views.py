from django.shortcuts import render 
from django.http import HttpResponse
from .models import Contact
# Create your views here.
def Admin(request):
    if request.method=='POST':
        name=request.POST['name']
        mobile=request.POST['mobile']
        x=Contact(name=name,mobile=mobile)
        x.save()
    all_msg=Contact.objects.all().filter(mobile=8390705048)

    return render(request, 'mainusr/index.html' , {'Contact':all_msg})