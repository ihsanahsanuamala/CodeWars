string = "ihsan ahsanu amala"

def to_jaden_case(string):
    # print(string)
    string = string.split(" ")
    # print(string)
    for i in range(len(string)):
        # print(string[i][0].upper())
        new = string[i].replace(string[i][0], string[i][0].upper())
        # print(type(new))
        print(new)


# print(string[0])

to_jaden_case(string)

