#-*- coding:utf-8 -*-

class Solution():
    def solve(self, x):
        strx = str(x)
        return strx[0:3] + ' ' + strx[3:6] + ' ' + strx[6:9]
        pass