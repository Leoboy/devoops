from django.conf.urls import patterns, include, url
from django.contrib import admin
from devoops import views

urlpatterns = patterns('',

    url(r'^$', 'devoops.views.home', name='home'),
    url(r'^datainit/([\w\.]+)', 'devoops.views.datainit'),
    url(r'^login/$',views.login),
    url(r'^profile/$', 'devoops.views.profile'),
    url(r'^logout/$', 'devoops.views.logout'),
    url(r'^check/(\w+)/$', views.check),
    url(r'^mytest/$', 'devoops.views.mytest'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^ddz/',include('ddz.urls')),
    url(r'^ymyj/',include('ymyj.urls')),
    url(r'^ops/',include('ops.urls')),
    url(r'^tstd/',include('tstd.urls')),
    url(r'^superstar/',include('superstar.urls')),
    url(r'^atm/',include('atm.urls')),
    url(r'^six/',include('six.urls')),
    url(r'^gamer/',include('gamer.urls')),
)
