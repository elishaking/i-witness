from django.conf.urls import url

from . import views

urlpatterns = [
    # report route
    url(r'^create/$', views.ReportCreateAPIView.as_view(), name='create'),
    url(r'^$', views.ReportListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', views.ReportRetrieveAPIView.as_view(), name='detail'),
]
