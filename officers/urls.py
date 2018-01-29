from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^reports/$', views.reports, name='reports'),
    url(r'^report_detail/$', views.reports, name='report_detail'),
]