#coding:utf-8
from django.conf.urls import patterns, include, url
from devoops.views import updateVer,checkGp,writLogs





urlpatterns = patterns('',
    url(r'^$', checkGp(['ops','atm'])(writLogs(updateVer)),{'appname':'atm','apptitle':'atm(奥特曼)-更新','referesh_website':''}),
    url(r'^update/$', checkGp(['ops','atm'])(writLogs(updateVer)),{'appname':'atm','apptitle':'superstar(奥特曼)-更新','referesh_website':''}),
)