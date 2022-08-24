#coding:utf-8
"""
快乐数复盘失败了，n=2的时候运行出错了。
也就是说是快乐数的时候可以正常判断并且返回Ture，
不是快乐数的时候返回False这边思路不清晰。
"""
"""
这题目两个难点：
第一个是求和， 转化为字符串之后， 求平方， 这里注意要转成int不要忘记
第二个是判断sum是否有重复， 有重复就认为不是快乐数， 返回false！！！
"""
def isHappy(n):
    all_set=set()
    while n not in all_set:
        all_set.add(n)
        ans=sum(map(lambda x:int(x)**2,str(n)))
        #print(ans)
        if ans==1:
            return True
        n=ans
    return False

if __name__=="__main__":
    n=19
    print(isHappy(n))