#coding:utf-8
"""
Author:Hou Yuling
Time:11/4/2021 3:22 PM
素数：只能被1和他本身相除的是素数
回文数：101， 12321， 从左至右，从右至左都一样
输入N， 比N大的最小的回文素数
例如：
6--->7
8-->11
13-->101
"""
def func(num):
    for i in range(num,10**8):
        for j in range(2,num):
            if i%j==0:
                break
        else:
            if str(i)==str(i)[::-1]:
                yield i
if __name__=="__main__":
    print(next(func(13)))

