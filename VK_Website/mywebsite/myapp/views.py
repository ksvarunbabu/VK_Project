from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#Creating a default home request directing to a Welcome Message
def home(request):
    return HttpResponse("Welcome to VK HomePage")

def enter(request):
    return HttpResponse("Entering VK Site")