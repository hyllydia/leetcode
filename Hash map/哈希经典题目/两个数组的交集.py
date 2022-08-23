#coding:utf-8
"""
Author:Hou Yuling
Time:4/13/2022 3:26 PM
给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。
示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]

示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# def intersection(n1,n2):
#     n=[]
#     for i in nums1:
#         if i in nums2:
#             n.append(i)
#     print(list(set(n)))

#leecode 题解答案


def intersection(n1,n2):
    print(list(set(n1)&set(n2)))

if __name__=="__main__":
    nums1=[1,2,2,1]
    nums2=[2,2]
    # nums1=[4,9,5]
    # nums2=[9,4,9,8,4]
    intersection(nums1,nums2)