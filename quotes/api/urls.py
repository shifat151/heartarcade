from . import views

from django.urls import path
app_name='blog'

urlpatterns = [
    path('', views.apiQuotesView.as_view(), name='all_blogs')
]
