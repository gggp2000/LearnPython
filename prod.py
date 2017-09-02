from functools import reduce
def prod(L):
    multi = reduce(lambda x,y:x*y, L)
    return multi
print('3*5*7*9 = ', prod([3,5,7,9]))
