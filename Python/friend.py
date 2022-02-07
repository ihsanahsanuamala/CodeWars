def friend(x):
    temp  = []
    for i in x:
        if len(i) == 4:
            return(temp.append(i))
            # print(temp)
print(friend(["Ryan", "Kieran", "Mark"]))