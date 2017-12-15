from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$', views.WitnessCreateAPIView.as_view(), name='create'),
    url(r'^$', views.WitnessListAPIView.as_view(), name='list'),
    url(r'^(?p<pk>\d+)$', views.WitnessRetrieveAPIView.as_view(), name='detail'),

    url(r'^login/$', views.WitnessLoginAPIView.as_view(), name='login')
]