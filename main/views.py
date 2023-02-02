from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse(("Hello, world. You're at the polls index."))

def about(request):
    return HttpResponse(("Hello , About Page"))

def main(request):
    return HttpResponse(("Hello , Main Page"))

def blog(request):
    return HttpResponse(("Hello , Blog Page"))