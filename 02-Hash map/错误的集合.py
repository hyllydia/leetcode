"""
集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。


示例 1：

输入：nums = [1,2,2,4]
输出：[2,3]

示例 2：

输入：nums = [1,1]
输出：[1,2]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/set-mismatch
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
"""
解题思路：
两个元素， 一个是丢失的元素， 一个是多余的元素
多余的元素次数为2，哈希值统计元素格式， value为2的元素多余的元素
丢失的元素用减法来解决：[1,n]数组的和减去sum(set(nums))得到的就是丢失的元素
"""
def findErrorNums(nums):
    res=[]
    hash_map={}
    for i in nums:
        hash_map[i]=hash_map.get(i,0)+1
    for k,v in hash_map.items():
        if v==2:
            res.append(k)
    m=sum(set(nums))
    n=(1+len(nums))*len(nums)//2
    res.append(n-m)
    return res

if __name__=="__main__":
    nums=[1,2,2,3]
    print(findErrorNums(nums))