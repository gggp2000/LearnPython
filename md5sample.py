import hashlib
md5 = hashlib.md5()
md52 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib? --Micheal'.encode('utf-8'))
md52.update('how to use md52 in python hashlib? --Micheal'.encode('utf-8'))
print(md5.hexdigest())
print(md52.hexdigest())           
