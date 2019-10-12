from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('scoring/', views.scoring, name='scoring'),
    path('scoring/<int:appid>', views.score_applicant, name='score_applicant'),
    path('rubric/', views.rubric, name='rubric'),
    path('teams/', views.teams, name='teams'),
    path('mentors/', views.mentors, name='teams'),
    path('documentation/', views.ProjectProposalCreate.as_view(), name='documentation'),
    path('documentation/success/', views.documentation_success, name='documentation_success'),
]
