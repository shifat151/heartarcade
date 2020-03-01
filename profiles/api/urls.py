from . import views
from django.urls import path
app_name='profiles'

urlpatterns = [
    path('', views.apiUserProfileView, name='user_profile'),
    path('change-password', views.APIChangePasswordView.as_view(), name='password_change'),
    path('change-username', views.apiUsernameChangeView, name='change_username'),
    path('<slug:slugifyUsername>/', views.apiProfileQuotes, name='profile_quotes'),

    

]
