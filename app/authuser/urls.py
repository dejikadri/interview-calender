from django.urls import path
from djoser import views as djoser_views
from rest_framework_jwt import views as jwt_views
from authuser import views


urlpatterns = [
    # Djoser paths
    path('user/view/', djoser_views.UserView.as_view(), name='user-view'),
    path('user/delete/', djoser_views.UserDeleteView.as_view(), name='user-delete'),
    path('user/create/', djoser_views.UserCreateView.as_view(), name='user-create'),
    # JWT  paths
    path('user/login/', jwt_views.ObtainJSONWebToken.as_view(), name='user-login'),
    path('user/login/refresh/', jwt_views.RefreshJSONWebToken.as_view(), name='user-login-refresh'),
]
