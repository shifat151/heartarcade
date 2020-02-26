from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from quotes import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('quotes/', include('quotes.urls')),
    path('registration/', include('registration.urls')),
    path('profile/', include('profiles.urls')),
    path('accounts/password_change/',
        auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html', 
        success_url='/'),name="password_change"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    #rest framweok urls
    path('api/quote/', include('quotes.api.urls', namespace='quotes_api')),
    path('api/account/', include('registration.api.urls', namespace='registration_api')),
        
        

]
