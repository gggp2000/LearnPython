def normalize(name):
    rename = name[0].upper() + name[1:].lower()
    return rename

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

 
