from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'immunizations.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'dashboard.views.home', name='dasboard_home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add/', 'dashboard.views.addimmunizations', name='dashboard_addimmunizations'),
    url(r'^patients/', 'dashboard.views.addpatients', name='dashboard_addpatients'),
    url(r'^patient/(?P<patientid>[0-9]+)/$', 'dashboard.views.patientview', name='dashboard_patientview'),
    url(r'^addfromapi/', 'dashboard.views.addfromapi', name='dashboard_addfromapi'),
    url(r'^addimmuno/', 'dashboard.views.addimmuno', name='dashboard_addimmuno'),
)
