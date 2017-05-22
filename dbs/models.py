#coding:utf-8
from django.db import models
from django.contrib.auth.models import User

__author__ = 'lixu'
# Create your models here.

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class ServerPlat(models.Model):
    Name=models.CharField('服务器平台',max_length=32,unique=True)
    Memo=models.CharField('备注',max_length=64,blank=True,null=True)

    def __unicode__(self):
        return self.Name

class GamePlat(models.Model):
    Name=models.CharField('游戏平台',max_length=32,unique=True)
    Memo=models.CharField('备注',max_length=64,blank=True,null=True)

    def __unicode__(self):
        return self.Name

class Department(models.Model):
    Name=models.CharField('部门',max_length=32,unique=True)
    Memo=models.CharField('备注',max_length=64,blank=True,null=True)

    def __unicode__(self):
        return self.Name

class LogAct(models.Model):
    ActName = models.CharField('事件名称',max_length=32,unique=True)
    Memo = models.CharField('备注',max_length=64)

    def __unicode__(self):
        return self.ActName


class Servers(models.Model):
    HostName=models.CharField('主机名',max_length=16,default='新服务器',unique=True)
    LoginUser=models.CharField('服务器用户',max_length=16,default='root')
    Password=models.CharField('密码',max_length=64,default='T1H3i5n#')
    Port=IntegerRangeField('SSH端口',min_value=0,max_value=65535,default=22)
    IP1=models.IPAddressField('公网IP',blank=True,null=True)
    IP2=models.IPAddressField('本地IP')
    IP3=models.IPAddressField('IP3',blank=True,null=True)
    IP4=models.IPAddressField('IP4',blank=True,null=True)
    Status=models.CharField('状态',max_length=3,default='RUN',choices=(('RUN', '运行中'), ('SUP', '待定中'),('CLS','已关机'),('DEL','已删除')))
    SID=models.CharField('服务器ID',max_length=16,blank=True,null=True)
    GPlat=models.ForeignKey(GamePlat,verbose_name='游戏平台')
    SrvPlat=models.ForeignKey(ServerPlat,verbose_name='服务器平台')
    DetailStatus=models.TextField('详细状态',blank=True,null=True)
    Memo=models.CharField('备注',max_length=64,blank=True,null=True)

    def __unicode__(self):
        return self.HostName


class Employee(models.Model):
    Euser = models.OneToOneField(User,verbose_name='用户ID')
    Name = models.CharField('用户名',max_length=24)
    #Edepartment = models.ForeignKey(Department,verbose_name='部门')
    Gplat = models.ManyToManyField(GamePlat,verbose_name='游戏平台')

    def __unicode__(self):
        return '%s %s' % (self.Euser,self.Name)

class IpGroup(models.Model):
    Name = models.CharField('IP组名',max_length=24)
    IP = models.TextField('IP地址',blank=True,null=True)

    def __unicode__(self):
        return self.Name



class Netpolicy(models.Model):
    Weight = models.IntegerField('策略权重')
    Chains =models.CharField('链表',max_length=16,default='INPUT',choices=(('INPUT','INPUT'),('OUTPUT','OUTPUT'),('FORWARD','FORWARD'),('PREROUTING','PREROUTING'),('POSTROUTING','POSTROUTING')))
    Protocol = models.CharField('网络协议',max_length=16)
    Policystat = models.TextField('协议状态',blank=True,null=True)
    Ports = models.TextField('端口列表',blank=True,null=True)
    IpGroupName = models.ForeignKey(IpGroup,verbose_name='IP组')
    Active = models.CharField('策略动作',max_length=6,choices=(('ACCEPT','ACCEPT'),('DROP','DROP'),('REJECT','REJECT'),('LOG','LOG')))
    Server=models.ForeignKey(Servers,on_delete=models.SET_NULL,verbose_name='IP策略服务器',blank=True,null=True)

    class Meta:
        unique_together=(('Weight','Server'),)

    def __unicode__(self):
        return '%s %s' % (self.Weight,self.Server)

class Roles(models.Model):
    Name=models.CharField('角色名',max_length=24,unique=True)
    DHost=models.ForeignKey(Servers,verbose_name='服务器角色',related_name='dset',max_length=64,blank=True,null=True)
    DPath=models.CharField('文件目标路径',max_length=64,blank=True,null=True)
    GPlat=models.ForeignKey(GamePlat,verbose_name='游戏平台')
    Type=models.CharField('类别',max_length=64,blank=True,null=True)
    Class=models.CharField('分类',max_length=64,blank=True,null=True)
    ExeCom=models.CharField('命令',max_length=64,blank=True,null=True)
    SHost=models.ForeignKey(Servers,verbose_name='文件源主机',blank=True,null=True,related_name='sset')
    SPath=models.CharField('文件源路径',max_length=64,blank=True,null=True)
    File=models.CharField('文件/参数',max_length=255,blank=True,null=True)
    AsRoot=models.BooleanField('AsRoot',default=False)
    Memo=models.CharField('备注',max_length=64,blank=True,null=True)

    def __unicode__(self):
        return self.Name



class Logs(models.Model):
    ActUser=models.CharField('用户ID',max_length=128,blank=True,null=True)
    ActIP=models.IPAddressField('登录IP')
    ActPlat=models.CharField('操作平台',max_length=128)
    ActMethod=models.CharField('操作方法',max_length=24)
    ActConnect=models.TextField('操作内容',blank=True,null=True)
    ActDateTime=models.DateTimeField('操作时间',auto_now_add=True, blank=True,null=True)

    def __unicode__(self):
        return '%s %s %s' % (self.ActUser,self.ActPlat,self.ActConnect)




