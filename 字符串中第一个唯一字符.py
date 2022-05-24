#coding:utf-8
"""
Author:Hou Yuling
Time:11/16/2021 9:33 PM
"""
def func(s):
    ls=list(s)
    d={}
    for c in ls:
        d[c]=0
    for c in ls:
        d[c]+=1
    for i,j in d.items():
        if j==1:
            return ls.index(i)
    return -1
if __name__=="__main__":
    print(func("leetcode"))
    print(func("loveleetcode"))