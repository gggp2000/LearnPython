from collections import Iterable
L = ['Hello', 'World', 18, 'Apple', None]
L2 = []
for s in L:
    if isinstance(s, Iterable):
        L2.append(s.lower())
    else:
        L2.append(s)
print(L2)
