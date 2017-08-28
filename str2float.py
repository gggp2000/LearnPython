from functools import reduce

def char2num(s):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

def str2float(s):
    n = s.index('.')
    s1 = s.replace('.','')
#    s1 = s[:n]+s[n+1:]
    return reduce(lambda x,y: x*10+y, map(char2num, s1))/pow(10,len(s1)-n)

f = str2float('2222.333')
print(f)
