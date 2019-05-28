from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from ..models import Candidate, Interviewer, InterviewSlot


class CandidateTest(TestCase):
    def setUp(self):
        candidate_john = Candidate.objects.create(
            full_name='John Smith',
            email='jsmith@acme.com',
            phone_number='+49 700 000 123',
            skype_id='john.smith'

        )

    def test_retrieve_candidate(self):
        get_candidate = Candidate.objects.get(email='jsmith@acme.com')
        self.assertEqual('jsmith@acme.com', get_candidate)