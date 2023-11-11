from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request,"websites/index.html")

def about_view(request):
    return render(request,"websites/about.html")

def contact_view(request):
    return render(request,"websites/contact.html")

