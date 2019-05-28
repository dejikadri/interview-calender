from datetime import date, datetime
from rest_framework import serializers
from .models import Candidate, Interviewer, InterviewSlot


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('full_name', 'email', 'phone_number', 'skype_id')


class InterviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interviewer
        fields = ('full_name', 'email')


class InterviewSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewSlot
        fields = ('candidate', 'interviewer', 'instruction_notes', 'interview_date', 'interview_time')

    def validate_interview_date(self, data):
        """
        Check that interview date and time is not before current date and time.
        """
        now = datetime.now()
        if data < date.today():
            raise serializers.ValidationError(f'The Supplied Date [{data}] cannot  '
                                              f'be before todays date ')
        else:
            tm = self.initial_data['interview_time']
            if self.initial_data['interview_time'] < now.strftime("%H:%M"):
                raise serializers.ValidationError(f'The Supplied time [{tm}] cannot  '
                                                  f'be before the current  time ')
        return data
