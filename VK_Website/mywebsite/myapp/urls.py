from django.urls import path
#importing views from the same app folder. '.' used for indicating that view is imported to current url
from . import views

urlpatterns = [
    path('', views.home, name="Homepage"),
    path('enter/', views.enter, name="Entering website"),
]