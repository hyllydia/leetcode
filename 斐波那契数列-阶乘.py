#生成斐波那契数列
def fib(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
        yield a
if __name__=="__main__":
    for i in fib(10):
        print (i,end=" ")

#递归求Fib数列：
def fib2(m):
    if m<=1:
        return 1
    else:
        return fib2(m-1)+fib2(m-2)
if __name__=="__main__":
    for i in range(7):
        print(fib2(i),end="%s")



#递归求阶乘
def func(n):
    if n==0:
        return 1
    else:
        return n*func(n-1)
if __name__=="__main__":
    print("\n",func(5))

#coding:utf-8
"""
Author:Hou Yuling
Time:10/19/2021 3:25 PM
a,b=b,a+b，先要去计算等号右边的值，b=1,b+a=1, 计算完成之后再赋值
b赋值给a, a=1, b=a+b=1
"""
a,b=0,1
for i in range(2):
    a,b=b,b+a
    print(a,b)
"""
i=0:
b=1,a+b=1
a=1,b=1
i=1:
b=1,a+b=2
a=1.b=2
"""