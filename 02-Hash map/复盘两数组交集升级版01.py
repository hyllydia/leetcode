#coding:utf-8
"""
Author:Hou Yuling
Time:8/23/2022 2:20 PM
"""
"""
复盘的问题：哈希值的方法写出来了， 没有问题， 代码基本和以前一样， 但是还有一个pop()的方法完全没想起来
"""
def func(nums1,nums2):
    res=[]
    d1={}
    d2={}
    count=0
    for i in nums1:
        d1[i]=d1.get(i,0)+1
    for j in nums2:
        d2[j]=d2.get(j,0)+1
    for k,v in d1.items():
        if k in d2:
            count=v if v<d2[k] else d2[k]
            for i in range(count):
                res.append(k)
    return res
if __name__=="__main__":
    nums1=[1,2,2,1]
    nums2=[2,2]
    print(func(nums1,nums2))
    nums3=[4,9,5]
    nums4=[9,4,9,8,4]
    print(func(nums3,nums4))

