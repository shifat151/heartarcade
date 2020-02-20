from . import views
from django.urls import path

urlpatterns = [
    
    path('<uuid:user_id>/', views.profile, name='profile'),
    path('edit/', views.editProfile, name='editProfile'),
    path('editusername/', views.editSocialProfile, name='editSocialProfile'),
    path('<slug:slugifyUsername>/', views.showProfile, name='showProfile'),

    
    # path('time/', views.set_timezone, name='set_timezone')
]