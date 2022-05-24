#strs=["flight",'flow','flower']
def func(strs):
    res=''
    ss=list(map(set,zip(*strs)))
    print(ss)
    for m in ss:
        m=list(m)
        if len(m)>1:
            break
        else:
            res=res+m[0]
    return res
if __name__=="__main__":
    strs=["flight",'flow','flower']
    print(func(strs))

