__author__ = 'Administrator'
class paixu(object):
    def __init__(self,listty):
        self.lenty = len(listty)
        self.listsj = listty

    def maopao(self):
        #print self.lenty
        #print self.listsj
        x = 0
        for i in range(1,self.lenty):
            #print i
            for j in range(1,self.lenty-i+1):
                x += 1
                if self.listsj[j-1] > self.listsj[j]:
                    y = self.listsj[j]
                    self.listsj[j] = self.listsj[j-1]
                    self.listsj[j-1] = y
        print self.listsj
        print x
#        return listsj
xulie = [7,4,8,2,5,9,44,56,23,9]
suanfa = paixu(xulie)
#print suanfa.lenty
suanfa.maopao()