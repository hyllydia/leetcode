#coding:utf-8
"""
Author:Hou Yuling
Time:11/4/2021 3:26 PM
"""
def func(n):
    for i in range(n,1,-1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            yield i
if __name__=="__main__":
    print(next(func(18)))