from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    url(r'^create/$', views.WitnessCreateAPIView.as_view(), name='create'),
    url(r'^$', views.WitnessListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', views.WitnessRetrieveAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit$', views.WitnessEditAPIView.as_view(), name='edit'),

    url(r'^login/$', views.WitnessLoginAPIView.as_view(), name='login'),
    url(r'^auth/token/$', obtain_jwt_token)
]