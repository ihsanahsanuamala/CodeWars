# def solution(string, marker):
#     # We Split String Into List 
#     list_s = string.split("\n")
#     # Check each item
#     for word  in list_s:
#         s = ""
#         temp = []
#         # Check if we find unik char
#         for char in word:
#             if char in marker:
#                 break
#             else:
#                 s += char
#         temp.append(s.strip())
#     return "\n".join(temp)

def solution(string,markers):
    s_list = string.split("\n")
    n_list = []

    for item in s_list:
        s = ""
        for char in item:
            if char in markers:
                break
            else:
                s = s + char
        n_list.append(s.strip())
    return "\n".join(n_list)

# print(solution("apples, pears # and bananas\ngrapes\nbananas !apples",["#","!"]))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in a:
    print(i)
    if i == 5:
        break