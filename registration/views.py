from django.shortcuts import render,redirect
from .forms import SignupForm
# from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import get_user_model


def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            User = get_user_model()
            user = User.objects.create_user(form.cleaned_data['username'],
            form.cleaned_data['email'], form.cleaned_data['password'])
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            return render(request, 'registration/signup.html',{'form':form})
    else:
        form=SignupForm()
        return render(request, 'registration/signup.html',{'form':form})
