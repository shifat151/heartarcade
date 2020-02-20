from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.create, name='create'),
    path('edit/<uuid:quote_id>/', views.editQuote, name='editQuote'),
    path('<uuid:quote_id>/delete/', views.deleteQuote, name='deleteQuote'),
    path('category/<str:quote_cat>/', views.quoteCat, name='quoteCat'),
    path('search/', views.Search, name='searchAuthor')
    # path('time/', views.set_timezone, name='set_timezone')
]
