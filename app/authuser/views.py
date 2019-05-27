from django.shortcuts import render
import uuid
from rest_framework import views, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response


class AuthUserLogoutView(views.APIView):
    """
    Logs out all all session for a user by changing the users jwt secret
    """
    def post(self, request, *args, **kwargs):
        user = request.user
        user.jwt_secret = uuid.uuid4()
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)