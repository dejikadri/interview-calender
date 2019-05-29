from django.urls import path
from .views import InterViewSlotList, InterViewSlotDetail, CandidateDetail, InterviewerDetail, \
    OtherInterviewersDetail


urlpatterns = [
    path('interview/slot/', InterViewSlotList.as_view(), name='interviewslotlist'),
    path('interview/slot/detail/<int:pk>/', InterViewSlotDetail.as_view(), name='interviewslotdetail'),

    path('interview/candidate/', CandidateDetail.as_view(), name='candidatedetail'),
    path('interview/interviewer/', InterviewerDetail.as_view(), name='interviewerdetail'),
    path('interview/otherinterviewers/', OtherInterviewersDetail.as_view(),name='otherInterviewersdetail'),

]
