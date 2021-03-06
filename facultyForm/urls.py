"""facultyForm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include 
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='static/img/favicon.png', permanent=True)

urlpatterns = [
    #admin and Favicon urls

    url(r'^admin/', admin.site.urls),
    url(r'favicon\.ico$', favicon_view),
    #url(r'favicon\.ico$', favicon_view),
    #url(r'favicon\.ico$', favicon_view),

    #list of app urls
    url(r'^', include('recruit.urls', namespace = 'recruit')),
    url(r'^register/', include('registration.urls', namespace = 'register')),

    #Non-Teaching Recruitment urls

    # url(r'^staffrecruit/', include('staffrecruit.urls', namespace = 'staffrecruit')),
    # url(r'^staffregister/', include('staffregistration.urls', namespace = 'staffregister')),

     # password Reset urls 
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^pay/', include('payment.urls', namespace='payment')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#setting file
