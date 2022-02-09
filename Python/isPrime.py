import math
def is_prime(num):
   #TODO
    if num < 2:
        return False
    if num == 2:
        return True
    x = int(math.sqrt(num))+1
    for i in range (2, x):
        if num % i == 0:
            return False
    return True