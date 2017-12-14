from django.conf.urls import url

from . import views

urlpatterns = [
                    #report route
    url(r'^create/$', views.ReportCreateAPIView.as_view(), name='create'),
    url(r'^$', views.ReportListAPIView.as_view(), name='list'),
    url(r'^(?p<pk>\d+)$', views.ReportRetrieveAPIView.as_view(), name='detail'),

                    #media route
    url(r'^create/$', views.MediaCreateAPIView.as_view(), name='create'),
    url(r'^$', views.MediaListAPIView.as_view(), name='list'),
    url(r'^(?p<pk>\d+)$', views.MediaRetrieveAPIView.as_view(), name='detail'),

]