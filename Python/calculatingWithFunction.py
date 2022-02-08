def zero(operasi = None): return 0 if operasi is None else int (operasi(0)) #your code here
def one(operasi = None): return 1 if operasi is None else int (operasi(1))#your code here
def two(operasi = None): return 2 if operasi is None else int (operasi(2))#your code here
def three(operasi = None): return 3 if operasi is None else int (operasi(3))#your code here
def four(operasi = None): return 4 if operasi is None else int (operasi(4))#your code here
def five(operasi = None): return 5 if operasi is None else int (operasi(5))#your code here
def six(operasi = None): return 6 if operasi is None else int (operasi(6))#your code here
def seven(operasi = None): return 7 if operasi is None else int (operasi(7))#your code here
def eight(operasi = None): return 8 if operasi is None else int (operasi(8))#your code here
def nine(operasi = None): return 9 if operasi is None else int (operasi(9))#your code here

def plus(y): return lambda x: x+y #your code here
def minus(y): return lambda x: x-y #your code here
def times(y): return lambda x: x*y#your code here
def divided_by(y): return lambda x: x/y #your code here

print(eight(divided_by(three())))