#coding=gbk

from __future__ import unicode_literals
import Image
import urllib
from Binaryzation import Binaryzation

class VerticalCut(object):
    '''
    ��ֱ�ָ�������ַ�֮��û��ճ�������
    ��ν��ֱ�ָ���ǰ���ɨ�裬�ҵ�ĳ��û�к�ɫ���ص㣨�Ѿ���ֵ������λ��
    
    �����ڶ�ֵ��
    '''

    img = None

    def __init__(self, img):
        self.img = img
        
    def getBorderPoint(self):
        """
        ���ͼ������ұ߽磬�����������֮��Ķ��ǿյ�ͼ�����������֮�ڲ���ͼ��
        """ 
        im = self.img 
        pixels = im.load()  
        w, h = im.size  
        
        left = -1
        right = -1
        breakout = False
        
        #����߽�
        for x in range(w):  
            for y in range(h):  
                if pixels[x, y] == 0:  #�����е�ĳ����Ϊ��ɫ
                    left = x
                    breakout = True
                    break
            if breakout:
                break
                
        breakout = False
        #���ұ߽�
        for x in range(w-1,0,-1):  
            for y in range(h):  
                if pixels[x, y] == 0:  #�����е�ĳ����Ϊ��ɫ
                    right = x
                    breakout = True
                    break
            if breakout:
                break
                
        return left,right
        
    def showVerticalProjection(self,graph):  
        w = len(graph)  
        h = max(graph)  
        img = Image.new('1', (w, h))
        for x in range(w):  
            for y in range(h):  
                if y <= graph[x]:  
                    img.putpixel((x, y), 255)  
                else:  
                    break  
        img = img.transpose(Image.FLIP_TOP_BOTTOM)  
        img.show()  
    
    def cut(self):
        """
        ��ʼ��ֱ�ָ�
        """
        
        if self.img:
            pixels = self.img.load()  
            w,h = self.img.size
            start,end = self.getBorderPoint()
            graph = [0] * (end - start)  #ָ������ĳ���
            
            #�ӿ�ʼ����β������ɨ�裬��ÿ�е����ص����������
            for x in range(start, end):  
                for y in range(h):  
                    pixel = pixels[x, y]
                    if pixel == 0: # �������ַ�  
                        graph[x - start] += 1
            return graph
        
        return None
            
if __name__ == '__main__':
     
    #����֤���ַ��http://su.100steps.net/2007/vote/verify.php
    #�Ա���֤���ַ��http://regcheckcode.taobao.com/auction/checkcode?sessionID=f06c56ea0e0bda9a9d71832422b68f29
    url = 'http://su.100steps.net/2007/vote/verify.php'
    s = urllib.urlopen(url).read()
    f = open('v.jpg','wb')
    f.write(s)
    f.close()
    im = Image.open('v.jpg')
    b =  Binaryzation(im)
    im = b.ConvertToBinaryzation(160)
    im.show()
    v = VerticalCut(im)
    print v.cut()
        
