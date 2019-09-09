from django.forms import ModelForm
from landing.models import QPApplication

class QPAppModelForm(ModelForm):
    class Meta:
        model = QPApplication
        fields = '__all__'
