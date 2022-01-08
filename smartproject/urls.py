"""smartproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from django_registration.backends.one_step.views import RegistrationView
# from django.contrib.auth import views 
from smartapp import views as smartapp_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('smartapp.urls')),
    # path('accounts/register/', RegistrationView.as_view(success_url='/create_profile'),
    # name='django_registration_register'),
    # path('accounts/', include('django_registration.backends.one_step.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('logout/', views.logout_then_login, name='logout'),
    # path('income/', include('userincome.urls')),
    
    path('', include('smartapp.urls')),
     path('expenses/', include('expenses.urls')),
    # path('authentication/', include('authentication.urls')),
    path('preferences/', include('userpreferences.urls')),
    path('income/', include('userincome.urls')),
    path('admin/', admin.site.urls),
    path('accounts/register/',smartapp_views.register, name='register'),
    path('accounts/login/',auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
   
   
]
