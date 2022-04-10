from collections import Counter

 

t=int(input("Masukkan Angka: "))

for i in range(t):

   n=int(input("Masukkan Angka: "))

   a=list(map(int,input().split(' ')))

   z=Counter(a)

   z=dict(z)  

   q=[k*v for k,v in z.items()]

   q.remove(min(q))

   print(sum(q))