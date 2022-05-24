#coding:utf-8
"""
Author:Hou Yuling
Time:11/1/2021 8:23 PM
"""
def func(nums):
    # ls=sorted(nums,reverse=True)
    # res=sorted(ls,key=lambda x :nums.count(x))
    res=sorted(nums,key=lambda x: (nums.count(x),-x))
    #首先基于nums.count(x)进行排序，如果nums.count(x)相等，那么基于-x排列，也就是降序排列
    print(res)
if __name__=="__main__":
    func([1,1,2,2,2,3])
    func([2,3,1,3,2])