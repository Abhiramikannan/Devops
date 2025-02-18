import os
print("current directory",os.getcwd())
# f= open("C:\Users\Administrator\devOPs\python\modules\file1.txt",'r')
try:
     f=open("file1.txt")
     #print(f.read())
     print(f.readline())#singleline
     print(f.readlines())#multipleline after the first line it prints
     print(type(f.readlines()))#list
     os.remove("file2.txt")
     print("file2.txt removed")
finally:
  f.close()
os.remove("file1.txt")
print("deleted the file")
     