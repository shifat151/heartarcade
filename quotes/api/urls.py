from . import views

from django.urls import path
app_name='blog'

urlpatterns = [
    path('', views.apiQuotesView.as_view(), name='all_quotes'),
    path('categories/', views.apiCategoryView.as_view(), name='all_category'),
    path('create', views.apiQuoteCreateView.as_view(), name='create_quote'),
    path('<uuid:quote_id>/', views.apiQuoteDetailView, name='detail_quote'),
    path('<uuid:quote_id>/edit', views.apiQuoteEditView, name='edit_quote'),
    path('<uuid:quote_id>/delete', views.apiQuoteDeleteView, name='delete_quote'),
]
