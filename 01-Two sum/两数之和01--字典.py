    #coding:utf-8
"""
Author:Hou Yuling
Time:11/16/2021 2:24 PM
"""
def func(nums,target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i+1,j+1]
def func1(nums,target):
    d={}
    for i,j in enumerate(nums):
        if target-j in d.keys():
            return [d[target-j]+1,i+1]
            #return [i,d[target-j]]
        d[j]=i
if __name__=="__main__":
    print(func1([0,0,3,4],0))