# coding:utf-8

import os, csv, json, datetime,sys,random,urllib,urllib2,time,base64,hmac,hashlib,re,commands
import paramiko
from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User, Permission
from django.db.models import Q, F
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.views.generic.base import TemplateView


from dbs.models import *

__author__ = 'lixu'


def check(request, MName):
    dbs = {'gp': [GamePlat, 'Name'], 'sp': [ServerPlat, 'Name'], 'user': [User, "username"]}
    val = request.POST.get("name", '')
    objNumber = dbs[MName][0].objects.filter(**{dbs[MName][1]: val}).exists()

    if objNumber:
        pTxt = '已存在的值，请重新输入！'
    else:
        pTxt = ''

    return HttpResponse(json.dumps({'msg': pTxt}))


def checkGp(gp):
    def handle_myview(myview):
        def handle_args(request,*args,**kwargs):
            if request.user.is_authenticated():
                em = Employee.objects.get(Euser=request.user)

                for g in em.Gplat.all():
                    if g.Name in gp:
                        return myview(request,*args,**kwargs)
                else:
                    return render_to_response('nopermission.html', locals())
            else:
                return HttpResponseRedirect('/login/')
        return handle_args
    return handle_myview

def writLogs(myview):
    def handle_args(request,*args,**kwargs):
        if request.user.is_authenticated():
            username=request.user.username
        else:
            username=''
        ip=request.META['REMOTE_ADDR']
        method=[request.method]
        connect=[]
        if request.method=='GET':
            connect.extend(request.GET.lists())
        elif request.method=='POST':
            connect.extend(request.POST.lists())


        if args:
            connect.extend(args)
        if kwargs:
            connect.append(kwargs)
        ActPlat=[myview.__name__]
        ActPlat.append(request.get_full_path())
        log=Logs(ActUser=username,ActIP=ip,ActPlat=ActPlat,ActMethod=method,ActConnect=connect)
        log.save()
        return myview(request,*args,**kwargs)
    return handle_args

def updateVer(request,appname=None,apptitle=None,referesh_website=None):
    proplat='open'
    updatefile='active'
    if request.method == 'POST':
        names=request.POST.getlist('port','')
        result=[]
        if names:

            for name in names:
                r=Roles.objects.get(Name=name)

                if r.SHost:
                    if r.DHost.SrvPlat.Name == "qcloud":

                        sip=r.SHost.IP2
                        dip=r.DHost.IP2
                    else:
                        sip = r.SHost.IP1
                        dip = r.DHost.IP1
                    if r.Type=='upcdn':
                        cdnupdate=CdnUpdate(sip,r.SPath,r.DPath,referesh_website)
                        cdnupdate.refershcdn()
                        output=cdnupdate.result
                        result.extend(output)
                    else:
                        (stat, output) = commands.getstatusoutput("%s %s:%s%s %s:%s " % (r.ExeCom,sip,r.SPath,r.File,dip,r.DPath))
                        result.append(output)
                else:
                    if r.DHost.SrvPlat.Name == "qcloud":
                        dip=r.DHost.IP2
                    else:
                        dip=r.DHost.IP1
                    (stat, output) = commands.getstatusoutput("%s %s -t %s%s " % (r.ExeCom,dip,r.DPath,r.File))
                    result.append(output)
        else:
            raise Http404

    gp=GamePlat.objects.get(Name=appname)
    rols=Roles.objects.filter(GPlat=gp).filter(Class='updatefile').order_by('Type')

    #types=Roles.objects.filter(GPlat=gp).values('Type').annotate(n=models.Count("pk"))
    #types=Roles.objects.filter(GPlat=gp).values('Type')
    #myclass=[]

    #if types:
    #    for index, type in enumerate(types):
    #        if index % 2:
    #            for x in range(type['n']):
    #                myclass.append('danger')
    #        else:
    #            for x in range(type['n']):
    #                myclass.append('success')

    #myrols=zip(rols,myclass)

    return render_to_response('update.html',locals())

def method_splitter(request, *args, **kwargs):
    get_view = kwargs.pop('GET', None)
    post_view = kwargs.pop('POST', None)
    if request.method == 'GET' and get_view is not None:
        return get_view(request, *args, **kwargs)
    elif request.method == 'POST' and post_view is not None:
        return post_view(request, *args, **kwargs)
    raise Http404

def login(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return render_to_response('index.html', locals())
    else:
        if request.user.is_authenticated():
            return render_to_response('index.html', locals())
    return render_to_response('sign-in.html')

@login_required(login_url='/login/')
@writLogs
def home(request):
    return render_to_response('index.html',locals())


@login_required(login_url='/login/')
def datainit(request, file):
    sdisplay = "none"
    edisplay = "none"
    ssource = ""
    esource = ""
    data = []

    if file == "submit" and request.method == "POST":
        module_dir = os.path.dirname(__file__)
        file = request.POST.get('file', '')
        file_path = os.path.join(module_dir, file)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as csvfile:
                spamreader = csv.reader(csvfile)
                for row in spamreader:
                    data.append(row)
            for da in data[20:]:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                sp = ServerPlat.objects.get(id=1)

                gp = GamePlat.objects.get(id=2)
                try:
                    ssh.connect(hostname=da[3], username='root', password='longUGm@0814')
                except Exception, e:
                    ssh.connect(hostname=da[3], username='root', password='T1H3i5n#')

                stdin, stdout, stderr = ssh.exec_command('hostname')

                d = Servers(HostName=stdout.read().strip(),
                            LoginUser='root',
                            Password='longUGm@0814',
                            Port=22,
                            IP1=da[3],
                            IP2=da[4],
                            SID=da[0],
                            GPlat=gp,
                            SrvPlat=sp,
                            Memo=da[1])
                d.save()


                # print stdout.read().strip()
                ssh.close()

    else:
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, file)
        print file_path
        if os.path.exists(file_path):
            with open(file_path, 'rb') as csvfile:
                spamreader = csv.reader(csvfile)
                for row in spamreader:
                    data.append(row)
                    # print '* '.join(row)
        else:
            raise Http404
            # data=json.dumps(data, ensure_ascii=False)

    return render_to_response('initdata.html', locals())

@login_required(login_url='/login/')
@writLogs
def profile(request):
    pro = "active"
    my = Employee.objects.get(Euser=request.user)
    result={}
    if request.method == 'POST':

        oldpwd=request.POST.get('userpwd0','')
        pwd1=request.POST.get('userpwd1','')
        pwd2=request.POST.get('userpwd2','')
        username=request.POST.get('username','')
        user = auth.authenticate(username=request.user.username, password=oldpwd)
        if user is not None and user.is_active:
            if username:
                user.employee.Name=username
                user.employee.save()
                result['success']='success'
                result['error']=''
            if pwd1!='' and pwd1==pwd2 and len(pwd1) > 5:
                user.set_password(pwd1)
                user.save()
            else:
                result['error']=u'新密码不匹配或长度不足6位！'
                result['success']=''

            my = Employee.objects.get(Euser=request.user)
        else:
            result['error']=u'原密码不正确！'
            result['success']=''
    return render_to_response('profile.html',locals())


def logout(request):
    auth.logout(request)
    return render_to_response('sign-in.html')

class ShowUser(TemplateView):
    template_name = 'user.html'

    def get_context_data(self, **kwargs):
        context = super(ShowUser, self).get_context_data(**kwargs)

        context['manplat']='open'

        context['request']=self.request

        users = Employee.objects.all()
        gps = GamePlat.objects.all()
        context['users']=users
        context['gps']=gps
        return context

class ShowHost(TemplateView):
    template_name = 'showhost.html'

    def get_context_data(self,page=1, **kwargs):
        context = super(ShowHost, self).get_context_data(**kwargs)
        context['request']=self.request
        context['manplat']="open"
        context['hostlist']="active"

        pageitem = 10
        items = Servers.objects.all().count()
        if items % pageitem == 0:
            pagenum = items / pageitem
        else:
            pagenum = items / pageitem + 1
        pagenum_range = range(1, pagenum + 1)

        page = int(page)
        #limitmin = (page - 1) * pageitem
        #limitmax = page * pageitem - 1
        hosts = Servers.objects.all()[(page - 1) * pageitem:page * pageitem]

        context['hosts']=hosts
        context['pagenum_range']=pagenum_range
        return context

class ShowGp(TemplateView):
    template_name = 'gameplat.html'

    def get_context_data(self, **kwargs):
        context = super(ShowGp,self).get_context_data(**kwargs)
        context['request']=self.request
        context['manplat']="open"
        context['gameplat']="active"
        gps = GamePlat.objects.all()
        context['gps']=gps
        return context

class ShowSp(TemplateView):
    template_name = 'serverplat.html'

    def get_context_data(self, **kwargs):
        context = super(ShowSp,self).get_context_data(**kwargs)
        context['request']=self.request
        context['manplat']="open"
        context['serverplat']="active"
        sps = ServerPlat.objects.all()
        context['sps']=sps
        return context

class ShowSecurity(TemplateView):
    template_name = 'security_net.html'

    def get_context_data(self, **kwargs):
        context = super(ShowSecurity,self).get_context_data(**kwargs)
        context['request']=self.request
        context['manplat'] = "open"
        context['security'] = "active"
        hosts = Servers.objects.filter(~Q(Status='DEL'))
        context['hosts']=hosts
        return context

class ShowIp(TemplateView):
    template_name = 'addip.html'

    def get_context_data(self, **kwargs):
        context = super(ShowIp,self).get_context_data(**kwargs)
        context['request']=self.request
        context['manplat'] = "open"
        context['addip'] = "active"
        hosts = Servers.objects.filter(Status='RUN')
        ips = IpGroup.objects.all()
        context['hosts']=hosts
        context['ips']=ips
        return context

class UcloudCdnUpdate():

    public_key  = '3OYbxh/2sPhAc3jFeKAlNGTBvX8edZwUZpRtb7YqRlMRculWHPaiqA=='
    private_key = 'eea8e705ffa6e0dbd0e1985173bb28d3e2aaa9e3'
    DomainId="ucdn-0tm25f"
    Url="http://update.idfamenetwork.com/"

    def __init__(self,IP,SPATH,DPATH,REFERSH_URL):
        self.IP=IP
        self.SPATH=SPATH
        self.DPATH=DPATH
        self.REFERSH_URL=REFERSH_URL
        self.result=[]
        self.urls=[]
        self.dirs=[]

    def _uprsync(self):
        cmd="/usr/bin/rsync -avz --exclude-from=%s/exclude.list %s:%s %s" %(self.DPATH,self.IP,self.SPATH,self.DPATH)
        (status,output) = commands.getstatusoutput(cmd)
        lines=output.split('\n')
        lines=lines[1:-2]
        line_re = re.compile(r'^\s*$')
        re_dir = re.compile(r'.*/$')
        for line in lines:
            if not line_re.match(line):
                if re_dir.match(line):
                    self.dirs.append(self.REFERSH_URL+line)
                else:
                    self.urls.append(self.REFERSH_URL+line)

    def _verfy_ac(private_key, params):
        """UCLOUD 实现签名"""
        items=params.items()
        # 请求参数串
        items.sort()
        # 将参数串排序

        params_data = "";
        for key, value in items:
            params_data = params_data + str(key) + str(value)
        params_data = params_data + private_key

        sign = hashlib.sha1()
        sign.update(params_data)
        signature = sign.hexdigest()

        return signature

class CdnUpdate():
    req_interface='cdn.api.qcloud.com/v2/index.php'
    secret_id='AKIDp6wH6LZNNkkBJp5dreXASNUtRRqeJsXe'
    secret_key='0AgTq4aPuFouNoNGz8p7nlcjdrMulw3T'



    def __init__(self,IP,SPATH,DPATH,REFERSH_URL):
        self.IP=IP
        self.SPATH=SPATH
        self.DPATH=DPATH
        self.REFERSH_URL=REFERSH_URL
        self.result=[]
        self.urls=[]

    def _uprsync(self):
        cmd="/usr/bin/rsync -avz --exclude-from=%s/exclude.list %s:%s %s" %(self.DPATH,self.IP,self.SPATH,self.DPATH)
        (status,output) = commands.getstatusoutput(cmd)
        lines=output.split('\n')
        lines=lines[1:-3]
        re_dir = re.compile(r'.*/$')
        for line in lines:
            if not re_dir.match(line):
                self.urls.append(self.REFERSH_URL+line)

    def _referesh_urls(self):
        """ 腾讯云CDN文件更新后，刷新更新文件的url（url可含参数），以达到快速同步文件到CDN节点的效果
        此为python代码实现（测试 python 2.6 可用）"""
        urlargs = [("Action","RefreshCdnUrl"),("Nonce",random.randint(1025,65535)),("SecretId",self.secret_id),("Timestamp",int(time.time()))]

        url_idx = 0
        for url in self.urls:
            urlargs.append(("urls."+str(url_idx),url))
            url_idx +=1

        #sorted(urlargs, key=lambda urlargs:urlargs[0])

        urlargs_pairs = []
        for urla in urlargs:
            urlargs_pairs.append(("%s=%s") % (urla[0],urla[1]))

        urlargs_str='&'.join(urlargs_pairs)

        string_to_sign = 'GET' + self.req_interface + '?' + urlargs_str
        #print string_to_sign
        #signature = urllib.quote(base64.b64encode(hmac.new(secret_key, string_to_sign, digestmod=hashlib.sha1).hexdigest()))
        signature = hmac.new(self.secret_key, string_to_sign, digestmod=hashlib.sha1).digest().encode('base64').rstrip()
        #print 'signature=%s' % signature

        urlargs.append(('Signature',signature))
        #sorted(urlargs, key=lambda urlargs:urlargs[0])
        urlargs_pairs = []
        for urla in urlargs:
            if urla[0]=='Signature':
                urlargs_pairs.append(("%s=%s") % (urla[0],urllib.quote(urla[1])))
            else:
                urlargs_pairs.append(("%s=%s") % (urla[0],urla[1]))

        #sorted(urlargs_pairs, key=lambda urlargs_pairs:urlargs_pairs[0])

        urlargs_str='&'.join(urlargs_pairs)
        req_url = 'https://%s?%s' % (self.req_interface,urlargs_str)
        #print 'req_url=%s' % req_url
        self.result.extend(self.urls)
        req = urllib2.urlopen(req_url)
        #result= req.read()
        #print result

        self.result.append(req.read())

    def refershcdn(self):
        self._uprsync()
        if self.urls:
            self._referesh_urls()
        else:
            self.result.append('文件末发生变！')

class UpdateVer(TemplateView):
    appname=''
    apptitle=''
    referesh_website=''
    template_name = 'update.html'
    result=[]

    def get_context_data(self, **kwargs):
        context = super(UpdateVer, self).get_context_data(**kwargs)

        context['proplat']='open'
        context['updatefile']='active'
        context['appname']=self.appname
        context['apptitle']=self.apptitle
        context['referesh_website']=self.referesh_website
        context['request']=self.request

        gp=GamePlat.objects.get(Name=self.appname)
        rols=Roles.objects.filter(GPlat=gp).order_by('Type')
        context['rols']=rols
        context['result']=self.result
        return context

    def post(self,*args,**kwargs):

        names=self.request.POST.getlist('port','')

        if names:
            for name in names:
                r=Roles.objects.get(Name=name)

                if r.SHost:
                    if r.Type=='upcdn':
                        cdnupdate=CdnUpdate(r.SHost.IP2,r.SPath,r.DPath,self.referesh_website)
                        cdnupdate.refershcdn()
                        output=cdnupdate.result
                        self.result.extend(output)
                    else:
                        (stat, output) = commands.getstatusoutput("%s %s:%s%s %s:%s " % (r.ExeCom,r.SHost.IP2,r.SPath,r.File,r.DHost.IP2,r.DPath))
                        self.result.append(output)
                else:
                    (stat, output) = commands.getstatusoutput("%s %s -tt %s%s " % (r.ExeCom,r.DHost.IP2,r.DPath,r.File))
                    self.result.append(output)
        else:
            raise Http404

        gp=GamePlat.objects.get(Name=self.appname)
        rols=Roles.objects.filter(GPlat=gp).order_by('Type')
        proplat='open'
        updatefile='active'
        apptitle=self.apptitle
        appname=self.appname
        result=self.result
        request=self.request
        return render_to_response('update.html',locals())

def mytest(request):
    return HttpResponse('{msg : "删除解密日志数据成功"}', content_type="application/json")
