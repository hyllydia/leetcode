#coding:utf-8
"""
Author:Hou Yuling
Time:8/22/2022 3:56 PM
"""
"""
这里我的思路和代码风格还有些问题
1、我能清楚的知道用哈希值法， 构造一个空字典， 元素作为key, 索引作为value
然而我是两个for循环， 
d={}
for i, j in enumerate(nums):
    d[j]=i
for k,v in d.items():
    if target-k in d:
        return [v,d[target-k]] 
我们来看一下标准答案， 一个for循环就搞定了， 在判断的同时去构造字典 !!!判断和构造字典放在一起！！！ 
"""
def two_sum(nums,target):
    d={}
    for i, j in enumerate(nums):
        if target-j in d:
            return [i,d[target-j]]
        d[j]=i
if __name__=="__main__":
    nums=[2,7,11,15]
    target=9
    print(two_sum(nums,target))
