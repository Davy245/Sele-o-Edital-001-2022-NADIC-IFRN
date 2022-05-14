from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import  *

urlpatterns = [
    path('', Index,name="Index"),
    path('formElection/', formsE, name='formsE'),
    path('formCandidate/', formsC, name='formsC'),
    path('listCandidates/<int:id>',listC, name="listC"),
    path('vote<int:id>', vote, name="vote")
]