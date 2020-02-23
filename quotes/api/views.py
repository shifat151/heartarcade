from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from quotes.models import Quote
from quotes.api.serializers import QuotesSerializer

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
