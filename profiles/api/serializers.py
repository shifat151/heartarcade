from rest_framework import serializers
from quotes.models import Quote,QuoteCategory
from registration.models import User

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email']
        read_only_fields = ['email']

class usernameSerializer(serializers.ModelSerializer):
    username=serializers.CharField(label='Username:',help_text="Remember your username. It will be needed for signing in!")
    class Meta:
        model=User
        fields=['username']

    def validate_username(self, username):
        if self.context['request'].user.username==username:
             raise serializers.ValidationError({'username':'This is already your username'})
        username_exists=User.objects.filter(username__iexact=username)
        if username_exists:
            raise serializers.ValidationError({'username':'This username already exists'})
        return username



class profileQuotesSerializer(serializers.ModelSerializer):
    author=serializers.CharField(source='author.username', read_only=True)
    categories = serializers.StringRelatedField(many=True)
    pub_date = serializers.DateTimeField(format='%D', read_only=True)
    
    class Meta:
        model = Quote
        fields = ['quote','author','categories','pub_date']


class UserPasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, max_length=30)
    password = serializers.CharField(required=True,label='Password:',style={'input_type': 'password'}, write_only=True,min_length=8,
    help_text="Your password must contain at least 8 characters and should not be entirely numeric.")
    confirm_password = serializers.CharField(required=True, label='Confirm password:',style={'input_type': 'password'}, write_only=True,min_length=8,)

    def validate(self, data):
        # add here additional check for password strength if needed
        if not self.context['request'].user.check_password(data.get('old_password')):
            raise serializers.ValidationError({'old_password': 'Wrong password.'})
        if data.get('confirm_password') != data.get('password'):
            raise serializers.ValidationError({'password': 'Password should match.'})
        if data.get('password').isdigit():
            raise serializers.ValidationError('Your password should contain letters!')
        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
    def create(self, validated_data):
        pass

    @property
    def data(self):
        return {'Success': "Password has been updated successfully"}