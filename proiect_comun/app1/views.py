from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Cazare
from .forms import newform

# Create your views here.

def index(request):
    cazare1 = Cazare.objects.all()
    return render(request, 'index.html',{'cazare': cazare1})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
            return redirect('login')
        else:
            messages.info(request, 'Password not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def search(request):
    if request.method == "POST":
        searched =request.POST['searched']
        posts = Cazare.objects.filter(title__icontains =searched)
        return render(request, 'search.html',
        {'searched':searched,
        'cazare':posts})
    else:
        return render(request, 'search.html')
    
def user(request):
    cazare1 = Cazare.objects.all()
    return render(request, 'user.html',{'cazare': cazare1})

def cazare(request,pk):
    cazare = Cazare.objects.get(id=pk)
    return render(request, 'cazare.html',{'cazare': cazare})

def new(request):
    submitted = False
    if request.method == "POST":
        form = newform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new?submitted=True')
    else:
        form = newform
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'new.html', {'form' : form, 'submitted' : submitted })

def main(request):
    cazare1 = Cazare.objects.all()
    return render(request, 'main.html',{'cazare': cazare1})