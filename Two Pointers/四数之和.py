#coding:utf-8
def func(nums,target):
    ans=[]
    nums.sort()
    n=len(nums)
    for i in range(n):
        #去重a
        if i >= 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i+1,n):
            #去重b
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            left=j+1
            right=n-1
            while left<right:
                total=nums[i]+nums[j]+nums[left]+nums[right]
                if total<target:
                    left+=1
                elif total>target:
                    right-=1
                else:
                    ans.append([nums[i],nums[j],nums[left],nums[right]])
                    while left!=right and nums[left]==nums[left+1]:
                        left+=1
                    while left!=right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
    return ans

if __name__=="__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    print(func(nums,target))