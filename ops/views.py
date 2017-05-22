# coding:utf-8

import os, csv, json, datetime,sys,random,urllib,urllib2,time,base64,hmac,hashlib,re,commands
from django.shortcuts import render, render_to_response
from django.http import Http404,HttpResponseRedirect
from django.db.models import Q
from devoops.views import checkGp,writLogs


from dbs.models import *

__author__ = 'lixu'


@checkGp(['ops'])
@writLogs
def user_post(request):
    assert request.method == 'POST'
    manplat = "open"
    getfun = request.POST.get('getfun', '')

    if getfun == 'add':
        userid = request.POST.get('gameplatname', '')
        pwd1 = request.POST.get('userpwd1', '')
        pwd2 = request.POST.get('userpwd1', '')
        name = request.POST.get('username', '')
        gps = request.POST.getlist('gplat', '')

        if userid and pwd1 and pwd1 == pwd2 and name:
            user = User.objects.create_user(userid, '', pwd1)
            em = Employee(Euser=user, Name=name)
            em.save()
        else:
            raise Http404

        if em and gps:
            for gp in gps:
                g = GamePlat.objects.get(id=int(gp))
                em.Gplat.add(g)
    elif getfun == 'update':
        up_pwd1 = request.POST.get('up_pwd1', '')
        up_pwd2 = request.POST.get('up_pwd2', '')
        up_name = request.POST.get('up_name', '')
        gps = request.POST.getlist('up_gplat', '')
        uid = request.POST.get('getid', '')
        if up_pwd1 == up_pwd2 and up_pwd1 and up_name:
            em = Employee.objects.get(id=int(uid))
            em.Euser.set_password(up_pwd1)
            em.Euser.save()
            em.Name = up_name
            em.save()
            em.Gplat.clear()
            if gps:
                for gp in gps:
                    g = GamePlat.objects.get(id=int(gp))
                    em.Gplat.add(g)
        elif up_name:
            em = Employee.objects.get(id=int(uid))
            em.Name = up_name
            em.save()
            em.Gplat.clear()
            if gps:
                for gp in gps:
                    g = GamePlat.objects.get(id=int(gp))
                    em.Gplat.add(g)
    elif getfun == "del":
        uid = request.POST.get('getid', '')
        if uid:
            deluid = Employee.objects.get(id=int(uid))
            deluid.delete()
        else:
            raise Http404
    else:
        raise Http404

    users = Employee.objects.all()
    gps = GamePlat.objects.all()
    return render_to_response('user.html', locals())

@checkGp(['ops'])
@writLogs
def addhost(request):
    manplat = "open"
    addhost = "active"

    if request.method == "POST":
        hostname = request.POST.get('hostname', '')
        loginuser = request.POST.get('loginuser', '')
        pwd = request.POST.get('pwd', '')
        port = request.POST.get('port', '')
        ip1 = request.POST.get('ip1', '')
        ip2 = request.POST.get('ip2', '')
        ip3 = request.POST.get('ip3', '')
        ip4 = request.POST.get('ip4', '')
        sid = request.POST.get('sid', '')
        memo = request.POST.get('memo', '')

        status = request.POST.get('status', '')
        gplat = request.POST.get('gplat', '')
        splat = request.POST.get('splat', '')

        g_plat = GamePlat.objects.get(id=gplat)
        s_plat = ServerPlat.objects.get(id=splat)
        try:
            if hostname and loginuser and pwd and port and ip2 and sid and status and gplat and splat:
                newhost = Servers(HostName=hostname, LoginUser=loginuser, Password=pwd, Port=port, IP1=ip1, IP2=ip2,
                                  IP3=ip3, IP4=ip4, Status=status, SID=sid, GPlat=g_plat, SrvPlat=s_plat, Memo=memo)
                newhost.save()
                message = '添加主机'
                sdisplay = 'block'
        except:
            raise Http404


    gPlats = GamePlat.objects.all()
    sPlats = ServerPlat.objects.all()

    return render_to_response('addhost.html', locals())

@checkGp(['ops'])
@writLogs
def delhost(request, hostid):
    manplat = "open"
    hostlist = "active"
    try:
        dh = Servers.objects.get(id=int(hostid))
        dh.delete()
        return HttpResponseRedirect('/showhost/1/')
    except:
        raise Http404

@checkGp(['ops'])
@writLogs
def modhost(request, hostid=1):
    manplat = "open"
    modhost = "active"

    gPlats = GamePlat.objects.all()
    sPlats = ServerPlat.objects.all()

    if request.method == "POST":
        hid = request.POST.get('modsel', '')
        print hid

        hostname = request.POST.get('hostname', '')
        loginuser = request.POST.get('loginuser', '')
        pwd = request.POST.get('pwd', '')
        port = request.POST.get('port', '')
        ip1 = request.POST.get('ip1', '')
        ip2 = request.POST.get('ip2', '')
        ip3 = request.POST.get('ip3', '')
        ip4 = request.POST.get('ip4', '')
        sid = request.POST.get('sid', '')
        memo = request.POST.get('memo', '')

        status = request.POST.get('status', '')
        gplat = request.POST.get('gplat', '')
        splat = request.POST.get('splat', '')

        g_plat = GamePlat.objects.get(id=gplat)
        s_plat = ServerPlat.objects.get(id=splat)

        selhost = Servers.objects.get(id=int(hid))

        selhost.HostName = hostname
        selhost.LoginUser = loginuser
        selhost.Password = pwd
        selhost.Port = port
        selhost.IP1 = ip1
        selhost.IP2 = ip2
        selhost.IP3 = ip3
        selhost.IP4 = ip4
        selhost.Status = status
        selhost.Sid = sid
        selhost.Memo = memo
        selhost.GPlat = g_plat
        selhost.SrvPlat = s_plat
        selhost.save()
        message = '更新主机'
        sdisplay = 'block'

    hostid = int(hostid)
    sel = {}
    hosts = Servers.objects.all()
    if hostid == 1:
        host = hosts[0]
        hostid = host.id
    else:
        host = Servers.objects.get(id=hostid)
    sel[host.Status] = 'selected'

    return render_to_response('modhost.html', locals())

@checkGp(['ops'])
@writLogs
def gameplat_post(request):
    assert request.method == 'POST'
    manplat = "open"
    gameplat = 'active'
    getfun = request.POST.get('getfun', '')
    if getfun:
        if getfun == "add":
            gameplatname = request.POST.get('gameplatname', '')
            gameplatmemo = request.POST.get('gameplatmemo', '')
            if gameplatname:
                newgp = GamePlat(Name=gameplatname, Memo=gameplatmemo)
                newgp.save()
                message = '添加游戏平台'
                sdisplay = 'block'
            else:
                raise Http404
        elif getfun == "update":
            gameplatname = request.POST.get('up_gpname', '')
            gameplatmemo = request.POST.get('up_gpmemo', '')
            gameplatid = request.POST.get('getid', '')
            if gameplatname:
                print gameplatid
                print gameplatname
                upgp = GamePlat.objects.get(id=int(gameplatid))
                upgp.Name = gameplatname
                upgp.Memo = gameplatmemo
                upgp.save()
                message = '修改游戏平台'
                sdisplay = 'block'
            else:
                raise Http404
        elif getfun == "del":
            gameplatid = request.POST.get('getid', '')
            if gameplatid:
                delgp = GamePlat.objects.get(id=int(gameplatid))
                delgp.delete()
                message = '删除游戏平台'
                sdisplay = 'block'
            else:
                raise Http404
    else:
        raise Http404
    gps = GamePlat.objects.all()
    return render_to_response('gameplat.html', locals())

@checkGp(['ops'])
@writLogs
def serverplat_post(request):
    assert request.method == 'POST'
    serverplat = 'active'
    manplat = "open"
    getfun = request.POST.get('getfun', '')
    if getfun:
        if getfun == "add":
            gameplatname = request.POST.get('gameplatname', '')
            gameplatmemo = request.POST.get('gameplatmemo', '')
            if gameplatname:
                newgp = ServerPlat(Name=gameplatname, Memo=gameplatmemo)
                newgp.save()
                message = '添加服务器平台'
                sdisplay = 'block'
            else:
                raise Http404
        elif getfun == "update":
            gameplatname = request.POST.get('up_gpname', '')
            gameplatmemo = request.POST.get('up_gpmemo', '')
            gameplatid = request.POST.get('getid', '')
            if gameplatname:
                print gameplatid
                print gameplatname
                upgp = ServerPlat.objects.get(id=int(gameplatid))
                upgp.Name = gameplatname
                upgp.Memo = gameplatmemo
                upgp.save()
                message = '修改服务器平台'
                sdisplay = 'block'
            else:
                raise Http404
        elif getfun == "del":
            gameplatid = request.POST.get('getid', '')
            if gameplatid:
                delgp = ServerPlat.objects.get(id=int(gameplatid))
                delgp.delete()
                message = '删除服务器平台'
                sdisplay = 'block'
            else:
                raise Http404
    else:
        raise Http404
    sps = ServerPlat.objects.all()
    return render_to_response('serverplat.html', locals())

@checkGp(['ops'])
@writLogs
def security_post(request):
    assert request.method == 'POST'
    manplat = "open"
    security = "active"
    allhost = request.POST.get('ports', '')
    host = request.POST.getlist('port', '')
    if allhost:
        hosts = Servers.objects.filter(~Q(Status='DEL'))
    else:
        hosts = Servers.objects.filter(~Q(Status='DEL'), id__in=host)
    for host in hosts:
        (stat, output) = commands.getstatusoutput("/usr/bin/sudo /usr/bin/nmap -sS -T5 -p 1-65535 %s" % host.IP2)
        host.DetailStatus = output
        if 'down' in host.DetailStatus:
            host.Status = 'SUP'
        host.save()
    hosts = Servers.objects.filter(~Q(Status='DEL'))
    return render_to_response('security_net.html', locals())

@checkGp(['ops'])
@writLogs
def addip_post(request):
    assert request.method == 'POST'
    manplat = "open"
    addip = "active"
    ip = ""
    ipgroupname = request.POST.get('ipgroupname', '')
    multiip = request.POST.getlist('multipleSelect2', '')
    customip = request.POST.get('customip', '')
    if multiip:
        for mip in multiip:
            srv = Servers.objects.get(id=int(mip))
            ip = ip + ' ' + srv.IP1 + ' ' + srv.IP2
    if customip:
        ip = ip + ' ' + customip

    newipg = IpGroup(Name=ipgroupname, IP=ip)
    newipg.save()

    hosts = Servers.objects.filter(Status='RUN')
    ips = IpGroup.objects.all()

    return render_to_response('addip.html', locals())

@checkGp(['ops'])
@writLogs
def delip(request, id):
    manplat = "open"
    addip = "active"
    hosts = Servers.objects.filter(Status='RUN')
    delip = IpGroup.objects.get(id=int(id))
    delip.delete()
    ips = IpGroup.objects.all()
    return render_to_response('addip.html', locals())

@checkGp(['ops'])
@writLogs
def netfilter_get(request, hostid=0):
    assert request.method == 'GET'
    manplat = "open"
    netfilter = "active"
    hostid = int(hostid)
    hosts = Servers.objects.filter(Status='RUN')
    if int(hostid) == 0:
        host = hosts[0]
    else:
        host = Servers.objects.get(id=hostid)
    portline = host.DetailStatus
    if portline:
        ports = re.findall(r"(^\d+)", portline, re.M)
    # print ports
    ips = IpGroup.objects.all()

    policys = Netpolicy.objects.filter(Server=host)

    return render_to_response('netfilter.html', locals())

@checkGp(['ops'])
@writLogs
def netfilter_post(request, hostid=0):
    assert request.method == 'POST'
    manplat = "open"
    netfilter = "active"

    ports = request.POST.getlist('port', [])
    ophost = request.POST.get('applypolicy', '')
    chains = request.POST.get('chains', '')
    protocol = request.POST.get('protocol', '')
    ip = request.POST.get('ip', '')
    jump = request.POST.get('jump', '')
    custport = request.POST.get('custport', '')
    netfilterfun = request.POST.get('netfilterfun', '')
    sdisplay = ''

    if custport:
        ports.append(custport)

    port = ' '.join(ports)
    netHost = Servers.objects.get(id=int(ophost))

    if netfilterfun == 'add':
        if protocol == 'all':
            if ophost and chains and protocol and ip and jump:
                ipgroup = IpGroup.objects.get(id=int(ip))
                weight = Netpolicy.objects.filter(Server=netHost).count() + 1
                newNP = Netpolicy(Weight=weight, Chains=chains, Protocol=protocol, IpGroupName=ipgroup, Active=jump,
                                  Server=netHost)
                newNP.save()
        else:
            if ports and ophost and chains and protocol and ip and jump:
                ipgroup = IpGroup.objects.get(id=int(ip))
                weight = Netpolicy.objects.filter(Server=netHost).count() + 1

                newNP = Netpolicy(Weight=weight, Chains=chains, Protocol=protocol, Ports=port, IpGroupName=ipgroup,
                                  Active=jump, Server=netHost)
                newNP.save()
    elif netfilterfun == 'apply':
        now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        filename = now + '_' + netHost.IP2 + '.sh'
        fwfile = open('/tmp/' + filename, 'a+')

        fw = ['/sbin/iptables -F ' + chains + '\n']
        fw.append('/sbin/iptables -P ' + chains + ' ACCEPT\n')
        # default add office ip(116.228.9.26) access.
        fw.append('/sbin/iptables -A ' + chains + ' -s 116.228.9.26 -j ACCEPT\n')
        fw.append('/sbin/iptables -A ' + chains + ' -s 127.0.0.1 -j ACCEPT\n')
        fw.append('/sbin/iptables -A ' + chains + ' -i lo -j ACCEPT\n')
        fw.append('/sbin/iptables -A ' + chains + ' -m state --state ESTABLISHED,RELATED -j ACCEPT\n')
        fwfile.writelines(fw)
        rules = Netpolicy.objects.filter(Server=netHost).order_by('Weight')
        for rule in rules:
            if rule.Ports:
                port = rule.Ports.split()
                ips = rule.IpGroupName.IP.split()
                for p in port:
                    for ip in ips:
                        tmplist = ('/sbin/iptables -A %s -s %s -p %s --dport %s -j %s\n') % (
                        rule.Chains, ip, rule.Protocol, p, rule.Active)
                        fwfile.write(tmplist)
            else:
                ips = rule.IpGroupName.IP.split()
                for ip in ips:
                    tmplist = ('/sbin/iptables -A %s -s %s -j %s\n') % (rule.Chains, ip, rule.Active)
                    fwfile.write(tmplist)

        fwfile.write('/sbin/iptables-save >/etc/sysconfig/iptables')
        fwfile.write('/sbin/chkconfig iptables on')
        fwfile.close()

        # transport script file
        tfile = paramiko.Transport((netHost.IP2, int(netHost.Port)))
        tfile.connect(username=netHost.LoginUser, password=netHost.Password)
        sftp = paramiko.SFTPClient.from_transport(tfile)
        sftp.put('/tmp/' + filename, '/tmp/' + filename)
        sftp.close()

        # exec script file
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=netHost.IP2, port=netHost.Port, username=netHost.LoginUser, password=netHost.Password)
        stdin, stdout, stderr = ssh.exec_command('/bin/sh /tmp/' + filename)
        msg, err = stdout.read(), stderr.read()
        ssh.close()
        sdisplay = 'block'
    elif re.match(r'[+-]?\d+$', netfilterfun):

        delpolicy = Netpolicy.objects.get(Weight=int(netfilterfun), Server=netHost)
        delpolicy.delete()
        Netpolicy.objects.filter(Weight__gt=int(netfilterfun), Server=netHost).update(Weight=F('Weight') - 1)

    if not hostid:
        url = request.get_full_path() + str(ophost) + '/'
    else:
        url = request.get_full_path()
    return HttpResponseRedirect(url)