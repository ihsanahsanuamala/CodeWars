def dont_give_me_five(start,end):
    # your code here
    n=0
    for i in range(start, end+1):
        # print()
        i = str(i)
        if "5" not in i :
            print(i)
            n+=1
    return n   # amount of numbers
print(dont_give_me_five(4,17))
4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,         