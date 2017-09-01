from io import BytesIO
f = BytesIO()
f.write('zhongwen'.encode('gbk'))
print(f.getvalue())
