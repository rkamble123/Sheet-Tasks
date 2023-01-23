from django.contrib import admin
from .models import Team,CandidateProfile,CandidateStatus,CandidateStage,Feedback,JobProfile,CandidateApplication

# Register your models here.

admin.site.register(Team)
admin.site.register(CandidateProfile)
admin.site.register(CandidateStatus)
admin.site.register(CandidateStage)
admin.site.register(Feedback)
admin.site.register(JobProfile)
admin.site.register(CandidateApplication)

