a = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"
# a = a.replace(' ',',')
a = a.split()
print(a)
sum=0
c = [int(numeric_string) for numeric_string in a]
print(min(c))
print(max(c))
print(c)

d = [str(max(c)), str(min(c))]  
print(d)
# for i in range(0,len(a),2):
#     print(a[i])

# for i in range(1, 10, 2):
#     print(i)