a = "This website is for losers LOL!"

b = ["a", "i" , "u", "e", "o"]
c = []

for i in a:
    if i.lower() not in b:
        c.append(i)
d = "".join(c)
print(d)
