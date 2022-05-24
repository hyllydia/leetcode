#coding:utf-8
"""
Author: Lydia Hou
Time: 5/9/2022 4:11 PM
给定一个包含大写字母和小写字母的字符串 s ，返回 通过这些字母构造成的 最长的回文串 。

在构造过程中，请注意 区分大小写 。比如 "Aa" 不能当做一个回文字符串。

示例 1:

输入:s = "abccccdd"
输出:7
解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

示例 2:

输入:s = "a"
输入:1

示例 3:

输入:s = "bb"
输入: 2

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

这一题的算法：
 回文字符串分为两种情况，偶数和奇数
 新建字典统计字符串中字符个数， 如果全部为偶数，那么自然构成回文字符串，长度也是所有字符个数之和。
 如果字符个数出现奇数的话，求出最大偶数。然后将该字符的value置为1。

"""
def longestPalindrome(s):
    d={}
    for i in s:
        d[i]=d.get(i,0)+1#统计字符串中字符个数
    result=0
    for key,value in d.items():
        if value %2 ==0:
            result+=value#如果字符个数是偶数的话， 直接+
        else:
            result +=value-1#如果字符个数是奇数的话， -1是为了求最大偶数，
            d[key]=1#然后将该字符个数置为1
    return result +1 if 1 in d.values()else result#统计结果如果value中还有1的话，可以+1， 作为回文字符串中间值

if __name__=="__main__":
    s1="a"
    s2="aaabccccdd"
    s3="bb"
    s=[s1,s2,s3]
    for m in s:
        res=longestPalindrome(m)
        print(res)