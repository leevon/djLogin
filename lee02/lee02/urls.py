from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lee02.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^lee02/login/$', 'lee02.online.views.login'),
    url(r'^lee02/index/$', 'lee02.online.views.index'),
    url(r'^lee02/logout/$', 'lee02.online.views.logout'),
)
