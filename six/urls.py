#coding:utf-8
from django.conf.urls import patterns, include, url
from devoops.views import checkGp,writLogs,updateVer

from ymyj.views import *


#@method_decorator(checkGp(['ops','ymyj']))
#@method_decorator(writLogs)
#def dispatch(self, request,*args, **kwargs):
#    return super(UpdateView, self).dispatch(request,*args, **kwargs)

urlpatterns = patterns('',
    url(r'^$', checkGp(['ops','six'])(writLogs(updateVer)),{'appname':'six','apptitle':'SIX(火线突击)-更新','referesh_website':''}),
    url(r'update/$',checkGp(['ops','six'])(writLogs(updateVer)),{'appname':'six','apptitle':'SIX(火线突击)-更新','referesh_website':''}),
    url(r'services/$',checkGp(['ops','six'])(writLogs(updateVer)),{'appname':'six','apptitle':'SIX(火线突击)-更新','referesh_website':''})
)