from django.shortcuts import render, redirect
from accounts.forms import MyAuthenticationForm, MyUserCreationForm
from django.views.decorators.http import (
    require_http_methods, 
    require_POST,
)
from django.contrib.auth import (
    login as auth_login, 
    logout as auth_logout,
)

# Create your views here.
@require_http_methods(["GET", "POST"])
def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        form = MyAuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_page = request.GET.get("next") or "home"
            return redirect(next_page)
    else:
        form = MyAuthenticationForm()
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("home")


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("home") 
    else:
        form = MyUserCreationForm()
    context = {
        "form": form
    }
    return render(request, "accounts/signup.html", context)