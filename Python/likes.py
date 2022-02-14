def likes(names):
    if names:
       if len(names) < 4:
           if len(names) == 1:
               return f"{names[0]} likes this"
           elif len(names) == 2:
               return f"{names[0]} and {names[1]} likes this" 
           else:
               return f"{names[0]}, {names[1]} and {names[2]} likes this"
       else:
            sisa = len(names)-2
            return f"{names[0]}, {names[1]} and {sisa} others likes this"       
    else:
        return "no one likes this"

# print(likes(["Peter", "Banu", "Suherman", "Aditya", "Rahma"]))
print(likes(["Jacob", "Alex"]))

# umur = 22
# print(f'Umur saya Adalah {umur}')

# print(["Peter"])

 