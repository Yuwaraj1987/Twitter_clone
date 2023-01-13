from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    # if the method is POST 
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) 
        # if the for is valid
        if form.is_valid():
            # Yes, save
            form.save()
            # Redirect to Home
            return HttpResponseRedirect('/')
        else:
            # No, show Error
            return HttpResponseRedirect(form.errors.as_json())
    
    
    #get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    
    # show
    return render(request, 'post.html',
                   {'posts': posts})

# Create your views here.

def delete(request, post_id):
    # Find post
    
    post =Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

# create edit post
# def edit(request, post_id):
   
#     return HttpResponseRedirect('/edit.html')
def edit(request,post_id):
    post=Post.objects.get(id=post_id)
    # if request.method=="GET":
    #     return render(request,"edit.html",{"post":post})
    if request.method=="POST":
        # editposts=Post.objects.get(id=post_id)
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():

                #yes Save
            form.save()
                #redirect to home
            return HttpResponseRedirect('/') 
        else:
            return HttpResponseRedirect(form.erros.as_json())
    return render(request, "edit.html", {"post": post})

def like(request, post_id):
    count=Post.objects.get(id=post_id)
    if count.count ==0:
        count.count +=1 
        count.save()
    elif count.count ==1:
        count.count -=1
        count.save()
    return HttpResponseRedirect('/')


