#!/usr/bin/env python
# -*- coding: gbk -*-
from __future__ import unicode_literals 
import smtplib
from email.mime.text import MIMEText

class Mail():
    """
        �����ʼ�
    """
    
    #���÷��������û����������Լ�����ĺ�׺
    mail_host = "smtp.163.com"
    mail_user = "autorunforscott@163.com"
    mail_pass = "autorun"
    mail_postfix = "163.com"
    
    def SendMail(self, toList, title, content,fromAddress=None):
        '''
        toList:����˭
        fromAddtress:������
        title:����
        content:����
        send_mail("aaa@126.com","sub","content")
        '''
        me = "AutorunForScott<autorunforscott@163.com>"
        if fromAddress is None:
            fromAddress = me
            
        msg = MIMEText(content)
        msg['Subject'] = title
        msg['From'] = fromAddress
        msg['To'] = ";".join(toList)
        try:
            s = smtplib.SMTP()
            s.connect(self.mail_host)
            s.login(self.mail_user, self.mail_pass)
            s.sendmail(me, toList, msg.as_string())
            s.close()
            return True
        except Exception, e:
            print str(e)
            return False
 


if __name__ == "__main__":
    if Mail().SendMail("qianlf2008@163.com", "title", "content"):
            print "���ͳɹ�"
    else:
            print "����ʧ��"	
