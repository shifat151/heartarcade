from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView
 
from quotes.models import Quote, QuoteCategory
from registration.models import User
from . serializers import (profileSerializer,
                usernameSerializer,
                profileQuotesSerializer,
                UserPasswordChangeSerializer)
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def apiUserProfileView(request):
    try:
        profile=request.user
    except profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=profileSerializer(profile)
        return Response(serializer.data)


@api_view(['GET','PUT'])
@permission_classes((IsAuthenticated,))
def apiUsernameChangeView(request):
    try:
        profile=request.user
    except profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=usernameSerializer(profile)
        return Response(serializer.data)
    if request.method=='PUT':
        serializer=usernameSerializer(profile, data=request.data, context={'request': request})
        data={}
        if serializer.is_valid():
            serializer.save()
            data['response']="Username update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def apiProfileQuotes(request, slugifyUsername):
    user=get_object_or_404(User, slugged_username=slugifyUsername)
    profileQuotes=Quote.objects.filter(author=user)
    print(profileQuotes)
    if request.method=="GET":
        serializer=profileQuotesSerializer(profileQuotes, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class APIChangePasswordView(UpdateAPIView):
    serializer_class = UserPasswordChangeSerializer
    model = get_user_model() 
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

# @api_view(['PUT',])
# def APIChangePasswordView(request):
#     if request.method=='PUT':
#         serializer=UserPasswordChangeSerializer(data=request.data, context={'request': request})
#         data={}
#         if serializer.is_valid():
#             serializer.save()
#             data['response']="password change successful"
#         else:
#             data=serializer.errors
#         return Response(data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
