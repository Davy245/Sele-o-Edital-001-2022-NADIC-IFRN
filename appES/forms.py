from enum import _auto_null, auto
from shutil import which
from django import forms
from django import views
from django.views import View
from .models import *
from .views import *

class electionForms (forms.Form):
    model: Election
    Name = forms.CharField(max_length=255)
    startData = forms.DateField()
    endDate = forms.DateField()
    Description = forms.CharField(widget=forms.Textarea, required=False)
    

class candidateForms (forms.Form):
    model = Candidate
    CPF = forms.CharField(max_length=11)
    Name = forms.CharField(max_length=255)
    dateBirth = forms.DateField(error_messages={'invalid': 'Essa data não é válida'})
    Address = forms.CharField(max_length=300)
    Election = forms.ModelChoiceField(queryset=Election.objects.all())  


class voterForms(forms.Form):
    
    model = Voter
    CPF = forms.CharField(max_length=11)
    
