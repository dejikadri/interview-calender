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
    # Both candidate and interviewer are allowed to be null because when either adds a slot
    # the other field will be null at that time

    candidate = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null=True)
    interviewer = models.ForeignKey(Interviewer,  on_delete=models.SET_NULL, null=True)
    instruction_notes = models.TextField()  # interview instructions and feedback
    interview_date = models.DateField()
    interview_start_time = models.TimeField()
    interview_end_time = models.TimeField()


class OtherInterviewers(models.Model):
    """
    Other Interviewers when a candidate can be interviewed by
    more than one interviewers
    """
    interviewer = models.ForeignKey(Interviewer,  on_delete=models.CASCADE)
    interview_slot = models.ForeignKey(Interviewer,  on_delete=models.CASCADE)
