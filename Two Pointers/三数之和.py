#coding:utf-8
def func(nums):
    ans=[]
    nums.sort()
    n=len(nums)
    for i in range(n):
        left=i+1
        right=n-1
        #因为已经排序了， 后面的数只会更大，第一个数就大于0， 那么和肯定不会是0，直接break
        if nums[i]>0:
            break
        '''
        对于这个判断很疑惑,DEBUG一步步看到，
        如果当前元素和前一个已经判断过的元素是相等的， 就不需要重复判断了，去重a操作
        '''
        if i>=1 and nums[i]==nums[i-1]:
            continue
        while left<right:
            total=nums[i]+nums[left]+nums[right]
            if total>0:
                right-=1
            elif total<0:
                left+=1
            else:
                ans.append([nums[i],nums[left],nums[right]])
                """
                对于这部分代码有疑惑，这一部分也是去重b,c操作，
                如果left和后一个元素相等， 就不需要在判断
                如果right和前一个元素相等， 那么也不需要再次去判断 
                """
                while left!=right and nums[left]==nums[left+1]:
                    left+=1
                while left!=right and nums[right]==nums[right-1]:
                    right-=1
                left+=1
                right-=1
    return ans

if __name__=="__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(func(nums))