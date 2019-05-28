from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import views, permissions, status
from .models import Candidate, Interviewer, InterviewSlot
from .serializers import CandidateSerializer, InterviewerSerializer, InterviewSlotSerializer


class InterViewSlotList(APIView):
    """
    Retrieve all interview slots and create new slots
    """
    def get(self, request):
        slots = InterviewSlot.objects.all()
        serializer = InterviewSlotSerializer(slots, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InterviewSlotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
