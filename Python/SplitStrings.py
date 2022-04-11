import textwrap
kata = "abcde"

def splitStrings(kata):
    if len(kata) % 2 == 0:
        return(textwrap.wrap(kata, 2))
    else:
        kata+="_"
        return(textwrap.wrap(kata, 2))

print(splitStrings(kata))

# kata_arr = [ch for ch in kata]
# if len(kata_arr) % 2 == 0:
#     for i in 
# print(kata_arr)
# def solution(s):
#     pass  