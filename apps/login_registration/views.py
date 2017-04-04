from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User
import re

# Create your views here.
def start(request):
    return render(request, 'login_registration/index.html')

def submit(request):
    error = False
    if request.method == 'POST':
        if request.POST['action'] == 'register':
            name = User.objects.nm_validate(request.POST['name'])
            if not name:
                messages.add_message(request, messages.ERROR, 'Name too short!', extra_tags = 'name')
                error = True
            alias = User.objects.alias_validate(request.POST['alias'])
            if not alias:
                messages.add_message(request, messages.ERROR, 'Alias too short!', extra_tags = 'alias')
                error = True
            email = User.objects.email_validate(request.POST['email'])
            if not email:
                messages.add_message(request, messages.ERROR, 'Invalid email!', extra_tags = 'email')
                error = True
            email_exists = User.objects.email_exists(request.POST['email'])
            if not email_exists:
                messages.add_message(request, messages.ERROR, 'Email already exists!', extra_tags = 'email')
                error = True
            password = User.objects.password_validate(request.POST['password'])
            if not password:
                messages.add_message(request, messages.ERROR, 'Password too short!', extra_tags = 'password')
                error = True
            password_match = User.objects.password_match(request.POST['password'], request.POST['confirm_password'])
            if not password_match:
                messages.add_message(request, messages.ERROR, 'Passwords do not match!', extra_tags = 'match')
                error = True

            if error:
                print messages
                return redirect('login_registration:start')
            else:
                new = User.objects.createUser(name = request.POST['name'], alias = request.POST['alias'], email = request.POST['email'],password = request.POST['password'])
                context={
                    'user': new
                }
                request.session['user_id'] = new.id
                request.session['user_name'] = new.name
                return redirect('book_review:start')

        elif request.POST['action'] == 'login':
            try:
                user = User.objects.get(email = request.POST['email'])
            except Exception:
                messages.add_message(request, messages.ERROR, 'Email does not exist. Please register to login in!', extra_tags = 'deny')
                return redirect('login_registration:start')

            if not User.objects.passwordsMatchCheck(request.POST['password'], user.password):
                messages.add_message(request, messages.ERROR, 'Email or password is not correct!', extra_tags = 'deny')
                return redirect('login_registration:start')
            else:
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('book_review:start')
