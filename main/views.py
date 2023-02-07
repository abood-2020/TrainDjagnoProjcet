from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request , 'index.html')

def about(request):
    return HttpResponse(("Hello , About Page"))

def main(request):
    return HttpResponse(("Hello , Main Page"))

def blog(request):
    return HttpResponse(("Hello , Blog Page"))