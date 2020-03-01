from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from registration.api.serializers import RegistrationSerializer

@api_view(['POST',])
def CreateUserAPIView(request):
    if request.method== 'POST':
        serializer=RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']="succesfully registered a new user"
            data['email']=account.email
            data['username']=account.username
            token=Token.objects.get(user=account).key
            data['token']=token
        else:
            data=serializer.errors
        return Response(data)

# class CreateUserAPIView(CreateAPIView):
#     model=get_user_model()
#     permission_classes=[
#         permissions.AllowAny
#     ]
#     serializer_class=RegistrationSerializer

