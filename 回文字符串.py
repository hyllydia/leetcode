import string
def func(s):
    res=("".join(i for i in s if i not in string.punctuation)).replace(' ','').upper()
    print(res)
    res1=res[::-1]
    print(res1)
    if res1==res:
        return True
    else:
        return False
if __name__=="__main__":
    print(func("A man, a plan, a canal: Panama"))



"""
Tips：
1)去掉字符串中的标点符号， string.punctuation  i for i in s if i not in string.punctuation;
2)去掉之后， 单词之间默认用空格连接，再次去掉空格， replace(" ",""), 左右两边有strip();
3)大小写的检查， 全部替换为小写或者大写 ，upper() lower()
4)反转[::-1], 用切片方法最好，因为字符串，列表都可用， sort()与sorted()是列表的反转函数
"""
