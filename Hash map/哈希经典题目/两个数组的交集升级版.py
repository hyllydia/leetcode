#coding:utf-8
"""
Author: Lydia Hou
Time: 4/13/2022 4:35 PM
给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，
应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
def intersect(n1,n2):
    n=[]
    for i in n1:
        if i in n2:
            n.append(i)
    res=[]
    m=list(set(n))
    for j in m:
        m1=n1.count(j)
        m2=n2.count(j)
        x=m1 if m1<=m2 else m2
        for i in range(x):
            res.append(j)

    print(res)
"""哈希值法"""
def intersect_hash01(nums1,nums2):
    res=[]
    hash_map1={}
    hash_map2={}
    for i in nums1:
        hash_map1[i]=hash_map1.get(i,0)+1
    for j in nums2:
        hash_map2[j]=hash_map2.get(j,0)+1
    for k,v in hash_map1:
        if k in hash_map2:
            x=v if v<=hash_map2[k] else hash_map2[k]
            for m in range(x):
                res.append(k)
    return res
def intersect_hash02(nums1,nums2):
    ans=[]
    d={}
    for i in nums1:
        d[i]=d.get(i,0)+1
    for j in nums2:
        if j in d:
            d[j]=d.get(j)-1
            if d[j]==0:
                d.pop(j)#d.pop()的用法
            ans.append(j)
    return ans
if __name__=="__main__":
    # nums1=[1,2,2,1]
    # nums2=[2,2]
    nums1=[4,9,5,4,9]
    nums2=[9,4,9,8,4]
    #intersect(nums1,nums2)
    print(intersect_hash02(nums1,nums2))