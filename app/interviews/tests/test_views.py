from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Candidate, Interviewer, InterviewSlot


class CandidateListTest(TestCase):
    def setUp(self):
        candidate_john = Candidate.objects.create(
            full_name='John Smith',
            email='jsmith@acme.com',
            phone_number='+49 700 000 123',
            skype_id='john.smith'

        )
        candidate_john.save()

        candidate_hans = Candidate.objects.create(
            full_name='Hans Guldan',
            email='hguldan@acme.com',
            phone_number='+49 701 010 123',
            skype_id='hans.guldan'

        )
        candidate_john.save()

    def test_get_list_of_candidate(self):
        candidate_count = Candidate.objects.all()
        self.assertEqual(2, candidate_count.count())


