import string
# print(string.ascii_lowercase[:14])
# a = string.ascii_lowercase[:14]
# b = [ch for ch in a]  
# print(b)

def print_error(s):
    s = s.lower()
    s = [ch for ch in s]
    a = [chr(i) for i in range(ord('a'),ord('m')+1)]
    temp = []
    for i in s:
            if i not in a:
                temp.append(i)
    print(f"{len(temp)}/{len(s)}")
print_error("aaaxbbbbyyhwawiwjjjwwm")
# a = [chr(i) for i in range(ord('a'),ord('z')+1)]
# print(a)
