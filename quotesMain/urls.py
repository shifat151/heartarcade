from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from quotes import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('quotes/', include('quotes.urls')),
    path('registration/', include('registration.urls')),
    path('profile/', include('profiles.urls')),
    path('accounts/password_change/',
        auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html', 
        success_url='/'),name="password_change"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    #rest framework urls
    path('api/quote/', include('quotes.api.urls', namespace='quotes_api')),
    path('api/account/', include('registration.api.urls', namespace='registration_api')),
    path('api/profile/', include('profiles.api.urls', namespace='profiles_api')),
    path('', RedirectView.as_view(url='home/')),
             
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
