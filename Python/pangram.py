from string import ascii_lowercase

kata = "abcdefghijklmopqrstuvwxyz"


print(kata.lower())
print(ascii_lowercase)
kata = kata.lower()
alphabet_list = [ch for ch in ascii_lowercase]
if any(x in kata for x in alphabet_list):
    print("Pangram")
else:
    print("Not Pangram")

# print(ascii_lowercase in kata)
# print(k   ata.find(ascii_lowercase))
# for c in ascii_lowercase:
        
