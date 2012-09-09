#coding=gbk

from __future__ import unicode_literals
import mechanize 
import cookielib,re,urllib,urllib2,sys,os

class TBLogin():
    
    user = None
    pwd = None
    browser = None

    def __init__(self,user,pwd):
        self.user = user
        self.pwd = pwd
        
        # Browser 
        self.browser = mechanize.Browser()
        
        # Cookie Jar 
        cj = cookielib.LWPCookieJar() 
        self.browser.set_cookiejar(cj)
        
        # Browser options 
        self.browser.set_handle_equiv(True) 
        self.browser.set_handle_gzip(False) 
        self.browser.set_handle_redirect(True)
        self.browser.set_handle_referer(False)
        #��������öԷ���վ��robots.txt�Ƿ������á�
        self.browser.set_handle_robots(False)                              
        
        # Follows refresh 0 but not hangs on refresh > 0 
        self.browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        
        # Want debugging messages? 
        #browser.set_debug_http(True) 
        #browser.set_debug_redirects(True) 
        #browser.set_debug_responses(True)
        
        # User-Agent (this is cheating, ok?) 
        self.browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]                    #����ua
        
    def checkLoginError(self,source):  
        commonError = re.compile('<div id="J_Message"  class="login-msg msg">.*<p class="error">(.*?)</div>',re.S)    
        r = commonError.search(source)
        return r.group(1) if r else None

    def checkLoginSucceed(self,source):
        return source.find('TB.Global.writeLoginInfo({"memberServer"') != -1

    def handleVerifyCode(self,source):
        verifyCode = re.compile('<img id="J_StandardCode_m" .*?src="(.*?)".*?>',re.S)  
        r = verifyCode.search(source)
        if r:
            img = urllib.urlopen(r.group(1)).read()
            f = open("verifyCode.jpg","wb")
            f.write(img)
            f.close()
            os.system('verifyCode.jpg')
            return raw_input('��������֤��:')
            
        return ''
    
    def login(self):

        try:
            self.browser.geturl()
        except:
            #�����ȡ��ǰurlʧ�ܣ�˵���ǵ�һ�ε�½����ʱ��Ҫ�򿪵�½ҳ��
            r = self.browser.open('https://login.taobao.com/member/login.jhtml?redirectURL=http://member1.taobao.com/member/fresh/account_security.htm') 
            print r.read()
            
        self.browser.select_form(nr=0)
        self.browser.form['TPL_username'] = 'autorunforscott@163.com'
        self.browser.form['TPL_password'] = 'autorun123456'
#        self.browser.form['longLogin'] = '1'  #�Զ���½
        self.browser.submit()
        self.browser.select_form(nr=0)
        
        #�鿴�ύ��ķ���ҳ��
        res = self.browser.response().read()
        
        if self.checkLoginSucceed(res) == False:
            error = self.checkLoginError(res)
            print error
            if error:
                if error.find('Ϊ�������˺Ű�ȫ����������֤�롣') != -1 \
                or error.find('��֤��������������롣') != -1:
                    v = self.handleVerifyCode(res)
                    self.browser.form['TPL_checkcode'] = v
                    self.login()
            else:
                print 'login failed'
                print res
                
        else:
            print 'login succeed'
#            print self.browser.open('http://i.taobao.com').read()
                    
t = TBLogin('autorunforscott@163.com','autorun123456')
t.login()