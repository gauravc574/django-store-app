from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product

# Create your views here.
def index(request):
    print("this is request coming",request)
    products = Product.objects.all()
    print("---- Products",products)
    return render(request, 'index.html',{'products':products})