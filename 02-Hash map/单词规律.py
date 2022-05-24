#coding:utf-8
"""
Author: Lydia Hou
Time: 5/12/2022 3:44 PM
"""
def wordPattern(pattern,s):
    l1=list(pattern)
    l2=s.split(" ")
    hash_map={}
    for k,v in zip(l1,l2):
        hash_map[k]=v



if __name__=="__main__":
    pattern1="abba"
    s1="dog cat cat dog"
    print(wordPattern(pattern1,s1))

    pattern2="aabb"
    s2="dog cat dog cat"
    print(wordPattern(pattern2,s2))