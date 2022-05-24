#coding:utf-8
"""
Author: Lydia Hou
Time: 5/20/2022 4:16 PM
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

美式键盘 中：

    第一行由字符 "qwertyuiop" 组成。
    第二行由字符 "asdfghjkl" 组成。
    第三行由字符 "zxcvbnm" 组成。
示例 1：

输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]

示例 2：

输入：words = ["omk"]
输出：[]

示例 3：

输入：words = ["adsdf","sfd"]
输出：["adsdf","sfd"]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/keyboard-row
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/keyboard-row
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

这套题目的算法思想是：新建字典， 每个字符设置对应的值1或2或3。判断这个单词是否是同一行打印出来的， 例如单词都是
第一行打印出来的， 那么每个字符对应的value值都是1，连接起来后得到"111111"这样的字符串， set之后
长度必然为1。如果不为1就不是一行打印出来的。


"""

def findWords(words):
    res=[]
    d1=dict.fromkeys("qwertyuiop",1)
    d2=dict.fromkeys("asdfghjkl",2)
    d3=dict.fromkeys("zxcvbnm",3)
    d1.update(d2)
    d1.update(d3)
    for word in words:
        aa=""
        for i in word:
            aa+=str(d1[i.lower()])
            if len(set(aa))!=1:
                break
        else:
            res.append(word)
    return res


if __name__=="__main__":
    words=["Hello","Alaska","Dad","Peace"]
    print(findWords(words))