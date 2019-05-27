from django.db import models


class Interviewer(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=2100)


class Candidate(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    skype_id = models.EmailField(max_length=100)


class InterviewSlot(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null=True)
    interviewer = models.ForeignKey(Interviewer,  on_delete=models.SET_NULL, null=True)
    instruction_notes = models.TextField()
    interview_date = models.DateField()
    interview_time = models.TimeField()
