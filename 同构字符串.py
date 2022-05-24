
#coding:utf-8
"""
Author:Hou Yuling
Time:11/8/2021 2:33 PM
list(x)!=[k for k,v in d.items() if v==y]
这个答案在力扣运行的执行时间和内存消耗都很大， 我需要寻求最优解，降低时间复杂度。
"""
def func(s,t):
    if len(s)!=len(t):
        return False
    d={}
    for x,y in zip(s,t):
        if x in d.keys() and d[x]!=y:
            return False
        elif y in d.values() and list(x)!=[k for k,v in d.items() if v==y]:
            return False
        else:
            d[x]=y
    return True

def func2(s,t):
    for i in range(len(s)):
        if s.index(s[i])!=t.index(t[i]):
            return False
    return True

if __name__=="__main__":
    print(func2('egg','adi'))

#力扣题解：
def func1(s,t):
    return all(s.index(s[i]) == t.index(t[i])  for i in range(len(s)))
"""
all()函数什么意思？怎么去使用？
all函数用于判断给定的可迭代参数iteable中的所有元素是否否为True， 
元素除了0，空。None False外都算True
def all(iterable):
    for element iterable:
        if not element:
            return False
    return True
题解两种方法一种是index方法， 一种是hash对应方法
"""
def func2(s,t):
    for i in range(len(s)):
        if s.index(s[i])!=t.index(t[i]):
            return False
    return True

