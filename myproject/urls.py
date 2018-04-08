"""myproject URL Configuration

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
"""
from django.conf.urls import include, url
from django.contrib import admin


#urlpatterns = [
#    url(r'^', include('blog.urls')),
#    url(r'^admin/', admin.site.urls),
#    url(r'^auth/', include('example.urls')),
#]


urlpatterns = [

     url(r'^', include('example.urls')),
     url(r'^admin/', admin.site.urls),

]

"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings
import blog.views
admin.autodiscover()

STATIC_ROOT = 'static/'
STATIC_URL = '/static/'



urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^blog/', include('demo.urls')),
#    url(r'^$', TemplateView.as_view(template_name='login.html')),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html')),
    url(r'^mm/', include('blog.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^static/(?P.*)$', include(blog.views.staticFileLoader.displayStaticFile)),
#    url(r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
]

