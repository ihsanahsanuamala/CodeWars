text = "The sunset sets at twelve o' clock."


def alphabet_position(text):
    for i in text:
        print(i)
# alphabet_position(text)
# kata = "ihsan"
# kata_arr = [a for a in kata]
# print(kata_arr)

temp = []
for x in text:
    print(x)
    temp.append(ord(x)-96)
print(temp)