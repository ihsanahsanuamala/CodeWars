from collections import Counter
def delete_nth(order):
    
    
    # temp = 0
    checker = dict(Counter(order))
    dict_order = {k: v for v, k in enumerate(order)} 
    # arrCheckerValues = list(checker.values())
    # print(checker)
    # for key in checker:
    #     # if checker[key] >

    # for i in arrCheckerValues:
    #     if i >=:
    #         temp+=1
    # return temp
    print(dict_order)
    # return checker
    for k, v in checker.items():
        print(k,v)    



# print(delete_nth([1,1,3,3,7,2,2,2,2]))
delete_nth([1,1,3,3,7,2,2,2,2])