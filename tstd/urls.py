#coding:utf-8
from django.conf.urls import patterns, include, url
from devoops.views import updateVer,checkGp,writLogs





urlpatterns = patterns('',
    url(r'^$', checkGp(['ops','tstd'])(writLogs(updateVer)),{'appname':'tstd','apptitle':'TSTD(三国)-更新','referesh_website':''}),
    url(r'^update/$', checkGp(['ops','tstd'])(writLogs(updateVer)),{'appname':'tstd','apptitle':'TSTD(三国)-更新','referesh_website':''}),
)