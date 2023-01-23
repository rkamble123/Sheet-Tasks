from django.db import models

# Create your models here.

class Team(models.Model):
    title = models.CharField(max_length=100)
    # team membres
    def __str__(self):
        return self.title

class CandidateProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.f_name} {self.l_name}'



class CandidateStatus(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class CandidateStage(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    # CandidateApplication


class JobProfile(models.Model):
    title = models.CharField(max_length=100)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    description = models.CharField(max_length=200,blank=True)
    # offered salary

    def __str__(self):
        return self.title



class CandidateApplication(models.Model):
    candidate = models.ForeignKey(CandidateProfile,on_delete=models.CASCADE)
    job = models.ForeignKey(JobProfile,on_delete=models.CASCADE)
    status = models.ForeignKey(CandidateStatus,on_delete=models.CASCADE)
    stage = models.ForeignKey(CandidateStage,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.candidate


class Feedback(models.Model):
    text = models.TextField()
    candidate = models.ForeignKey(CandidateApplication,on_delete=models.CASCADE)
