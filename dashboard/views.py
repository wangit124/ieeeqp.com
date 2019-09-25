from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from landing.models import QPApplication

@login_required
def index(request):
    return render(request, 'dashboard.html', context={})

@login_required
def scoring(request, appid=0):
    context={
        'qpapplications': QPApplication.objects.all(),
    }
    return render(request, 'scoring.html', context)