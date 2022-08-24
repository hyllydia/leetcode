#coding:utf-8
def func1(magazine,ransomNote):
    d1 = {}
    for i in magazine:
        d1[i] = d1.get(i, 0) + 1
    #print(d1)
    # for j in ransomNote:
    #     if j not in d1 or d1[j]<=0:
    #         return False
    #     else:
    #         d1[j]=d1[j]-1
    # return True
    for j in ransomNote:
        value=d1.get(j)
        if value is None or value==0:
            return False
        else:
            d1[j]-=1
    return True

def func2(magazine,ransomNote):
    d1 = {}
    for i in magazine:
        d1[i] = d1.get(i, 0) + 1
    d2={}
    for j in ransomNote:
        d2[j] = d2.get(j,0)+1
    for k,v in d2.items():
        if k not in d1 or d1[k]<v:
            return False
    return True


"""
方法三：数组作为哈希表， 这个是执行用时最少的。
record=[0]*26
"""
def func3(magazine,ransomNote):
    record=[0]*26
    for i in magazine:
        record[ord(i)-ord('a')]+=1
    #判断和循环放在一起
    for j in ransomNote:
        #对应的位置的值为0的话说明magazine没有这个元素， 那么直接return False
        if record[ord(j)-ord('a')]==0:
            return False
        else:
            record[ord(j)-ord('a')]-=1
    return True
if __name__=="__main__":
    magazine="aab"
    ransomNote="aa"
    print(func1(magazine,ransomNote))
    #print(func2(magazine, ransomNote))
    #print(func3(magazine, ransomNote))