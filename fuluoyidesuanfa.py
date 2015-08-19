#-*-coding=utf-8-*-
__author__ = 'Administrator'
zuida = 9999
didian = input(u"输入地点数量 : ")
luxian = input(u"输入路径数量 : ")
#初始化数据方阵
listsq = [[zuida for tt in range(didian)] for ttt in range(didian)]
for yuan in range(didian):
    listsq[yuan-1][yuan-1] = 0

#初始化路径方阵
listlj = [[yy for yy in range(didian)] for ttt in range(didian)]
#print listlj
print u"输入路径数据 : \n"
for ni in range(luxian):
    i,j,quanzhi = input(u"起始，结束，权值(1,2,3) :")
#    print i,j,quanzhi
    listsq[i-1][j-1] = quanzhi
#    print listsq
#    print listsq
#核心算法
for k in range(didian):
    for i in range(didian):
        for j in range(didian):
            if listsq[i-1][j-1] > listsq[i-1][k-1] + listsq[k-1][j-1]:
                listsq[i-1][j-1] = listsq[i-1][k-1] + listsq[k-1][j-1]
                listlj[i-1][j-1] = listlj[i-1][k-1]

#打印路径和权值
print listsq
for i in range(didian):
    for j in range(didian):
        print u"从 %d 到%d 的权值是 %d" %(i+1,j+1,listsq[i][j]),
        k = listlj[i][j]
        print u"路径是 " , i+1,
        while k != j :
            print "--->" , k+1,
            k = listlj[k][j]
        print "--->" , j+1

#            k = listlj[k][j]
#print listsq
#print listlj

