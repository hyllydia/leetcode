#coding:utf-8
"""
Author:Hou Yuling
Time:11/16/2021 9:56 PM
"""
import re
def func(s1,s2):
    if len(s1)!=len(s2):
        return False
    for i in range(1,len(s1)):
        while (s1[i::]+s1[0:i])==s2:
            return True
if __name__=="__main__":
    print(func("waterbottle","erbottlewat"))