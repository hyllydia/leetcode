#coding:utf-8
"""
Author:Hou Yuling
Time:11/17/2021 10:50 AM
"""
def func(target):
    i,j,s,res=1,2,3,[]
    while i<j:
        if target==s:
            res.append(list(range(i,j+1)))
        if target>=s:
            j+=1
            s+=j
        else:
            s-=i
            i-=1
    return res
if __name__=="__main__":
    print(func(9))
    #print(func(15))