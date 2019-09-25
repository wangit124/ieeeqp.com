from django import forms
from dashboard.models import ScoreApplication
from landing.models import QPApplication

class ScoreApplicationForm(forms.ModelForm):
    class Meta:
        model = ScoreApplication
        fields = ('score',)

class UpdateQPApplication(forms.ModelForm):
    class Meta:
        model = QPApplication
        fields = ()