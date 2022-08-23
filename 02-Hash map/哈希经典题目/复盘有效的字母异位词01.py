#coding:utf-8
"""
Author:Hou Yuling
Time:8/22/2022 4:31 PM
"""
""""
242. 有效的字母异位词

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

 

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true

示例 2:

输入: s = "rat", t = "car"
输出: false
"""
"""
复盘的问题：统计字符在字符串中出现的次数
两种方法， 第一种构造[0]*26, 这个写出来了
第二种方法用hashz_map的方法去构造!!!!这个方法完全忘记了
hash_map={}
for i in s:
    hash_map[i]=hash_map.get(i,0)+1
    
"""
def func(s,t):
    record=[0]*26
    for i in s:
        record[ord(i)-ord('a')]+=1
    print(record)
    for j in t:
        record[ord(j)-ord('a')]-=1
    print(record)
    if record==[0]*26:
        return True
    else:
        return False
if __name__=="__main__":
    s = "anagram"
    t = "nagaram"
    func(s,t)