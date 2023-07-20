from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse



#Creating a default home request directing to a Welcome Message
def home(request):
    # return HttpResponse("Welcome to VK HomePage")
    return render(request, 'home.html') # render function is used to point the html files inside template folder
def enter(request):
    # return HttpResponse("Entering VK Site")
    return render(request, 'enter.html')