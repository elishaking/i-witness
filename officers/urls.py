from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^reports/$', views.reports, name='reports'),
    url(r'^report_detail/(?P<pk>[0-9]+)$', views.report_details, name='report_detail'),
]