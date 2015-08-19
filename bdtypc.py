__author__ = 'Administrator'
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class geshihua():
    


class BDTB(object):

    def __init__(self,tburl):
        self.tburl = tburl
        self.tbnr = None
        self.zklz = 1

    def wangyesj(self):
        x = urllib2.Request('http://tieba.baidu.com/p/2504730047?see_lz=1&pn=2')
        y = urllib2.urlopen(x)
        z = y.read()
        return z

    def tittle(self,c):
        tittlere = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>')
        tittle = re.search(tittlere,c)
        #print tittle.group(1)
        return str(tittle)

    def yeshu(self,c):
        yeshure = re.compile('<span class="tP">(.*?)</span>')
        yeshu = re.search(yeshure,c)
        #print tittle.group(1)
        return str(yeshu)

    def wenjian(self):
        filety =

def wenjian
def xiewenjian

yuanurl
shifouxietittle
shifouxieyema

