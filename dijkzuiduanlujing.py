#-*- coding:utf-8 -*-
__author__ = 'Administrator'

#初始化阵列
m = input(u'输入地点数量 :')
n = input(u'输入路径数量 :')
longway = 9999
list = [[longway for i in range(m)] for i in range(m)   ]
#print list
for i in range(m):
    list[i-1][i-1] = 0
#print list
for i in range(n):
    x,y,z = input(u'输入路径的方向和权值 :')
    list[x-1][y-1] = z

#初始化dis列表
disway = list[0]
biduilist = [0 for i in range(m)]
biduilist[0] = 1
'''print list
print disway
print biduilist'''
#核心算法

for j in range(m):
    min = longway
    for i in range(m):
        if disway[i] < min and biduilist[i] == 0 :
            min = disway[i]
            u = i
    biduilist[u] = 1
    for v in range(m):
        if disway[v] > disway[u] + list[u][v]:
            disway[v] = disway[u] + list[u][v]

print list



'''首先，dis1最小肯定是0，找到其他dis最小的数值，然后使用dis最小的数据到每个结束路径dis进行比对，如果有更小则更新，再从未定义的里面继续取一个dis'''
