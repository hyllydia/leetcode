#coding:utf-8
"""
Author:Hou Yuling
Time:10/31/2021 10:32 PM
冒泡排序的思想是， 交换相邻的两个元素，如果前面的元素大就相互交换
时间复杂度：O(n**2),空间复杂度为O(1)
"""
def func(ll):
    n=len(ll)
    if n<=1:
        return ll
    for i in range(n):
        for j in range(n-i-1):
            if ll[j]>ll[j+1]:
                (ll[j],ll[j+1])=(ll[j+1],ll[j])
    return ll

if __name__=="__main__":
    print(func([1,2,2,19,5,4,3]))