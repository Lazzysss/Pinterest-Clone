from django.shortcuts import render
from app.models import Post
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from .forms import PostForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
from django.db.models import Q

def home(request, pagename):
	products = Post.objects.all()
	context = {
		'products' : products
	}
	return render(request, 'base.html',context)

def success_class(request):
    context = {}
    return render(request, 'registration/success_register.html',context)

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'registration/sign_in.html', context)

def sign_out(request):
    logout(request)
    return redirect('success_out')

def success_out(request):
    context = {}
    return render(request, 'registration/success_out.html',context)

def sign_up(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            #login(request, user)
            return redirect('success_class')
        else:
            messages.error(request, 'An error occured during registration')
    context = {
        'form': form
    }
    return render(request, 'registration/sign_up.html', context)


def MyProfile(request):
    context = {}
    return render(request, 'MyProfile.html',context)

#создать
def create(request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('/')
    context = {
       'form' : form 
    }
    return render(request, 'create.html', context)

#Удалить
def delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/')

#редактировать 
def update(request, pk):
    computer = Computers.objects.get(id=pk)
    form = ComputersForm(instance=computer)
    if request.method == 'POST':
        form = ComputersForm(request.POST, instance=computer, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
       'form' : form 
    }
    return render(request, 'post_update.html', context)

def detaile(request, pk):
    product = Post.objects.get(id=pk)
    context = {
        'product' : product
    }
    return render(request, 'detaile.html', context)

def MyPosts(request):

    product = Post.objects.filter(author=request.user)
    context = {
        'product':product,
    }
    return render(request, 'MyPosts.html', context)

def change_password(request):
    success_url = reverse_lazy('success_password')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return HttpResponseRedirect(success_url)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })


def success_password(request):
    return render(request, 'registration/success_password.html')

def search(request):
  query = request.GET.get('search')
  object_list = Post.objects.filter(Q(name__icontains=query))
  context = {
    'object_list':object_list
  }
  return render(request, 'search_results.html', context)