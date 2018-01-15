from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AccountListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', views.AccountRetrieveAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit$', views.AccountEditAPIView.as_view(), name='edit'),
]
