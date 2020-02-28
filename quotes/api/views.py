from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, CreateAPIView
from quotes.models import Quote
from registration.models import User
from quotes.api.serializers import QuotesSerializer, QuoteDetailSerializer, QuoteCreateSerializer
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

@api_view(['GET','PUT'])
@permission_classes((IsAuthenticated,))
def apiQuoteEditView(request, quote_id):
    quote=get_object_or_404(Quote,id=quote_id)
    user=request.user
    if quote.author!=user:
        return Response({'response':"you don't have permission to edit the quote!"})
    if request.method== "PUT":
        serializer=QuoteDetailSerializer(quote, data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['success']="update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    else:
        serializer=QuoteDetailSerializer(quote)
        return Response(serializer.data)


@api_view(['DELETE',])
@permission_classes((IsAuthenticated,))
def apiQuoteDeleteView(request, quote_id):
    quote=get_object_or_404(Quote,id=quote_id)
    user=request.user
    if quote.author!=user:
        return Response({'response':"you don't have permission to delete the quote!"})
    if request.method== "DELETE":
        operation=quote.delete()
        data={}
        if operation:
            data['success']="Delete successful"
        else:
            data['failure']="delete failed"
        return Response(data=data)


# @api_view(['GET','POST',])
# @permission_classes((IsAuthenticated,))
# def apiQuoteCreateView(request):
#     author=request.user
#     quote=Quote(author=author)
#     if request.method== "POST":
#         serializer=QuoteCreateSerializer(quote, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         serializer=QuoteCreateSerializer()
#         return Response(serializer.data)



class apiQuoteCreateView(CreateAPIView):
    serializer_class = QuoteCreateSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)