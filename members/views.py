from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from store.models import Address


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'registration.html')


def add(request):
    if request.method == 'POST':
        first_name = request.POST['firstName']
        second_name = request.POST['secondName']
        username = request.POST['userName']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if username == 'AnonymousUser':
            return HttpResponse('Username cant be taken.')
        else:
            if password == repassword:
                if User.objects.filter(username=username).exists():
                    return HttpResponse('Username already taken,Go back and try again')
                elif User.objects.filter(email=email).exists():
                    return HttpResponse('email taken,Go back and try again')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name,
                                                    last_name=second_name)
                    user.save()
                    return HttpResponse('Congratulations! Registration Successful!')
            else:
                return HttpResponse('Password not matching,Go back and try again')
    else:
        return render(request, 'registration.html')


def logon(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'home.html', {'status': 'Invalid username/password'})
    else:
        return render(request, 'login.html')


@login_required(login_url='login')
def profile(request):
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'profile.html', {'addresses': addresses})


def logout(request):
    auth.logout(request)
    return redirect('login')
