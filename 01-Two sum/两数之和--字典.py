"""
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
#coding:utf-8
def func(ll,num):
    res=[]
    for i in range(len(ll)-1):
        for j in range(i+1,len(ll)):
            if ll[i]+ll[j]==num:
                res.append(i)
                res.append(j)
    return res

def func1(ll,num):
    d={}
    for i,j in enumerate(ll):
        if num-j in d:
            return [i,d[num-j]]
        d[j]=i
def func2(ll,num):
    d={}
    for i in range(len(ll)):
        if num-ll[i] in d:
            return [i,d[num-ll[i]]]
        d[ll[i]]=i
if __name__=="__main__":
    print(func1([2,7,4],9))