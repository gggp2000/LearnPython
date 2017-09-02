def by_name(t):
    return t[0].upper()

def by_score(t):
    return t[1]

L=[('Bob',75), ('Tom',82),('igao',90),('lisa',95)]

L1 = sorted(L,key=by_name,reverse=True)

L2 = sorted(L,key=by_score)

print(L1)
print(L2)
