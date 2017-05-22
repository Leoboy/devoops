#coding:utf-8
from django.conf.urls import patterns, include, url
from devoops.views import updateVer,checkGp,writLogs





urlpatterns = patterns('',
    url(r'^$', checkGp(['ops','superstar'])(writLogs(updateVer)),{'appname':'superstar','apptitle':'superstar(篮球)-更新','referesh_website':''}),
    url(r'^update/$', checkGp(['ops','superstar'])(writLogs(updateVer)),{'appname':'superstar','apptitle':'superstar(篮球)-更新','referesh_website':''}),
)