#coding:utf-8
"""
给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：

    0 <= i, j, k, l < n
    nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0



示例 1：

输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
输出：2
解释：
两个元组如下：
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

示例 2：

输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/4sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
"""
这个题目采用哈希值方法，将a+b的和放进hashmap中作为key， 次数作为value
然后遍历c,d， 如果出现(0-a-b), 那么count+1
"""
def func(nums1,nums2,nums3,nums4):
    hashmap={}
    for i in nums1:
        for j in nums2:
            hashmap[i+j]=hashmap.get(i+j,0)+1
    c=0
    for m in nums3:
        for n in nums4:
            key=-m-n
            if -m-n in hashmap:
                c+=hashmap[key]
    return c


if __name__=="__main__":
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    print(func(nums1,nums2,nums3,nums4))