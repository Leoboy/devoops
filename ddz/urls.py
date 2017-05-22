#coding:utf-8
from django.conf.urls import patterns, include, url
from devoops.views import updateVer,checkGp,writLogs





urlpatterns = patterns('',
    url(r'^$', checkGp(['ops','ddz'])(writLogs(updateVer)),{'appname':'ddz','apptitle':'DDZ(棋乐斗地主)-更新','referesh_website':'http://cdn.platform.qile.club/'}),
    url(r'^update/$', checkGp(['ops','ddz'])(writLogs(updateVer)),{'appname':'ddz','apptitle':'DDZ(棋乐斗地主)-更新','referesh_website':'http://cdn.platform.qile.club/'}),
)