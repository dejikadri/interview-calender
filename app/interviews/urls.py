from django.urls import path
from .views import InterViewSlotList, InterViewSlotDetail, CandidateList, InterviewerList, \
    OtherInterviewersList


urlpatterns = [
    path('interview/slot/', InterViewSlotList.as_view(), name='interviewslotlist'),
    path('interview/slot/detail/<int:pk>/', InterViewSlotDetail.as_view(), name='interviewslotdetail'),

    path('interview/candidate/', CandidateList.as_view(), name='candidatelist'),
    path('interview/interviewer/', InterviewerList.as_view(), name='interviewerlist'),
    path('interview/otherinterviewers/', OtherInterviewersList.as_view(), name='otherInterviewerslist'),

]
