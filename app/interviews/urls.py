from django.urls import path
from .views import InterViewSlotList

urlpatterns = [
    path('interview/slot', InterViewSlotList.as_view(), name='interviewslotlist')
]