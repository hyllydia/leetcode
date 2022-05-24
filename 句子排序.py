# coding:utf-8
"""
Author:Hou Yuling
Time:10/19/2021 3:25 PM
解题思路：
我的思路是先排序然后删除数字，
答案思路先排序然后join数字之前的元素， 数字在最后一位可以不用删除， 直接join数字前的元素就可以了
" ".join([item[:-1] for item in sorted(s.split(" "),key =lambda x: x[-1])])
"""


def func(s):
    lls = sorted(s.split(" "), key=lambda x: x[-1])
    res = []
    for item in lls:
        x = list(item)
        x.remove(x[-1])
        item = "".join(x)
        res.append(item)
    print(" ".join(res))


if __name__ == "__main__":
    func("is2 sentence4 This1 a3")
