

# def sort_array(source_array):
#     temp = []
#     for i in range(len(source_array)):
#         if source_array[i] % 2 != 0:
#             temp.append(source_array[i])
#     return temp

# print(sort_array([3, 8, 6, 5, 4]))        
data = [5, 3, 2, 8, 1, 4]
testing = [el for el in data if el %2==1]
odds = iter(sorted(el for el in data if el % 2))
a = [next(odds) if el % 2 else el for el in data]
print(a)