import os 
import shutil

source="C:/Users/shubh/Downloads"
listoffiles=os.listdir(source)
print(listoffiles)

for i in listoffiles:
    route,ext=os.path.splitext(i)
    #print(route)
    print(ext)