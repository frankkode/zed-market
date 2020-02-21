"""zed_market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import ( 
    index,
    about_us,
    ad_listing,
    ad_list_view,
    blog,
    category,
    contact_us,
    dashboad_archived_ads,
    dashboad_favourit_ads,
    dashboad_my_ads,
    dashboad_pending_ads,
    dashboad,
    login,
    package,
    register,
    single_blog,
    single,
    store,
    terms_condition,
    user_profile,
    )   


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog),
    path('about_us/', about_us),
    path('ad_listing/', ad_listing),
    path('ad_list_view/', ad_list_view),
    path('category/', category),
    path('contact_us/', contact_us),
    path('dashboad_archived_ads/', dashboad_archived_ads),
    path('dashboad/', dashboad),
    path('dashboad_favourit_ads/', dashboad_favourit_ads),
    path('dashboad_my_ads/', dashboad_my_ads),
    path('dashboad_pending_ads/', dashboad_pending_ads),
    path('login/', login),
    path('package/', package),
    path('register/', register),
    path('single_blog/', single_blog),
    path('single/', single),
    path('store/', store),
    path('terms_condition/', terms_condition),
    path('user_profile/', user_profile),
    
    ]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)