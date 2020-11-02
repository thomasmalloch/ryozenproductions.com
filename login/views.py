from django.shortcuts import render
from .forms import LoginForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from common.backend import Functions


def logout_and_redirect(request):
    logout(request)
    return redirect('index')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(email__iexact=form.cleaned_data["email"])
            except:
                user = None

            user = authenticate(request, username=user.username, password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()

    context = Functions.build_page_context("login", request)
    context["form"] = form
    context["method"] = request.method
    return render(request, 'login/login.html', context=context)


def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["email"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"])

            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()

    context = Functions.build_page_context("register", request)
    context["form"] = form
    return render(request, 'login/register.html', context=context)

