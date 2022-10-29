from collections import OrderedDict
def lcs(x,y):
    x = "".join(OrderedDict.fromkeys(x))
    y = "".join(OrderedDict.fromkeys(y))
    # print(x)
    # print(y)
    temp = []
    # if len(x) >= len(y):
    #     for i in x:
    #         if i in y:
    #             temp.append(i)
    # else:
    #     for i in y:
    #         if i in x:
    #             temp.append(i)
    for i in y:
        if i in x:
            temp.append(i)
    splash="" 
    return splash.join(temp)
    # for i in y:
    #     if i in 
    # print(search(y, x))
    # if len(x)>= len(y):
    #     if x == y:
    #         return y 
    #     else:
    #         return "" 
    # else:
    #     if x == y:
    #         return x
    #     else:
    #         return ""
# lcs("abcdef","acf")
print(lcs("anothertest","notatest"))
print(lcs("finaltest","zzzfinallyzzz"))
# a = "ABCCD"
# print("".join(OrderedDict.fromkeys(a)))