#coding:utf-8
"""
Author:Hou Yuling
Time:11/8/2021 2:02 PM
输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
def func(n):
    all_set=set()
    while n not in all_set:
        all_set.add(n)
        tmp=sum(map(lambda x:int(x)**2,str(n)))
        if tmp==1:
            return True
        n=tmp
    return False
if __name__=="__main__":
    print(func(20))