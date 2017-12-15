from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$', views.OfficerCreateAPIView.as_view(), name='create'),
    url(r'^$', views.OfficerListAPIView.as_view(), name='list'),
    url(r'^(?p<pk>\d+)$', views.OfficerRetrieveAPIView.as_view(), name='detail'),

    url(r'^login/$', views.OfficerLoginAPIView.as_view(), name='login'),
]