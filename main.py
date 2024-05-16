
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