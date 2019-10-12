from django import forms
from dashboard.models import ScoreApplication, ProjectProposal
from landing.models import QPApplication, team
from django.forms import models
from django.forms.fields import MultipleChoiceField

class AdvancedModelChoiceIterator(models.ModelChoiceIterator):
    def choice(self, obj):
        return (self.field.prepare_value(obj), obj)

class AdvancedModelChoiceField(models.ModelMultipleChoiceField):
    def _get_choices(self):
        if hasattr(self, '_choices'):
            return self._choices
        return AdvancedModelChoiceIterator(self)
    
    choices = property(_get_choices, MultipleChoiceField._set_choices)

class ScoreApplicationForm(forms.ModelForm):
    score = forms.IntegerField()

    class Meta:
        model = ScoreApplication
        fields = [
            'score',
        ]

    def clean(self, *args, **kwargs):
        score = self.cleaned_data.get('score')
        if  score is None or score < 0 or score > 10:
            raise forms.ValidationError("Please enter a score between 1 and 10!")
        return super(ScoreApplicationForm, self).clean(*args, **kwargs)

class ProjectProposalForm(forms.ModelForm):
    class Meta:
        model = ProjectProposal
        fields = '__all__'

class UpdateQPApplication(forms.ModelForm):
    class Meta:
        model = QPApplication
        fields = [
            'accepted'
        ]

class CreateTeamForm(forms.ModelForm):
    # using the above customized ModelChoiceField here
    member_choices = AdvancedModelChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset = QPApplication.objects.all(),
        required = False,
        help_text = 'Add members to this team'
    )

    def customSave(self):
        teams_json = []
        create_team = self.save(commit=False)
        cleaned_members = self.cleaned_data['member_choices']
        for member in cleaned_members:
            teams_json.append(member.first_name + ' ' + member.last_name)

        create_team.members = teams_json
        create_team.save()
        return create_team

    class Meta:
        model = team
        fields = [
            'name',
            'nickname',
        ]