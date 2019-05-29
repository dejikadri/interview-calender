from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import views, permissions, status
from .models import Candidate, Interviewer, InterviewSlot, OtherInterviewers
from .serializers import CandidateSerializer, InterviewerSerializer,\
    InterviewSlotSerializer, OtherInterviewersSerializer

from django.http import Http404


class InterViewSlotList(APIView):
    """
    Retrieve all interview slots and create new slots
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        slots = InterviewSlot.objects.all()
        serializer = InterviewSlotSerializer(slots, many=True)
        return Response(serializer.data)

    def post(self, request):
        candidate = request.data['candidate']
        interview_date = request.data['interview_date']
        interview_start_time = request.data['interview_start_time']

        # Check that the Interview slot is available
        slot = InterviewSlot.objects.filter(
                                            candidate=candidate,
                                            interview_date=interview_date,
                                            interview_start_time=interview_start_time
                                         )
        if not slot:
            serializer = InterviewSlotSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": f"The interview slot clashes with date {interview_date}"
                                      f" and time{interview_start_time}"})


class InterViewSlotDetail(APIView):
    def get_object(self, pk):
        try:
            return InterviewSlot.objects.get(pk=pk)
        except InterviewSlot.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        slot = self.get_object(pk)
        serializer = InterviewSlotSerializer(slot)
        return Response(serializer.data)

    def patch(self, request, pk):
        """ updates the interview slot to add an interviewer or a candidate depends on who booked the slot first """

        slot = self.get_object(pk)
        serializer = InterviewSlotSerializer(slot, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InterviewerDetail(APIView):
    def post(self, request):
        serializer = InterviewerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CandidateDetail(APIView):
    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OtherInterviewersDetail(APIView):
    def post(self, request):
        serializer = OtherInterviewersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)