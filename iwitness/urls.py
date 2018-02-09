"""iwitness URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index),
    url(r'^privacy/$', views.privacy, name='privacy'),

    # url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^officers/', include('officers.urls', namespace='officers')),
    # url(r'^reports/', include('reports.urls', namespace='reports')),
    # url(r'^witness/', include('witness.urls', namespace='witness')),
    # url(r'^media/', include('media.urls', namespace='media')),

    url(r'^api/', include([
        url(r'^accounts/', include('accounts.api.urls')),
        url(r'^officers/', include('officers.api.urls')),
        url(r'^reports/', include('reports.api.urls')),
        url(r'^witness/', include('witness.api.urls')),
        url(r'^media/', include('media.api.urls')),
    ])),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
