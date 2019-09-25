from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apply/', views.QPApplicationCreate.as_view(), name='apply'),
    path('success/', views.apply_success, name='apply-success'),
    path('login/', views.login_view, name='login'),
    path('ieeeqpsignup/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
