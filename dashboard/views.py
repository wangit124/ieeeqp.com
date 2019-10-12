from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from landing.models import QPApplication, team
from dashboard.models import ScoreApplication, ProjectProposal
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import forms
import os
from ieeeqpucsd import settings

@login_required
def index(request):
    return render(request, 'dashboard.html', context={})

class ProjectProposalCreate(CreateView):
    model = ProjectProposal
    form_class = forms.ProjectProposalForm

    def get_success_url(self):
        return reverse('documentation-success')

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
                post_application.save()

            return redirect('teams')
    else:
        create_team = forms.CreateTeamForm()
    
    context = {
        'create_team': create_team,
        'teams': team.objects.all(),
    }

    return render(request, 'teams.html', context)

@login_required
def mentors(request):
    image_list=[]
    for root, dirs, files in os.walk(settings.STATIC_ROOT):
        for file in files:
            staticUrl = 'staff/'
            if file.endswith("_mentor.jpg"):
                staticUrl += file
                image_list.append(staticUrl)
    
    row1 = image_list[0: len(image_list)//4]
    row2 = image_list[len(image_list)//4: len(image_list)//2]
    row3 = image_list[len(image_list)//2: len(image_list)*3//4]
    row4 = image_list[len(image_list)*3//4: len(image_list)]

    return render(request, 'mentors.html', context={ 'row1': row1, 'row2': row2, 'row3': row3, 'row4': row4  })