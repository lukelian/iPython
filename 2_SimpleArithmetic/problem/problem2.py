#-*- coding:utf-8 -*-

class Solution():
    def solve(self, x, y):
        add = x + y
        sub = x - y
        mul = x * y
        div_floor = x//y
        return ['x + y = ' + str(add), 'x - y = ' + str(sub), 'x * y = ' + str(mul), 'x // y = ' + str(div_floor)]
        pass