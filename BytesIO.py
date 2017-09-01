from io import BytesIO
f = BytesIO()
f.write('中文'.encode('gbk'))
print(f.getvalue())
