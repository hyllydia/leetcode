


def findRestaurant(list1,list2):
    d={}
    for i in list1:
        if i in list2:
            d[i]=list1.index(i)+list2.index(i)
    d=dict(sorted(d.items(),key=lambda x:x[1]))
    print(d)
    # key_list=list(d.keys())
    # value_list=list(d.values())
    # res.append(key_list[0])
    # for i in range(1,len(value_list)):
    #     if value_list[i]==value_list[0]:
    #         res.append(key_list[i])
    # return res
    return [k for k,v in d.items() if v==list(d.values())[0]]

if __name__=="__main__":
    list1=["Shogun","KFC","Burger King","KFC1"]
    list2=["KFC", "Shogun", "Burger King"]
    print(findRestaurant(list1,list2))