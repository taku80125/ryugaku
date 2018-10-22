from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def index(request):
    if request.method =="POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        
        c=Student(firstname=firstname, lastname=lastname)
        c.save()
  
        return render(request,'mysite/about.html')   
    else:
        return render(request,'mysite/index.html')   


def about(request):
    return render(request,'mysite/about.html')    
