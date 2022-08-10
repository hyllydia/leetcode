"""
242.有效的字母异位词

力扣题目链接:https://leetcode.cn/problems/valid-anagram/

(opens new window)

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1: 输入: s = "anagram", t = "nagaram" 输出: true

示例 2: 输入: s = "rat", t = "car" 输出: false

说明: 你可以假设字符串只包含小写字母。

"""
"""
方法一：构造record数组[0]*26 , 然后通过计算s[i]-'a'+=1的方法来计算字符串中字符出现的次数判断。
方法二：构造hash_map ,计算字符串中字符的次数， 然后来判断两个hash_map是否相等。
"""
def isAnagram_1(s,t):
    record=[0]*26
    for i in range(len(s)):
        record[ord(s[i])-ord('a')]+=1
    for j in range(len(t)):
        record[ord(t[j])-ord('a')]-=1
    if record==[0]*26:
        return True
    else:
        return False

def isAnagram_2(s,t):
    hash_map01={}
    hash_map02={}
    for i in s:
        hash_map01[i]=hash_map01.get(i,0)+1
    for j in t:
        hash_map02[j]=hash_map02.get(j,0)+1
    return hash_map01==hash_map02
if __name__=="__main__":
    s = "anagram"
    t = "nagarame"
    print(isAnagram_1(s,t))
    print(isAnagram_2(s,t))