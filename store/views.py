from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print("this is request coming",request)
    return render(request, 'index.html')