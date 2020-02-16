from django import forms
from registration.models import User



class UsernameChangeForm(forms.Form):

    error_messages = {
        # 'email_mismatch': "The two e-mail address fields do not match.",
        # 'email_inuse': "This e-mail address cannot be used. Please select a different e-mail address.",
        'username_inuse':"This username is already taken by some other user",
        'password_incorrect': "Incorrect password.",
        'username_change': "This is already your username",
    }


    current_password = forms.CharField(label="Current Password:",widget=forms.PasswordInput,required=True)
    new_username=forms.CharField(label="Change your Username:", max_length=255, required=True,
     help_text="Remember your username. It will be needed for signing in again!")
    # new_email1 = forms.EmailField(
    #     label="New E-mail Address:",
    #     max_length=254,
    #     required=True
    # )

    # new_email2 = forms.EmailField(
    #     label="Confirm New E-mail Address:",
    #     max_length=254,
    #     required=True
    # )
    field_order = ['new_username', 'current_password']
    # a call to super() is made to 
    # ensure the initialization process of the parent class (i.e. forms.ChoiceField) is made
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(UsernameChangeForm, self).__init__(*args, **kwargs)
        self.fields['new_username'].initial=self.user.username
        
    def clean(self):
        cleaned_data=super(UsernameChangeForm, self).clean()
        user_name = self.cleaned_data.get('new_username')
        if self.fields['new_username'].initial==user_name:
            raise forms.ValidationError(self.error_messages['username_change'])
        return cleaned_data
            

    def clean_current_password(self):
        """
        Validates that the password field is correct.
        """
        current_password = self.cleaned_data["current_password"]
        if not self.user.check_password(current_password):
            raise forms.ValidationError(self.error_messages['password_incorrect'], code='password_incorrect',)
        return current_password

    def clean_new_username(self):
        """
        Prevents a username that is already registered from being registered by a different user.
        """
        username1 = self.cleaned_data.get('new_username')
        username_exists=User.objects.filter(username__iexact=username1)
        if username_exists:
            raise forms.ValidationError(self.error_messages['username_inuse'], code='username_inuse',)
        return username1

    # def clean_new_email2(self):
    #     """
    #     Validates that the confirm e-mail address's match.
    #     """
    #     email1 = self.cleaned_data.get('new_email1')
    #     email2 = self.cleaned_data.get('new_email2')
    #     if email1 and email2:
    #         if email1 != email2:
    #             raise forms.ValidationError(self.error_messages['email_mismatch'], code='email_mismatch',)
    #     return email2

    def save(self, commit=True):
        self.user.username = self.cleaned_data['new_username']
        if commit:
            self.user.save()
        return self.user

class SocialUsernameChangeForm(forms.Form):

    error_messages = {
        # 'email_mismatch': "The two e-mail address fields do not match.",
        # 'email_inuse': "This e-mail address cannot be used. Please select a different e-mail address.",
        'username_inuse':"This username is already taken by some other user",
        'username_change': "This is already your username",
    }


    new_username=forms.CharField(label="Change your Username:", max_length=255, required=True,
     help_text="Remember your username. It will be needed for signing in again!")
 
   
 
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SocialUsernameChangeForm, self).__init__(*args, **kwargs)
        self.fields['new_username'].initial=user.username
        
    def clean(self):
        cleaned_data=super(SocialUsernameChangeForm, self).clean()
        user_name = self.cleaned_data.get('new_username')
        if self.fields['new_username'].initial==user_name:
            raise forms.ValidationError(self.error_messages['username_change'])
        return cleaned_data
            

    def clean_new_username(self):
        """
        Prevents a username that is already registered from being registered by a different user.
        """
        username1 = self.cleaned_data.get('new_username')
        if User.objects.filter(username__iexact=username1).count() > 0:
            raise forms.ValidationError(self.error_messages['username_inuse'], code='username_inuse',)
        return username1

    def save(self, commit=True):
        self.user.username = self.cleaned_data['new_username']
        if commit:
            self.user.save()
        return self.user