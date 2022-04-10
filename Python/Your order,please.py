# from numpy import array


# def order(sentence):
#     # array = [ch for ch in sentence]
#     array = sentence.split()
#     # for i in array: 
#     return array
# print(order("Banu Suherman"))


# words = "Ahsanu2 Ihsan1 3Amala"

# arrWords = words.split()
# # print(arrWords)
# kump_list = []
# for i in arrWords:
#     # print (i)
#     list = [ch for ch in i]
#     kump_list.append(list)
# print (kump_list)
# for i in range(len(kump_list)):
#     # print(kump_list[i])
#     for j in range(len(kump_list[i])) :
#         # print("iterasi",j)
#         print(kump_list[i][j])

def order(sentence):
    array = sentence.split()
    rules = {"1":"NONE", "2":"NONE", "3":"NONE", "4":"NONE", "5":"NONE", "6":"NONE", "7":"NONE", "8":"NONE", "9":"NONE"}
    result=""
    for word in array:
        for char in word:
            if(char.isdigit() and int(char) <=9):
                rules[char] = word
    sorted_dict = sorted(rules.items())
    for s in sorted_dict:
        if(s[1]!="NONE"):
            result = result + s[1]+" "
    result = result[:-1]
    return result
#     return array

# a = "2"
# print(a.isdigit())
print(order("is2 Thi1s T4est 3a"))

