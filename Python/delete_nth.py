# from collections import Counter
# def delete_nth(order):
    
    
#     # temp = 0
#     checker = dict(Counter(order))
#     dict_order = {k: v for v, k in enumerate(order)} 
#     # arrCheckerValues = list(checker.values())
#     # print(checker)
#     # for key in checker:
#     #     # if checker[key] >

#     # for i in arrCheckerValues:
#     #     if i >=:
#     #         temp+=1
#     # return temp
#     print(dict_order)
#     # return checker
#     for k, v in checker.items():
#         print(k,v)    


bil = [1,1,3,3,7,2,2,2,7]

# print(len(bil))
# # print(delete_nth([1,1,3,3,7,2,2,2,2]))
# # delete_nth([1,1,3,3,7,2,2,2,2])

# conSet = {2, 2, 3}
# print(conSet)
# temp = []
# for i in bil:
#     if bil.count(i) > 3:
#         temp.append(i)
# print(temp)

# print(bil.count(2))

# a = set(bil)
# for i in a:
#     if bil.count(i)>2:
#         temp.append
# for i in reversed(bil):
#     print(i)
# c = list(filter((1).__ne__, bil))
# print(c)


# Solusi
# temp = []
# for i in bil:
#     if temp.count(i) < 2:
#         temp.append(i)
# print(temp)


nums = [-1,0,3,5,9,12]
target = 0

def binarySearch(nums, target):
    for i in range(len(nums)):
        if(nums[i]) == target:
            return(i)
    return -1
print(binarySearch(nums, 9))