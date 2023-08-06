from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

teas = [
    {'id': 1, 'name': 'Black Tea'},
    {'id': 2, 'name': 'Indian Masala Tea'},
    {'id': 3, 'name': 'Green Tea'},
]

#Creating a default home request directing to a Welcome Message
def home(request):
    # return HttpResponse("Welcome to VK HomePage")
    # return render(request, 'myapp/home.html', {'teas': teas}) # render function is used to point the html files inside template folder
    context = {'teas' : teas}
    return render(request, 'myapp/home.html', context)
def enter(request):
    # return HttpResponse("Entering VK Site")
    return render(request, 'myapp/enter.html')