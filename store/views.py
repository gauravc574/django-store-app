from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category

# Create your views here.
def index(request):
    #print("this is request coming",request)
    products = Product.get_all_products()
    categories =  Category.get_all_categories()
    print('cat-----------',categories)

    data= {'products':products,'categories':categories}
    #print("---- Products",products)
    return render(request, 'index.html',data)