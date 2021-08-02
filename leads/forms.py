from django import forms
from .models import Lead

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            'first_name',
            'last_name',
            'age',
            'phoned',
            'source',
            'agent'
        ]

class LeadForm(forms.Form):
  SOURCE_CHOICES = (
    ('YouTube', 'YouTube'),
    ('Google', 'Google'),
    ('Newsletter', 'Newsletter'),
    ('LinkedIn', 'LinkedIn'),
  )
  first_name = forms.CharField(max_length=100)
  last_name = forms.CharField(max_length=100)
  # email = forms.EmailField()
  age = forms.IntegerField(min_value=0)
  phoned = forms.BooleanField(required=False)
  source = forms.ChoiceField(choices=SOURCE_CHOICES)