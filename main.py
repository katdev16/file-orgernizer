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

    # if "ZIP"  in files_in_dir:
    #     print("ZIP folder already exist")
 
    # if "MP4" in files_in_dir:
    #     print("MP4 folder already exist")

    # if "PGN" in files_in_dir:
    #     print("PGN folder already exist")

    
    # if "ZIP" not in files_in_dir:
    #         os.mkdir(path+r"\ZIP")
    # if "ZIP" not in files_in_dir:
    #         os.mkdir(path+r"\MP4")
    # if "PGN" not in files_in_dir:
    #         os.mkdir(path+r"\PGN")

    a=0
    list_of_type_files = []
    for j in files_in_dir:
        if j
        split_tup = os.path.splitext(j)

        file_1_ext = split_tup[1]

        # print(file_1_ext)
        list_of_type_files.append(file_1_ext)

        

        

        if file_1_ext not in path:
            # print(file_1_ext)
            os.mkdir(path+rf"\{file_1_ext}")
            
                
                # os.mkdir(path+rf"\{file_1_ext}")
                # shutil.move(path + rf"\{j}",path+rf"{split_tup[1]}")
    
        shutil.move(path + rf"\{j}",path+rf"\{file_1_ext}")
        # else:
        #     print(1)
        
        a+=1

    # print(list_of_type_files)




        


        

        



    # print(files_in_dir)

