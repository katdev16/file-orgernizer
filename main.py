import os
from queue import Full
import shutil

promt = input("Orgainer files(y) or exit with any other key: ")

if promt.lower() == 'y':


    path = r"C:\Users\user\Music"

    files_in_dir = os.listdir(path)
    print(len(files_in_dir))

    empty = []

    if len(files_in_dir) != 0:

        a=0
        y=0
        folders_in_dir=[]
        list_of_type_files = []
        print(f"no. of files in Directory: {len(files_in_dir)}")
        for j in files_in_dir:
            index = len(j)-4
            length = len(j)
            
            if j[index] == ".":
                split_tup = os.path.splitext(j)

                file_1_ext = split_tup[1]

                # print(file_1_ext)
                list_of_type_files.append(file_1_ext)
            
                files_in_dir=os.listdir(path)

                if file_1_ext not in files_in_dir:
                    list_of_Dirmade= []
                    Dir_maker = os.mkdir(path+rf"\{file_1_ext}")
                    y+=1
                    list_of_Dirmade.append(file_1_ext)
                    
                    files_in_dir.append(file_1_ext)
                if y==len(folders_in_dir):
                    print("files organized")
                    break
                if  y!=len(folders_in_dir):

                    shutil.move(path + rf"\{j}",path+rf"\{file_1_ext}")
                a+=1
            else:
                y+=1
                a+=1
              
                folders_in_dir.append(j)


        print(f"y= {y}")
        print(f"a= {a}")
        print(f"folders: {folders_in_dir}")
        print(f"{list_of_Dirmade} folder created")

else: 
    print("no promt")
