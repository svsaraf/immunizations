from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'immunizations.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'dashboard.views.home', name='dasboard_home'),
    url(r'^admin/', include(admin.site.urls)),
)
