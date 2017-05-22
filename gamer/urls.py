#coding:utf-8
from django.conf.urls import patterns, include, url
from devoops.views import checkGp,writLogs,updateVer

from ymyj.views import *


#@method_decorator(checkGp(['ops','ymyj']))
#@method_decorator(writLogs)
#def dispatch(self, request,*args, **kwargs):
#    return super(UpdateView, self).dispatch(request,*args, **kwargs)

urlpatterns = patterns('',
    url(r'^$', checkGp(['ops','gamer'])(writLogs(updateVer)),{'appname':'gamer','apptitle':'Gamer(天津怪糖)-更新','referesh_website':''}),
    url(r'update/$',checkGp(['ops','gamer'])(writLogs(updateVer)),{'appname':'gamer','apptitle':'Gamer(天津怪糖)-更新','referesh_website':''}),
    url(r'services/$',checkGp(['ops','gamer'])(writLogs(updateVer)),{'appname':'game','apptitle':'Gamer(天津怪糖)-更新','referesh_website':''})
)