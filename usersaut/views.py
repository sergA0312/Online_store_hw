from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from usersaut.forms import RegisterForm,LoginForm

def register_view(request):
    if request.method == 'GET':
        context_data = {'form': RegisterForm()}
        return render(request, 'users/Register.html', context=context_data)

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1']
                )
                return redirect('/users/login/')
            else:
                form.add_error('password2', 'Password must be at least 8 characters.')

        context_data = {'form': form}
        return render(request, 'users/Register.html', context=context_data)


def login_view(request):
    if request.method == 'GET':
        context_data = {'form': LoginForm()}
        return render(request, 'users/login.html', context=context_data)

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )

            if user:
                login(request, user=user)
                return redirect('product_menu')
            else:
                form.add_error('password', 'Incorrect password.')

        context_data = {'form': form}
        return render(request, 'users/login.html', context=context_data)


def logout_view(request):
    logout(request)
    return redirect('product_menu')
