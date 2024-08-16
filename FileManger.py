import os
import shutil

class FileManager:
    def __init__(self):
        self.current_directory = os.getcwd()

    def create_folder(self, folder_name):
        folder_path = os.path.join(self.current_directory, folder_name)
        try:
            os.mkdir(folder_path)
            print(f"Folder '{folder_path}' created successfully.")
        except FileExistsError:
            print(f"Error: The folder '{folder_path}' already exists.")


    def files_in_folder(self):
        try:
            contents = os.listdir(self.current_directory)
            return contents
        except FileNotFoundError:
            print(f"Error: The folder '{self.current_directory}' does not exist.")
            return []


    def delete_folder(self, folder_name):
        folder_path = os.path.join(self.current_directory, folder_name)
        try:
            shutil.rmtree(folder_path)
            print(f"Folder '{folder_path}' removed successfully.")
        except FileNotFoundError:
            print(f"Error: The folder '{folder_path}' does not exist.")
 

    def move_file(self, src, dest):
        try:
            shutil.move(src, dest)
            print(f"File '{src}' moved to '{dest}'.")
        except FileNotFoundError:
            print(f"Error: The source file '{src}' does not exist.")


    def list_files_in_folder(self, folder_path):
        try:
            contents = os.listdir(folder_path)
            return contents
        except FileNotFoundError:
            print(f"Error: The folder '{folder_path}' does not exist.")
            return []


