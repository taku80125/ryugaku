from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def index(request):
        return render(request,'mysite/index.html')   


def money(request):
    return render(request,'mysite/money.html')    

def language(request):
    return render(request,'mysite/language.html')    

def programming(request):
    return render(request,'mysite/programming.html')    

def getback(request):
    return render(request,'mysite/getback.html')    

def contact(request):
    if request.method =="POST":
        email= request.POST.get('email')
        massage = request.POST.get('massage')
        c=Contact(email=email,  massage=massage)
        c.save()
  
        return render(request,'mysite/getback.html')   
    else:
        return render(request,'mysite/contact.html')   
