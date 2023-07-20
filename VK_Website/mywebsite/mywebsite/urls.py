"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#include function is used to call the urls from myapp folder
from django.urls import path, include
# from django.http import HttpResponse

# #Creating a default home request directing to a Welcome Message
# def home(request):
#     return HttpResponse("Welcome to VK HomePage")

# def enter(request):
#     return HttpResponse("Entering VK Site")

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', home), #calling the home function to display default welcome screen. "" inside path function will point to look in the current file for home.
    # path('enter/', enter), # navigating between pages. This page will be accessed from /enter/ along with the homepage link (homepage link is the django link you click to access the webserver)
    path('', include('myapp.urls')),

]
