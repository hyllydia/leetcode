#coding:utf-8
"""
Author: Lydia Hou
Time: 5/20/2022 10:38 AM
nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。

给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。

对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。

返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。



示例 1：

输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
输出：[-1,3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
- 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
- 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。

示例 2：

输入：nums1 = [2,4], nums2 = [1,2,3,4].
输出：[3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 2 ，用加粗斜体标识，nums2 = [1,2,3,4]。下一个更大元素是 3 。
- 4 ，用加粗斜体标识，nums2 = [1,2,3,4]。不存在下一个更大元素，所以答案是 -1 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/next-greater-element-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
暴力解法：遍历nums2, 构造字典， 将元素作为key, 将第一个比该元素大的元素作为value；
然后遍历nums1， 初始值设置为-1， 有该元素的直接返回value。
代码里面break的使用是要学习的地方， 结束当前for循环。
"""
def nextGreaterElemnet_1(nums1,nums2):
    d, ln = {}, len(nums2)
    for index, num in enumerate(nums2):
        for i in range(index + 1, ln):
            if nums2[i] > num:
                d[num] = nums2[i]
                break
    return [d.get(j, -1) for j in nums1]

def nextGreaterElement_2(nums1,nums2):
    m, n = len(nums1), len(nums2)
    res = [0] * m
    for i in range(m):
        j = nums2.index(nums1[i])
        k = j + 1
        while k < n and nums2[k] < nums2[j]:
            k += 1
        res[i] = nums2[k] if k < n else -1
    return res
if __name__=="__main__":
    nums1=[4,1,2]
    nums2=[1,3,7,2,5,4]
    # res=nextGreaterElemnet_1(nums1,nums2)
    # print(res)
    res2=nextGreaterElement_2(nums1,nums2)
    print(res2)