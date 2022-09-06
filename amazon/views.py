from itertools import product
import re
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helloworld(reqest):
    return HttpResponse("helloworld")

def mywebsite(request):
    return HttpResponse("<h1> iti website </h1>")

def sayhello(request, name):
    return HttpResponse(f"<h1> hi {name} </h1>")

def contactus(request):
    #return HttpResponse("this is my amazon")
    return render(request, "amazon/contactus.html")

def amazonproducts(request):
    products= [
        {"id":1, "name":"mobile","image":"1.png"},
        {"id":2, "name":"camera","image":"2.png"},
        {"id":3, "name":"labtop","image":"3.png"}
    ]
    content= {"products":products}
    return render(request, "amazon/products.html", content)

def aboutus(request):
    return render(request, "amazon/aboutus.html")