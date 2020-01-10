from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from landing.models import QPApplication, team
from dashboard.models import ScoreApplication, ProjectProposal, Milestone
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ieeeqpucsd import settings
from itertools import chain
from . import forms
import os

@login_required
def index(request):
    return render(request, 'dashboard.html', context={})

class ProjectProposalCreate(LoginRequiredMixin, CreateView):
    model = ProjectProposal
    form_class = forms.ProjectProposalForm

    def get_success_url(self):
        return reverse('documentation_success')

    def get_context_data(self, **kwargs):
        ctx = super(ProjectProposalCreate, self).get_context_data(**kwargs)
        ctx['proposals_qp'] = ProjectProposal.objects.filter(program="qp").order_by('id')
        ctx['proposals_qp2'] = ProjectProposal.objects.filter(program="qp2").order_by('id')
        return ctx

class MilestoneCreate(LoginRequiredMixin, CreateView):
    model = Milestone
    form_class = forms.MilestoneReportForm

    def get_success_url(self):
        return reverse('documentation_success')

    def get_context_data(self, **kwargs):
        ctx = super(MilestoneCreate, self).get_context_data(**kwargs)
        ctx['milestone_1'] = Milestone.objects.filter(report_num='1').order_by('id')
        ctx['milestone_2'] = Milestone.objects.filter(report_num='2').order_by('id')
        return ctx

@login_required
def documentation_success(request):
    return render(request, 'documentation_success.html', context={})

@login_required
@user_passes_test(lambda u: u.has_perm('landing.can_score_applicant'))
def scoring(request):
    existing_ids = ScoreApplication.objects.filter(scorer_id=request.user.id).values_list('application_id', flat=True)
    existing_apps = QPApplication.objects.filter(id__in=existing_ids)
    unscored_apps = QPApplication.objects.exclude(id__in=existing_ids)

    context={
        'unscored_apps': unscored_apps,
        'existing_apps': existing_apps,
        'all_apps': QPApplication.objects.all().count,
    }
    return render(request, 'scoring.html', context)

@login_required
@user_passes_test(lambda u: u.has_perm('landing.can_score_applicant'))
def rubric(request):
    return render(request, 'dash_rubric.html', context={})

@login_required
@user_passes_test(lambda u: u.has_perm('landing.can_score_applicant'))
def score_applicant(request, appid):
    instance = get_object_or_404(QPApplication, id=appid)
    existing = ScoreApplication.objects.filter(scorer_id=request.user.id, application_id=instance.id)
    check_existing = existing and existing.count() > 0

    if request.method == "POST":
        update_form = forms.UpdateQPApplication(request.POST, instance=instance)
        score_form = forms.ScoreApplicationForm(request.POST)
        safe_num_scores = instance.num_of_scores if instance.num_of_scores else 0
        safe_score = instance.score if instance.score else 0

        if score_form.is_valid() and update_form.is_valid():
            post_score = score_form.save(commit=False)
            post_application = update_form.save(commit=False)
            post_score.application_id = instance.id
            post_score.scorer_id = request.user.id
            post_application.num_of_scores = safe_num_scores + 1
            cleaned_score = score_form.cleaned_data.get('score')
            cleaned_accept = update_form.cleaned_data.get('accepted')
            post_application.score = cleaned_score + safe_score
            if (cleaned_accept):
                post_application.accepted = cleaned_accept
            else:
                post_application.accepted = instance.accepted
            post_score.save()
            post_application.save()
            return redirect('scoring')
        
        if not score_form.is_valid() and update_form.is_valid():
            update_form.save()
    
    else:
        update_form = forms.UpdateQPApplication(instance=instance)
        score_form = forms.ScoreApplicationForm()

    context={
        'applicant': instance,
        'score_form': score_form,
        'update_form': update_form,
        'check_existing': check_existing,
    }

    return render(request, 'score_applicant.html', context)

@login_required
def teams(request):
    if request.method == "POST":
        create_team = forms.CreateTeamForm(request.POST)
        if create_team.is_valid():
            cleaned_members = create_team.cleaned_data['member_choices']
            custom_saved_members = create_team.customSave()

            for member in cleaned_members:
                app_instance = get_object_or_404(QPApplication, id=member.id)
                update_form = forms.UpdateQPApplication(request.POST, instance=app_instance)
                post_application = update_form.save(commit=False)
                post_application.team_id = custom_saved_members.pk
                post_application.accepted=1
                post_application.save()

            return redirect('teams')
    else:
        create_team = forms.CreateTeamForm()
    
    qpteams = {}
    qp2teams = {}
    
    context = {
        'create_team': create_team,
        'qpteams': team.objects.filter(nickname="QP").order_by('id'),
        'qp2teams': team.objects.filter(nickname="QP++").order_by('id'),
    }

    return render(request, 'teams.html', context)

@login_required
def specific_team(request, teamid):
    team_instance = get_object_or_404(team, id=teamid)
    members = team_instance.members.replace("['", "").replace("']", "").split("', '")
    program = team_instance.nickname
    mentor = User.objects.filter(id=team_instance.mentor_id)

    if program == 'QP':
        program = 'qp'
    else:
        program = 'qp2'

    emails = {}

    for member in members:
        name = member.split(" ")
        first_name = name[0]
        if len(name) > 2:
            for i in range(1, len(name) - 1):
                first_name += " "
                first_name += name[i]

        last_name = name[len(name) - 1]

        # Get QPApplicant and update
        applicant = QPApplication.objects.filter(programs=program, first_name__contains=first_name, last_name__contains=last_name)

        # update applicant instance
        for applicant_id in applicant.values('id'):
            applicant_instance = get_object_or_404(QPApplication, id=applicant_id['id'])
            update_applicant = forms.UpdateQPApplication(request.POST, instance=applicant_instance)
            update_commit_false = update_applicant.save(commit=False)
            update_commit_false.accepted=1
            update_commit_false.team_id=teamid
            update_commit_false.save()

        # get email
        email = applicant.values('email')

        for e in email:
            emails[member] = e['email']

    context = {
        'team': team_instance,
        'team_emails': emails,
        'mentor': mentor,
    }
    return render(request, 'specific_team.html', context)


@login_required
def mentors(request):
    image_list=[]
    email_list={}
    for root, dirs, files in os.walk(settings.STATIC_ROOT):
        for file in files:
            staticUrl = 'staff/'
            if file.endswith("_mentor.jpg"):
                mentor = User.objects.filter(first_name=file.replace("_mentor.jpg", ""))
                email = mentor.values_list('email', flat=True)
                name = mentor.values_list('first_name', flat=True)
                for i in range(0, len(email)):
                    email_list[name[i]] = email[i]

                staticUrl += file
                image_list.append(staticUrl)
    
    row1 = image_list[0: len(image_list)//4]
    row2 = image_list[len(image_list)//4: len(image_list)//2]
    row3 = image_list[len(image_list)//2: len(image_list)*3//4]
    row4 = image_list[len(image_list)*3//4: len(image_list)]

    return render(request, 'mentors.html', context={ 'row1': row1, 'row2': row2, 'row3': row3, 'row4': row4, 'emails': email_list })

@login_required
def calendar(request):
    return render(request, 'calendar.html', context={})

@login_required
def workshops(request):
    return render(request, 'workshops.html', context={})