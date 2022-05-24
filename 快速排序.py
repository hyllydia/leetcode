#coding:utf-8
"""
Author:Hou Yuling
Time:11/2/2021 3:31 PM
思想：找到一个基准值， 每个元素和基准值比较， 比它小的放前面，大的放后面，
第一轮比较完成之后，将基准值左边部分和右边部分分别用快排序再次排序，也就是递归排序
时间复杂度O(nlogn),空间复杂度O(logn)
"""
def quicksort(ll,left,right):
    if left>right:
        return ll
    mid=partition(ll,left,right)
    quicksort(ll,left,mid-1)
    quicksort(ll,mid+1,right)
def partition(ll,left,right):
    key=left
    while left<right:
        while left<right and ll[right]>=ll[key]:
            right-=1
        while left<right and ll[left]<=ll[key]:
            left+=1
        (ll[left],ll[right])=(ll[right],ll[left])
    (ll[left],ll[key])=(ll[key],ll[left])
    return left
def func(ll):
    n=len(ll)
    if n<=1:
        return ll
    quicksort(ll,0,n-1)
    return ll
if __name__=="__main__":
    print(func([3,19,28,0,5,40,2]))