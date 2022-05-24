"""
123->321
-123->-321
120->21
"""
def func(num):
    s=str(num)
    if len(s)>1:
        if s[0]=='-':
            s1='-'+s[1:][::-1]
        elif s[-1]=='0':
            s1=s[0:-1][::-1]
        else:
            s1=s[::-1]
        res = int(s1)
        if -2**31<res<2**31-1:
            return res
        else:
            return 0
    else:
        return int(s)
if __name__=="__main__":
    print(func(123))
    print(func(-123))
    print(func(120))