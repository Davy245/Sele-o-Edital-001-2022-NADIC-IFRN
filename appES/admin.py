from django.contrib import admin

from appES.models import Candidate, Election, Voter

# Register your models here.

admin.site.register(Election)
admin.site.register(Candidate)
admin.site.register(Voter)
