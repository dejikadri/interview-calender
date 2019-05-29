from datetime import date, datetime
from rest_framework import serializers
from .models import Candidate, Interviewer, InterviewSlot, OtherInterviewers


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('full_name', 'email', 'phone_number', 'skype_id')


class InterviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interviewer
        fields = ('full_name', 'email')


class OtherInterviewersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherInterviewers
        fields = ('interviewer', 'interview_slot')


class InterviewSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewSlot
        fields = (
                    'candidate', 'interviewer', 'instruction_notes', 'interview_date',
                    'interview_start_time', 'interview_end_time'
                  )

    def validate_interview_date(self, interview_date):
        """
        Check that interview date and time is not before current date and time.
        """
        now = datetime.now()
        if interview_date < date.today():
            raise serializers.ValidationError(f'The Supplied Date [{interview_date}] cannot  '
                                              f'be before todays date ')
        else:
            tm = self.initial_data['interview_start_time']
            if tm < now.strftime("%H:%M"):
                raise serializers.ValidationError(f'The Supplied time [{tm}] cannot  '
                                                  f'be before the current  time ')
            else:
                if str(tm).split(":")[1] != "00":
                    print(str(tm).split(":")[1], datetime.now())
                    raise serializers.ValidationError(f'The Supplied time [{tm}] must be on the hour  ')

        return interview_date
