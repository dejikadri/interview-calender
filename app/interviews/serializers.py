from rest_framework import serializers
from .models import Candidate, Interviewer, InterviewSlot


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('full_name', 'email', 'phone_number', 'skype_id')


class InterviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interviewer
        fields = ('full_name', 'email', 'phone_number', 'skype_id')


class InterviewSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewSlot
        fields = ('full_name', 'email', 'phone_number', 'skype_id')
