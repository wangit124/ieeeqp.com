from django import forms
from dashboard.models import ScoreApplication
from landing.models import QPApplication

class ScoreApplicationForm(forms.ModelForm):
    score = forms.IntegerField()

    class Meta:
        model = ScoreApplication
        fields = [
            'score',
        ]

    def clean(self, *args, **kwargs):
        score = self.cleaned_data.get('score')
        if score < 0 or score > 10:
            raise forms.ValidationError("Please enter a score between 1 and 10!")
        return super(ScoreApplicationForm, self).clean(*args, **kwargs)

class UpdateQPApplication(forms.ModelForm):
    class Meta:
        model = QPApplication
        fields = ()