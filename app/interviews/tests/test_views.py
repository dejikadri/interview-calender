import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

client = Client()


class CandidateListTest(TestCase):
    def test_create_new_candidate(self):
        response = client.post(reverse('candidatelist'),
                               data=json.dumps({
                                                "full_name": "deji",
                                                "email": "dj@deji.com",
                                                "phone_number": "000-222-444",
                                                "skype_id": "ad.dk"
                                                }),
                               content_type='application/json'
                               )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
