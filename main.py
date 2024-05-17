import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Dictionary to map file extensions to folder names
    file_types = {
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov'],
        'Music': ['.mp3', '.wav', '.aac', '.flac'],
        'Archives': ['.zip', '.tar', '.gz', '.rar'],
        'Scripts': ['.py', '.sh', '.bat', '.js', '.html', '.css']
    }

    # Create subdirectories if they don't exist
    for folder in file_types:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to appropriate subdirectories
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if filename.lower().endswith(tuple(extensions)):
                    shutil.move(file_path, os.path.join(directory, folder, filename))
                    print(f"Moved: {filename} to {folder}/")
                    moved = True
                    break
            if not moved:
                # Create a 'Others' folder for unrecognized file types
                others_folder = os.path.join(directory, 'Others')
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, os.path.join(others_folder, filename))
                print(f"Moved: {filename} to Others/")

if __name__ == "__main__":
    target_directory = input("Enter the directory to organize: ")
    organize_files(target_directory)
