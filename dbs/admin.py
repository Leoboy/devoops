#coding:utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from dbs.models import *

__author__ = 'lixu'

class ServerPlatAdmin(admin.ModelAdmin):
    list_display = ('Name','Memo')
    search_fields = ('Name','Memo')

class GamePlatAdmin(admin.ModelAdmin):
    list_display = ('Name','Memo')
    search_fields = ('Name','Memo')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('Name','Memo')
    search_fields = ('Name','Memo')

class LogActAdmin(admin.ModelAdmin):
    list_display = ('ActName','Memo')
    search_fields = ('ActName','Memo')

class ServersAdmin(admin.ModelAdmin):
    list_display = ('HostName','IP1','IP2','GetGPlat','GetSrvPlat','Status','Memo')
    search_fields = ('HostName','Port','IP1','IP2','IP3','IP4','Status','Memo')
    ordering = ('id',)

    def GetGPlat(self,obj):
        return obj.GPlat

    def GetSrvPlat(self,obj):
        return obj.SrvPlat

    GetGPlat.short_description = '游戏平台'
    GetSrvPlat.short_description = '服务器平台'


class IpGroupAdmin(admin.ModelAdmin):
    list_display = ('Name','IP')
    search_fields = ('Name','IP')
    ordering = ('Name',)

class NetpolicyAdmin(admin.ModelAdmin):
    list_display = ('Weight','GetServer','Ports','GetIpGroupName','Active')
    ordering = ('Weight',)

    def GetServer(self,obj):
        return obj.Server

    def GetIpGroupName(self,obj):
        return obj.IpGroupName

    GetServer.short_description = 'IP策略服务器'
    GetIpGroupName.short_description = 'IP组'

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('GetEuser','Name','GetGplat')
    search_fields = ('Euser','Name','Gplat')
    ordering = ('Euser','Name')

    def GetEuser(self,obj):
        return obj.Euser

    def GetGplat(self,obj):
        return '|'.join([g.Name + ' ' + g.Memo for g in obj.Gplat.all()])

    GetGplat.short_description = '游戏平台'
    GetEuser.short_description = '用户ID'

class LogsAdmin(admin.ModelAdmin):
    list_display = ('ActUser','ActIP','ActPlat','ActMethod','ActConnect','ActDateTime')
    search_fields = ('ActUser','ActIP','ActPlat','ActMethod','ActConnect','ActDateTime')
    ordering = ('-ActDateTime',)
    list_filter = ('ActDateTime',)



class RolesAdmin(admin.ModelAdmin):
    list_display = ('Name','GetGPlat','Type','Class','ExeCom','GetDHost','DPath','GetSHost','SPath','AsRoot','Memo')
    search_fields = ('Name',)

    def GetDHost(self,obj):
        return obj.DHost
    def GetSHost(self,obj):
        return obj.SHost
    def GetGPlat(self,obj):
        return obj.GPlat

    GetDHost.short_description = '服务器'
    GetSHost.short_description = '源服务器'
    GetGPlat.short_description = '游戏平台'

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'



# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (EmployeeInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(ServerPlat,ServerPlatAdmin)
admin.site.register(GamePlat,GamePlatAdmin)
#admin.site.register(Department,DepartmentAdmin)
admin.site.register(LogAct,LogActAdmin)
admin.site.register(Servers,ServersAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(IpGroup,IpGroupAdmin)
admin.site.register(Netpolicy,NetpolicyAdmin)
admin.site.register(Roles,RolesAdmin)
admin.site.register(Logs,LogsAdmin)

