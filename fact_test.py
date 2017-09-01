# -*- coding:utf-8 -*-
#fact_test.py

def fact(n):
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n-1)

'''
>>> fact(3)
6
>>> fact(1)
1
>>> fact(-1)
Traceback (most recent call last):
    ...
ValueError
'''

if __name__ == '__main__':
    import doctest
    doctest.testmode()
