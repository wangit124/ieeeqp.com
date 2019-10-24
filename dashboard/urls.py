from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('scoring/', views.scoring, name='scoring'),
    path('scoring/<int:appid>', views.score_applicant, name='score_applicant'),
    path('rubric/', views.rubric, name='rubric'),
    path('teams/', views.teams, name='teams'),
    path('teams/<int:teamid>', views.specific_team, name='specific_team'),
    path('mentors/', views.mentors, name='mentors'),
    path('proposal/', views.ProjectProposalCreate.as_view(), name='proposal'),
    path('documentation/success/', views.documentation_success, name='documentation_success'),
    path('milestones/', views.MilestoneCreate.as_view(), name='milestone'),
]
