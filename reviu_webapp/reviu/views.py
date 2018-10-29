from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def login(request):
    return render(request, 'reviu/login.html')

def home(request):
	return render(request, 'reviu/home.html')