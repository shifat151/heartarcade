from . import views

from django.urls import path
app_name='blog'

urlpatterns = [
    path('', views.apiQuotesView.as_view(), name='all_blogs'),
    path('<uuid:quote_id>/', views.apiQuoteDetailView, name='edit_quote'),
    path('<uuid:quote_id>/edit', views.apiQuoteEditView, name='edit_quote'),
    path('<uuid:quote_id>/delete', views.apiQuoteDeleteView, name='edit_quote'),
]
