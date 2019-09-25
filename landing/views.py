from django.shortcuts import render, redirect
from django.views import generic
from landing.forms import QPAppModelForm, UserLoginForm, UserRegisterForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from landing.models import QPApplication
import django.db.models.fields.reverse_related
from django.urls import reverse
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)


def index(request):
    return render(request, 'index.html', context={})


class QPApplicationCreate(CreateView):
    model = QPApplication
    form_class = QPAppModelForm

    def get_success_url(self):
        return reverse('apply-success')


def apply_success(request):
    return render(request, 'apply_success.html', context={})


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/dashboard/')

    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/login/')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')
