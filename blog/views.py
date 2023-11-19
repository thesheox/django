from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import Post,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import Comment_Form
from django.contrib import messages

def blog_view(request,**kwargs):
     posts=Post.objects.filter(status=1)
     if kwargs.get('cat_name')!=None:
          posts=Post.objects.filter(category__name=kwargs['cat_name'])
          
     if kwargs.get('author_username')!=None:
          posts=Post.objects.filter(author__username=kwargs['author_username'])
   
     if kwargs.get('tag_name')!=None:
          posts=Post.objects.filter(tags__name__in=[kwargs['tag_name']])
     
     posts=Paginator(posts,3)
     try:      
          page_number=request.GET.get('page')
          posts=posts.get_page(page_number)
     except PageNotAnInteger:
         posts=posts.get_page(1)
     except EmptyPage:
         posts=posts.get_page(1)
         

         
     context={'posts': posts}
     return render(request,"blog/blog-home.html",context)

    

def blog_single (request,pid):
     if request.method == 'POST':
          form=Comment_Form(request.POST)
          if form.is_valid():
              form.save()
              messages.add_message(request,messages.SUCCESS,"your comment submitted successfully") 
          else:
               messages.add_message(request,messages.ERROR,"your comment didnt submitted") 
    
     posts=Post.objects.filter(status=1)
     post=get_object_or_404(posts,pk=pid)
     comments=Comment.objects.filter(post=post.id,approved=True)
     form=Comment_Form()
     context={'post' : post,'comments':comments,'form':form}
     return render(request,"blog/blog-single.html",context)
def test(request):

     return render(request,'test.html')


def blog_search(request):
     posts=Post.objects.filter(status=1)
     if request.method =='GET':
          if s:=request.GET.get('s'):
               posts=posts.filter(content__contains=s)
          
    
     context={'posts': posts}
     return render(request,"blog/blog-home.html",context)
