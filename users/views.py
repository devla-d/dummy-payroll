from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .froms import RegisterForm, LoginForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


from baseapp import utils


def home(request):
    return render(request, "index.html")


def logi_n(request):
    destination = utils.get_next_destination(request)
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user:
                login(request, user)
                if destination:
                    return redirect(f"{destination}")
                else:
                    return redirect("dashboard")
        else:
            messages.warning(request, ("invalid credentials".upper()))
            return redirect("login")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def rigiste_r(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(
                request, "Account created successfully you can now login".capitalize()
            )
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


@login_required()
def dashboard(request):
    return render(request, "dashboard.html")


@login_required()
def history(request):
    return render(request, "history.html")


@login_required()
def profile(request):
    # form = ProfileForm
    return render(request, "profile.html")


@login_required()
def settings(request):
    if request.POST:
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            update_session_auth_hash(request, user=form.user)
            messages.info(request, "Password change")
            redirect("settings")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "settings.html", {"form": form})


def logou_t(request):
    messages.info(request, "Logged out")
    logout(request)
    return redirect("login")
