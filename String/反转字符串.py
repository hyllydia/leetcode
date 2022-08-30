#coding:utf-8
# def reversestring(s):
#     # s1="".join(s)
#     # print(s1)
#     s2=list(reversed(s))
#     #print(s2)
#     return s2
def two_pointers_sol(s):
    n=len(s)
    left=0
    right=n-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return s
if __name__=="__main__":
    s = ["h","e","l","l","o"]
    #print(reversestring(s))
    print(two_pointers_sol(s))