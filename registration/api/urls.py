from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
app_name='registration'

urlpatterns = [
    path('signup/', views.CreateUserAPIView, name='api_registration'),
    path('login/', obtain_auth_token, name='login'),
]