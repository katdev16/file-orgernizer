import os
from queue import Full
import shutil

promt = input("Orgainer files(y) or exit with any other key: ")

if promt.lower() == 'y':


    path = r"C:\Users\user\Music"

    files_in_dir = os.listdir(path)

    empty = []

    if len(files_in_dir) != 0:

        a=0
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

                if file_1_ext not in files_in_dir:
                    # print(file_1_ext)
                    os.mkdir(path+rf"\{file_1_ext}")
                    files_in_dir.append(file_1_ext)
                    
                        
                        # os.mkdir(path+rf"\{file_1_ext}")
                        # shutil.move(path + rf"\{j}",path+rf"{split_tup[1]}")
                if files_in_dir[a]==len(files_in_dir)-1:
                    print("files organized")
                if files_in_dir[a]!=len(files_in_dir)-1:

                    shutil.move(path + rf"\{j}",path+rf"\{file_1_ext}")
                a+=1
                print(a)
                # else:
                #     print(1)
                

            else:
                a+=1
                print(a)
                folders_in_dir.append(j)
                print(folders_in_dir)

        

        print(list_of_type_files)
        print(folders_in_dir)




            


            

            



        # print(files_in_dir)
else: 
    print("no promt")
