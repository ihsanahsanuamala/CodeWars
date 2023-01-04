a = [0,1,0,1,0]

def find_it(a):
    a_set = set(a)
    for i in a_set:
        if a.count(i) % 2 !=0:
            return i

def xo(s):
    s = s.lower()
    s_list =  [i for i in s]
    counter_o = s_list.count('o')
    counter_x = s_list.count('x')
    if counter_o == 0 and counter_x == 0:
        return True
    elif counter_x == counter_o:
        return True
    else:
        return False

# print(xo("xxxoo"))

x = '8 j 8   mBliB8g  imjB8B8  jl  B'
def no_space(x):
    return x.strip()
print(no_space(x))

