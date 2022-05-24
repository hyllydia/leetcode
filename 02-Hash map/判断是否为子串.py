#coding:utf-8
"""
Author: Lydia Hou
Time: 5/11/2022 3:29 PM
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

如果可以，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。

示例 1：

输入：ransomNote = "a", magazine = "b"
输出：false

示例 2：

输入：ransomNote = "aa", magazine = "ab"
输出：false

示例 3：

输入：ransomNote = "aa", magazine = "aab"
输出：true

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/ransom-note
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
方法1：Hash表的办法
1.将父串中字符的出现个数写入哈希表中；
2.遍历子串， 子串的字符若不在哈希表中，那么便不是子串，返回False
如果出现， 那么该字符串的次数-1， 直到减到-1。
"""
def canConstruct_1(sub_str,str):
    hash_map={}
    Flag=True
    for word in str:
        hash_map[word]=hash_map.get(word,0)+1
    for word in sub_str:
        if word not in hash_map:
            Flag=False
            return Flag
        else:
            hash_map[word]-=1
            if hash_map[word]==-1:
                Flag=False
                return Flag
    return Flag
"""
方法2：判断子串是否在父串中， 在的话， 父串的该字符替换成空格
"""
def canConstruct_2(sub_str,s):
    for i in range(len(sub_str)):
        if sub_str[i] in s:
            s =  s.replace(sub_str[i],'',1)
        else:
            return False
    return True

"""
方法3：

"""
def canConstruct_3(sub_str,str):
    arr=[0]*26
    for i in str:
        arr[ord(i)-ord('a')] += 1
    for i in sub_str:
        if arr[ord(i)-ord('a')]==0:#遍历子串的字符， 如果父串中对应位置的值为0 ， 那么说明父串没有这个字符，那么久返回False
            return False
        else:
            arr[ord(i)-ord('a')]-=1
    return True

if __name__=="__main__":
    #判断是否为子串
    sub_str1="aa"
    str1="aab"

    sub_str2="ba"
    str2="bb"

    # res1=canConstruct_1(sub_str1,str1)
    # print(res1)
    # res2=canConstruct_1(sub_str2,str2)
    # print(res2)

    # res3 = canConstruct_2(sub_str1, str1)
    # print(res3)
    # res4 = canConstruct_2(sub_str2, str2)
    # print(res4)

    res5 = canConstruct_3(sub_str1, str1)
    print(res5)
    res6 = canConstruct_3(sub_str2, str2)
    print(res6)