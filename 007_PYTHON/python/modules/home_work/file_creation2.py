import os
import time


def file_creation(directory,filenames):
    if not os.path.exists(directory):
        os.makedirs(directory)
    for file_name in filenames:
        file_path=os.path.join(directory,file_name)
        with open(file_path,'w') as file:
            file.write("this is a sample file: " +file_name)
        print("created :{file_path}")#fstring format

directory=input("enter the directory path")
