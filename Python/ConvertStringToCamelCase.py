import re
def to_camel_case(text):
    # Convert String To List
    a = [char for char in text]
    # Search '-' char after '-' be Upper
    for i in range(len(a)):
            if a[i] == '_' or a[i] == '-' and i != (len(a)-1):
                a[i+1] = a[i+1].upper()
    # Join the list into String again
    text = "".join(a)
    # Remove Char "_" and "-"
    text = re.sub('[_-]', '', text) 
    return text

# print( to_camel_case("the-stealth-warrior"))
print(to_camel_case("the-cat_Is-evil"))
