from django.urls import path
from .views import create_meeting, get_user_details, home, generate_access_token
urlpatterns = [
    path('', home),
    path('token/', generate_access_token),
    path('user/', get_user_details),
    path('create/', create_meeting)
]