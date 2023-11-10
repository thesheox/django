from django.shortcuts import render
from django.http import HttpResponse

def blog_view(request):
     return render(request,"blog/blog-home.html")
    

def blog_single (request):

    return render(request,"blog/blog-single.html",{'title':'my first blog post about django','content':'django is very sweet for me and im so excited to build my first app with it','author':'shayan saeidian'})
    
