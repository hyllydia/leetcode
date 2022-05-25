#coding:utf-8
"""
Author: Lydia Hou
Time: 5/23/2022 4:32 PM
和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。

现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。

数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。



示例 1：

输入：nums = [1,3,2,2,5,2,3,7]
输出：5
解释：最长的和谐子序列是 [3,2,2,2,3]

示例 2：

输入：nums = [1,2,3,4]
输出：2

示例 3：

输入：nums = [1,1,1,1]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-harmonious-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
思路：哈希值方法
哈希值方法其实就是字典的方法， 字典的困难之后在于寻找key和value的对应关系，
这题目将，key是元素值， value是元素的个数

"""
from collections import Counter
def findLHS_01(nums):
    hash_map=Counter(nums)
    return max(v+hash_map[k+1]if k+1 in hash_map else 0 for k,v in hash_map.items())


"""同样是hash方法： 将列表中的元素作为key， 元素出现的次数作为value"""
# def findLHS_02(nums):
#     hash_map=defaultdict(int)
#     ans=0
#     for i in nums:
#         hash_map[i]+=1
#         if i+1 in hash_map:
#             ans = max(ans,hash_map[i]+hash_map[i+1])
#         if i-1 in hash_map:
#             ans = max(ans,hash_map[i]+hash_map[i-1])
#     return ans
"""
思路：左右指针加上滑动窗口
左右指针的困难之处在于确定指针指向之处。 该题目是寻求最大和谐子序列，
左边begin指向初始值， 右边end指向比初始值+1的最后一个元素。那么最大长度就是end-begin+1。
"""
def findLHS(nums):
    nums.sort()
    res, begin = 0, 0
    for end in range(len(nums)):
        if nums[end] - nums[begin] > 1:
            begin += 1
        if nums[end] - nums[begin] == 1:
            res = max(res, end - begin + 1)
    return res

if __name__=="__main__":
    nums=[1,2,2,3,3,3]
    #print(findLHS_01(nums))
    print(findLHS_01(nums))