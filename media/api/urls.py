from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$', views.MediaCreateAPIView.as_view(), name='create'),
    url(r'^$', views.MediaListAPIView.as_view(), name='list'),
    # url(r'^(?P<pk>\d+)$', views.WitnessRetrieveAPIView.as_view(), name='detail'),
]
