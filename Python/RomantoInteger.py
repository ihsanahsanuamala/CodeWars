def array_diff(a, b):
    #your code here
    temp = []
    for i in a:
        if i not in b:
            temp.append(i)
    return temp

print(array_diff([1, 2], [1]))