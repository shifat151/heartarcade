from django.shortcuts import render,redirect, get_object_or_404
from quotes.models import Quote
from registration.models import User
from . forms import UsernameChangeForm, SocialUsernameChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def profile(request, user_id):
    # unslug=username_slug.replace('-', ' ')
    id=str(user_id)
    profile=User.objects.get(pk=id)
    profile_quotes=Quote.objects.filter(author=profile)
    return render(request, 'profiles/profile.html', {'profile':profile,'quotes': profile_quotes, 'proStatus':'active'})

@login_required()
def editProfile(request):
    # user_email=request.user.email
    if request.method == 'GET':
        form = UsernameChangeForm(user=request.user)
        return render(request, 'profiles/editProfile.html', {'form': form,'proStatus':'active'})
    elif request.method == 'POST':
        form = UsernameChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'username updated successfully.')
            return redirect('profile',user_id=request.user.id)
        else:
            return render(request, 'profiles/editProfile.html',{'form':form,'proStatus':'active'})

@login_required()
def editSocialProfile(request):
    # user_email=request.user.email
    if request.method == 'GET':
        form = SocialUsernameChangeForm(user=request.user)
        return render(request, 'profiles/editSocialProfile.html', {'form': form,'proStatus':'active'})
    elif request.method == 'POST':
        form = SocialUsernameChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'username updated successfully.')
            return redirect('profile',user_id=request.user.id)
        else:
            return render(request, 'profiles/editSocialProfile.html',{'form':form, 'proStatus':'active'})

@login_required
def showProfile(request, slugifyUsername):
    unslugged=get_object_or_404(User, slugged_username=slugifyUsername)
    publicProfile=User.objects.get(username=unslugged)
    profile_quotes=Quote.objects.filter(author=publicProfile)
    return render(request, 'profiles/showProfile.html',{'profile':publicProfile,'quotes': profile_quotes})
