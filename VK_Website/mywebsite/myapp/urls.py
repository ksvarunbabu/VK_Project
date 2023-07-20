from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Homepage"),
    path('enter/', views.enter, name="Entering website"),
]