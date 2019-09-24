from django.shortcuts import render
from django.views import generic
from landing.forms import QPAppModelForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from landing.models import QPApplication
import django.db.models.fields.reverse_related
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html', context={})

class QPApplicationCreate(CreateView):
    model = QPApplication
    fields = '__all__'

    def get_success_url(self):
        return reverse('apply-success');

def apply_success(request):
    return render(request, 'apply_success.html', context={})

def login(request):
    return render(request, 'login.html', context={})
