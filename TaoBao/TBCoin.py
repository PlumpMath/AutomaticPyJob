#coding=gbk

from __future__ import unicode_literals
from TBLogin import TBLogin
import re


class TBCoin(object):
    '''
    �Խ��ģ��
    ʹ��֮ǰ����ȷ���Ѿ�ʹ��TBLogin.py���е�¼
    '''
    
    tb = TBLogin()
        
    
    def getCurrentTBCoin(self):
        """
        ��õ�ǰ��¼�û����Խ������
        ����ֵ���ɹ��򷵻ؽ��������ʧ���򷵻�None
        """
        
        r = re.compile('<strong id="J_Coin">(.*?)</strong>', re.S)
        
        url  = 'http://taojinbi.taobao.com/home/award_exchange_home.htm'
        source =  self.tb.request(url)
        s = r.search(source)
        coin = s.group(1) if s else None
        return int(coin) if coin else None
        
if __name__ == '__main__':
    t = TBLogin('autorunforscott@163.com','autorun123456')
    if t.login():
        print TBCoin().getCurrentTBCoin()