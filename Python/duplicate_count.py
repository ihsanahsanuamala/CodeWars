# def duplicate_count(text):
#     # Change Input into String
#     text = str(text)
#     # Change Input into Lower to chekcing easier
#     text = text.lower()
#     # Change Input into list
#     arrText = [ch for ch in text]
#     counter = 0
#     temp = 0
#     print(arrText)
#     for i in range(len(arrText)):
#         for j in range(i+1, len(arrText)):
#             if arrText[i] == arrText[j]:
#                 counter+=1
#                 break
#                 # print("ada")
#                 # if counter ==2:
#                 #     temp+=1
#                 #     break
#     return counter                
#     # print(len(arrText))
#     # print(len(set(arrText)))

    # We just subtract the list and the set
    # return len(arrText) - len(set(arrText))
# duplicate_count("abcde")

# Cara 2
from collections import Counter
def duplicate_count(text):
    # Change Input into String
    text = str(text)
    # Change Input into Lower to chekcing easier
    text = text.lower()
    # Change Input into list
    arrText = [ch for ch in text]
    # Variable for hold value
    temp = 0

    checker = dict(Counter(arrText))
    arrCheckerValues = list(checker.values())
    for i in arrCheckerValues:
        if i >=2:
            temp+=1
    return temp

print(duplicate_count("abcdeaa"))