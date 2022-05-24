#coding:utf-8
"""
Author:Hou Yuling
Time:11/9/2021 1:48 PM
该题目有三种算法：
超过一半的数字叫做众数
第一：一种是排序法啊，数字的个数超过一半， 那么排序之后中点的数字肯定是众数；
第二：摩尔投票法，众数出现一次记为1， 其他数字出现一次-1， 最终的和肯定是>0的。
"""
def s_func(nums):
    return sorted(nums)[len(nums)//2]
def vote_func(nums):
    vote=0
    for num in nums:
        if vote==0:
            x=num
        if num==x:
            vote+=1
        else:
            vote-=1
    return x

if __name__=="__main__":
    print(s_func([1,2,2,2,2,4,5,3,4]))
    print(vote_func([1,2,2,2,2,4,5,2,4,2]))