from django.shortcuts import render
from django.http import HttpResponse

def home_view(requests):
    return HttpResponse("<h1>home page</h1>")

def about_view(requests):
    return HttpResponse("<h1>about page</h1>")

def contact_view(requests):
    return HttpResponse("<h1>contact page</h1>")
