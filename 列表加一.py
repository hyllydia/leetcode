"""
示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例 2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：

输入：digits = [0]
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
def func(ll):
    s1=[str(i) for i in ll]
    s1=str(int("".join(s1))+1)
    res=[int(i) for i in s1]
    return res
if __name__=="__main__":
    print(func([1,2,3]))


