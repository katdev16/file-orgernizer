import os
from queue import Full
import shutil

path = r"C:\Users\user\Music"

files_in_dir = os.listdir(path)


types_of_files = ['.zip','.mp4','.pgn']

empty = []

if len(files_in_dir) != 0:
    
    # split_tup = os.path.splitext(files_in_dir[1])
    # print(split_tup)

    if "ZIP"  in files_in_dir:
        print("ZIP folder already exist")
 
    if "MP4" in files_in_dir:
        print("MP4 folder already exist")

    if "PGN" in files_in_dir:
        print("PGN folder already exist")

    
    if "ZIP" not in files_in_dir:
            os.mkdir(path+r"\ZIP")
    if "ZIP" not in files_in_dir:
            os.mkdir(path+r"\MP4")
    if "PGN" not in files_in_dir:
            os.mkdir(path+r"\PGN")

a=0
for j in files_in_dir:
    split_tup = os.path.splitext(files_in_dir[a])
    # curr_location =os.path.abspath(j)
    # print(split_tup)
    # print(curr_location)
    
    # if split_tup[1]==types_of_files[1]:

    # print("+")
    
  
    if split_tup[1]==types_of_files[0]:
            shutil.move(path + rf"\{j}", path + r"\ZIP")
            print(j)
    if split_tup[1]==types_of_files[0]:
            shutil.move(path + rf"\{j}", path + r"\ZIP")
            print(j)
          
    a+=1




    


    

    



# print(files_in_dir)

