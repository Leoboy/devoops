#coding:utf-8
from django.conf.urls import patterns, include, url
from devoops.views import checkGp,writLogs,updateVer

from ymyj.views import *


#@method_decorator(checkGp(['ops','ymyj']))
#@method_decorator(writLogs)
#def dispatch(self, request,*args, **kwargs):
#    return super(UpdateView, self).dispatch(request,*args, **kwargs)

urlpatterns = patterns('',
    url(r'^$', checkGp(['ops','ymyj'])(writLogs(updateVer)),{'appname':'ymyj','apptitle':'YMYJ(三个奶爸)-更新','referesh_website':'http://y.osg.so/'}),
    url(r'update/$',checkGp(['ops','ymyj'])(writLogs(updateVer)),{'appname':'ymyj','apptitle':'YMYJ(三个奶爸)-更新','referesh_website':'http://y.osg.so/'}),
    url(r'services/$',checkGp(['ops','ymyj'])(writLogs(updateVer)),{'appname':'ymyj','apptitle':'YMYJ(三个奶爸)-更新','referesh_website':'http://y.osg.so/'})
)