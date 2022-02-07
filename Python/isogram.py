def is_isogram(string):
    string = string.lower()
    x = [char for char in string]
    print(x)
    if len(x) == len(set(x)):
        return True
    else:
        return False
        
print(is_isogram("moOse"))