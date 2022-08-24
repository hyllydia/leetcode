#coding:utf-8
def func(magazine,ransomNote):
    d1 = {}
    for i in magazine:
        d1[i] = d1.get(i, 0) + 1
    d2 = {}
    for j in ransomNote:
        d2[j] = d2.get(j, 0) + 1
    for k, v in d2.items():
        if k not in d1 or d1[k]<v:
            return False
    return True

if __name__=="main__":
    magazine="ab"
    ransomNote="aa"
    print(func(magazine,ransomNote))