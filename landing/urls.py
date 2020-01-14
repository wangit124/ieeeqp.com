from django.urls import path
from . import views
from datetime import date

deadline = date(2020, 1, 16)
today = date.today()

if (today >= deadline):
    application_view = views.apply_closed
else:
    application_view = views.QPApplicationCreate.as_view()

urlpatterns = [
    path('', views.index, name='index'),
    path('apply/', application_view, name='apply'),
    path('success/', views.apply_success, name='apply-success'),
    path('login/', views.login_view, name='login'),
    path('ieeeqpsignup/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
