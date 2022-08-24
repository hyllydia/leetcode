#coding:utf-8
from collections import defaultdict
s="aab"
d=defaultdict(int)
for i in s:
    d[i]+=1
print(d)