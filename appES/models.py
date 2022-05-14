

from pyexpat import model

from django.db import models
from pkg_resources import require


# Create your models here.

class Election(models.Model):
    Name = models.CharField(max_length=255)
    startData = models.DateField()
    endDate = models.DateField()
    Description = models.TextField(blank=True)
    numCandidates = models.IntegerField(default=0)
    Winner = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.Name

    def winner():
     for i in Candidate:
        x = 0
        if i.numVotes >= x:
            x = i.numVotes
            c = Candidate.objects.get(numVotes = x)
            char = c.Name
        return char
    

    

class Candidate (models.Model):
    CPF = models.CharField(max_length=11)
    Name = models.CharField(max_length=255)
    dateBirth = models.DateField()
    Address = models.CharField(max_length=300)
    Election = models.ForeignKey('Election', on_delete=models.CASCADE)
    numVotes = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.Name
    

            
    

class Voter (models.Model):
    CPF = models.CharField(max_length=11)
    Candidate = models.ForeignKey('Candidate', on_delete=models.DO_NOTHING)
    Election = models.ManyToManyField('Election', default=[0])

