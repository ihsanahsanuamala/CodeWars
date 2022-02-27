from collections import Counter

def dirReduc(arr):
    # rules = {
    #     "NORTH" : 1,
    #     "SOUTH" : -1,
    #     ""
    # }

    a =  dict(Counter(arr))
    # print(a)
    
    # print(a.values())
    # print(a.keys("NORTH"))
    # print(a["NORTH"])
    for count, dirr in enumerate(a):
        print(count, dirr)
        
        # if a[i]
    # print(a)
    # temp = []
    # for dirr,count in a.items():
    #     print( dirr, count)
        # temp.append(dirr, count)


direction = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
dirReduc(direction)