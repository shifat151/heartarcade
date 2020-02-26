from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from quotes.models import Quote
from quotes.api.serializers import QuotesSerializer, QuoteDetailSerializer
from django.shortcuts import get_object_or_404

# @api_view(['GET',])
# def api_quotes_view(request):
#     try:
#         all_quotes=Quote.objects.all()
#     except all_quotes.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method== "GET":
#         serializer=QuotesSerializer(all_quotes, many=True)
#         return Response(serializer.data)

class apiQuotesView(ListAPIView):
    queryset=Quote.objects.order_by('-pub_date').prefetch_related('author')
    serializer_class=QuotesSerializer
    Pagiantion_class=PageNumberPagination

@api_view(['GET',])
def apiQuoteDetailView(request, quote_id):
    quote=get_object_or_404(Quote,id=quote_id)
    if request.method== "GET":
        serializer=QuoteDetailSerializer(quote)
        return Response(serializer.data)

@api_view(['PUT',])
def apiQuoteEditView(request, quote_id):
    quote=get_object_or_404(Quote,id=quote_id)
    if request.method== "PUT":
        serializer=QuoteDetailSerializer(quote, data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['success']="update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

@api_view(['DELETE',])
def apiQuoteDeleteView(request, quote_id):
    quote=get_object_or_404(Quote,id=quote_id)
    if request.method== "DELETE":
        operation=quote.delete()
        data={}
        if operation:
            data['success']="Delete successful"
        else:
            data['failure']="delete failed"
        return Response(data=data)