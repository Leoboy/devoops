from django.conf.urls import patterns, include, url
from devoops.views import checkGp,writLogs,method_splitter,ShowUser,ShowHost,ShowGp,ShowSp,ShowSecurity,ShowIp
from ops import views









urlpatterns = patterns('',
    url(r'^user/$', method_splitter,{'GET':checkGp(['ops'])(writLogs(ShowUser.as_view())),'POST':views.user_post}),
    url(r'^showhost/$', checkGp(['ops'])(writLogs(ShowHost.as_view()))),
    url(r'^showhost/(?P<page>\d+)/$', checkGp(['ops'])(writLogs(ShowHost.as_view()))),
    url(r'^sethost/add/$',views.addhost),
    url(r'^sethost/del/(\d+)/$',views.delhost),
    url(r'^sethost/mod/(\d+)/$', views.modhost),
    url(r'^sethost/mod/$', views.modhost),
    url(r'^sethost/gameplat/$', method_splitter,{'GET':checkGp(['ops'])(writLogs(ShowGp.as_view())),'POST':views.gameplat_post}),
    url(r'^sethost/serverplat/$', method_splitter,{'GET':checkGp(['ops'])(writLogs(ShowSp.as_view())),'POST':views.serverplat_post}),
    url(r'^security/$', method_splitter,{'GET':checkGp(['ops'])(writLogs(ShowSecurity.as_view())),'POST':views.security_post}),
    url(r'^addip/$', method_splitter,{'GET':checkGp(['ops'])(writLogs(ShowIp.as_view())),'POST':views.addip_post}),
    url(r'^delip/(\d+)/$', views.delip),
    url(r'^netfilter/$', method_splitter,{'GET':views.netfilter_get,'POST':views.netfilter_post}),
    url(r'^netfilter/(?P<hostid>\d+)/$', method_splitter,{'GET':views.netfilter_get,'POST':views.netfilter_post}),


)
