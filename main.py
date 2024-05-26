import os
from queue import Full
import shutil

path = r"C:\Users\user\Music"

files_in_dir = os.listdir(path)

if len(files_in_dir) != 0:
    types_of_files = [".zip",".mp4",".pgn"]
    # split_tup = os.path.splitext(files_in_dir[1])
    # print(split_tup)
    for i in files_in_dir:
        if "ZIP" in files_in_dir:
            print("ZIP folder already exist")
        elif "MP4" in files_in_dir:
            print("MP4 folder already exist")
        elif "PGN" in files_in_dir:
            print("PGN folder already exist")
        else:
            os.mkdir(path+"\ZIP")
            os.mkdir(path+"\MP4")
            os.mkdir(path+"\PGN")

    


    

    



print(files_in_dir)

