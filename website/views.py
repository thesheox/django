from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm,contact_form,NewsletterForm
from django.contrib import messages

def home_view(request):
    return render(request,"websites/index.html")

def about_view(request):
    return render(request,"websites/about.html")

def contact_view(request):
    if request.method == "POST":
        form=contact_form(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"your ticket submitted successfully") 
        else:
            messages.add_message(request,messages.ERROR,"your ticket didnt submitted ") 
    form=contact_form()
    return render(request,"websites/contact.html",{'form':form})

def test_view(request):
    if request.method == "POST":
        form=contact_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("Invalid")
  
        
    form=contact_form()
    return render(request,'test.html',{"form":form})


def newsletter_view(request):
    if request.method == "POST":
        form=NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
