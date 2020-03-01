from rest_framework import serializers
from registration.models import User




class RegistrationSerializer(serializers.ModelSerializer):
    
    username=serializers.CharField(label='Username:',help_text="Remember your username. It will be needed for signing in!")
    email=serializers.EmailField(label='Email:')
    password = serializers.CharField(label='Password:',style={'input_type': 'password'}, write_only=True,min_length=8,
    help_text="Your password must contain at least 8 characters and should not be entirely numeric."
    )
    password2=serializers.CharField(label='Confirm password:',style={'input_type': 'password'},  write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password', 'password2']
    
    def validate_username(self, username):
        username_exists=User.objects.filter(username__iexact=username)
        if username_exists:
            raise serializers.ValidationError({'username':'This username already exists'})
        return username

    def validate_email(self, email):
        email_exists=User.objects.filter(email=email)
        if email_exists:
            raise serializers.ValidationError({'email':'This email already exists'})
        return email
        
    def validate_password(self, password):
        if password.isdigit():
            raise serializers.ValidationError('Your password should contain letters!')
        return password       

    def validate(self, data):
        password=data.get('password')
        password2=data.pop('password2')
        if password != password2:
            raise serializers.ValidationError({'password':'password must match'})
        return data


    def create(self, validated_data):
        user= User.objects.create(
                username=validated_data['username'],
                email=validated_data['email']
            )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
# class RegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(style={'input_type': 'password'}, min_length=8, write_only=True)
#     class Meta:
#         model=User
#         fields=('username','email','password')
#     def create(self, validated_data):
#         user=User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user

