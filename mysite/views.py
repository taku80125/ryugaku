from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def index(request):
        return render(request,'mysite/index.html')   


def money(request):
    return render(request,'mysite/money.html')    
