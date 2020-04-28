from django.shortcuts import render,redirect
from .models import *
from .forms import NewWritterForm,NewPoemForm


def home(request):

    posts = Post.objects.all().order_by('-id')
    total_posts = posts.count()

    return render(request,'home/home.html',{'posts':posts,'total_posts':total_posts})

def writter_profile(request,pk):

    writter = Writter.objects.get(id=pk)
    posts = writter.post_set.all()
    total_posts_by_user = posts.count()

    context = {'writter':writter,'posts':posts,'total_posts_by_user':total_posts_by_user}

    return render(request,'home/writter_profile.html',context)

def server_info(request):
    return render(request,'home/server_info.html')

def sign_up(request):
    
    all_writters = Writter.objects.all()

    all_writters_name = []

    for i in all_writters:
        all_writters_name.append(i.name.lower())

    form = NewWritterForm()

    if request.method == 'POST':
        form = NewWritterForm(request.POST)
        if form.is_valid():
            if request.POST['name'].lower() in all_writters_name:
                return redirect('/')
            else:
                form.save()
                return redirect('/')

    context = {'form' : form}

    return render(request,'home/sign_up.html',context)

def new_poem(request):

    form = NewPoemForm()

    if request.method == 'POST':
        form = NewPoemForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/')

    context = {'form':form}

    return render(request,'home/new_poem.html',context)
    
