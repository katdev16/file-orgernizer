import os
import shutil


class FileManger():



    current_directory = os.getcwd()


    def create_folder(self,FolderName):
        
        os.mkdir(self.current_directory+rf"\{FolderName}")
        print("created succesfully")



    def files_in_folder(self):
        print(self.current_directory)
        list = os.listdir(self.current_directory)
        return list


    def delete_folder(self,FolderName):
        os.rmdir(self.current_directory+ rf"\{FolderName}")
        print("Folder removed")



    def move_file(src, dest):
        try:
            # Move the file
            shutil.move(src, dest)
            print(f"File '{src}' moved to '{dest}'.")
        except FileNotFoundError:
            print(f"Error: The source file '{src}' does not exist.")



    def files_in_folder(folder_path):
        try:
            # List the contents of the folder
            contents = os.listdir(folder_path)
            return contents
        except FileNotFoundError:
            print(f"Error: The folder '{folder_path}' does not exist.")
            return []


