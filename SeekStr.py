# index file and print the path
import os

def SeekStr(path,string):
    for x in os.listdir(path):
        if os.path.isdir(x):
            SeekStr(os.path.join(path,x),string)
        elif os.path.basename(x).find(string) !=-1:
            print(os.path.join(path, x))
        



               
    
