#coding:utf-8
"""
Author: Lydia Hou
Time: 5/12/2022 10:05 AM
给定两个字符串 s 和 t ，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。



示例 1：

输入：s = "abcd", t = "abcde"
输出："e"
解释：'e' 是那个被添加的字母。

示例 2：

输入：s = "", t = "y"
输出："y"


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-the-difference
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
分为两种情况， 第一是添加的字符和原来的字符完全不同， 第二种添加的字符和原来的字符有重复的， 那么就只是value值增加了
"""
#字典
def findthedifference_1(s,t):
    hash_map1={}
    hash_map2={}
    for word in s:
        hash_map1[word]=hash_map1.get(word,0)+1
    for word in t:
        hash_map2[word]=hash_map2.get(word,0)+1
    for k,v in hash_map2.items():
        if k not in hash_map1:
            return k
        elif v>hash_map1[k]:
            return k
#ASCII码计数法
def findthedifference_2(s,t):
    arr=[0]*26
    for i in s:
        arr[ord(i)-ord('a')]+=1
    for i in t:
        arr[ord(i)-ord('a')]-=1
        if  arr[ord(i)-ord('a')]<0:
            return i
#异或， 位运算
def findTheDifference(s,t):
    res = 0
    for i in s + t :
        res ^= ord(i)
    return chr(res)
#求和方法，两个字符串的ascii码相加之后做减法，其实和ascii码的方法差不多
def findthedifference(s,t):
    return chr(sum(map(ord,t))-sum(map(ord,s)))



if __name__=="__main__":
    s="abc"
    t="bcda"
    # res=findthedifference_1(s,t)
    # print(res)
    res1=findthedifference_2(s,t)
    print(res1)
    #res2=findthedifference(s,t)
    #print(res2)