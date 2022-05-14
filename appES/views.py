from datetime import datetime
from multiprocessing import context
from re import I
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .forms import *
from .models import *
from datetime import date
# Create your views here.

def Index(request):
    
    today = date.today()
    election = Election.objects.all()
    
    
    return render (request, 'index.html', context={ 'election' : election , 'today': today})

def formsE(request):
    if request.method == "GET":
        form=electionForms()
        return render (request, 'forms_election.html',context = {'form':form})
    else:
        form = electionForms(request.POST)
        
        if form.is_valid():
            
            Name = form.cleaned_data.get("Name")
            startData = form.cleaned_data.get("startData")
            endDate = form.cleaned_data.get("endDate")
            Description = form.cleaned_data.get("Description")
            

            obj = Election.objects.create(Name = Name, startData = startData, endDate = endDate,Description = Description)
            obj.save()

            

            form = candidateForms()
            return redirect ('Index')

        return render (request, 'forms_election.html',context= {'form' : form})


def formsC(request):
    if request.method == "GET":
        form=candidateForms()
        return render (request, 'forms_candidate.html',context= {'form' : form})
    
    else:
        form = candidateForms(request.POST)
        
        if form.is_valid():
            
            CPF = form.cleaned_data.get("CPF")
            Name = form.cleaned_data.get("Name")
            dateBirth = form.cleaned_data.get("dateBirth")
            Address = form.cleaned_data.get("Address")
            election = form.cleaned_data.get("Election")

            

            obj = Candidate.objects.create(CPF = CPF, Name = Name, dateBirth = dateBirth, Address = Address, Election = election)
            obj.save()

            e = Election.objects.get(id = election.id)
            e.numCandidates +=  1
            e.save()

            form = candidateForms()
            return redirect ('Index')

        return render (request, 'forms_candidate.html',context= {'form' : form})

def listC(request, id):

    candidate = Candidate.objects.filter(Election = id)

    return render (request, 'list_candidate.html',context= {'candidate' : candidate})

def vote(request, id):

    can = Candidate.objects.get(id = id)
    can.numVotes += 1
    can.save()

    if request.method == "GET":
        form=voterForms()
        return render (request, 'vote.html',context= {'form' : form})
    else:

            form = voterForms(request.POST)

            

            if form.is_valid():
                CPF = form.cleaned_data.get("CPF")


                obj = Voter.objects.create(CPF = CPF, Candidate = 0, Election = 0)
                obj.save()





                form = voterForms() 
                return redirect ('Index')
            
    return render (request, 'vote.html',context= {'form' : form})
