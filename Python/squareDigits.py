def square_digits(num):
    # x = num.split()
    x = [int(i) for i in str(num)]
    
    for i in range(len(x)):
        x[i] = x[i]**2
    # print(x)
    res = int("".join(map(str, x)))
    return res
print(square_digits(1212))