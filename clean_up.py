import os
import shutil
import sys
import tkinter
from tkinter import filedialog
#  ! Test
def get_user_documents_path():
    return os.path.join(os.path.expanduser("~"), "Documents")

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
    else:
        print("Path Exists")

def organize_files(source_dir, user_documents_path):
    os.chdir(source_dir)
    print(os.getcwd())

    directories = {
        "audio": "audio",
        "video": "video",
        "images": "images",
        "docs": "docs",
        "undefined": "undefined",
    }

    for directory in directories.values():
        create_directory_if_not_exists(os.path.join(user_documents_path, directory))

    file_types = {
        "audio": (".3ga", ".aac", ".ac3", ".aif", ".aiff", ".alac", ".amr", ".ape", ".au", ".dss", ".flac", ".flv", ".m4a", ".m4b", ".m4p", ".mp3", ".mpga", ".ogg", ".oga", ".mogg", ".opus", ".qcp", ".tta", ".voc", ".wav", ".wma", ".wv"),
        "video": (".webm", ".MTS", ".M2TS", ".TS", ".mov", ".mp4", ".m4p", ".m4v", ".mxf"),
        "images": (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", ".gif", ".webp", ".svg", ".apng", ".avif"),
        "docs": (".docx", ".txt", ".pdf", ".pptx"),
        "junk": (".zip", ".exe", ".msi", ".7z", ".xlsx", ".dll", ".fx", ".rar"),
    }

    def is_file_type(file, file_type):
        return os.path.splitext(file)[1] in file_types.get(file_type, ())

    for file in os.listdir(source_dir):
        for directory, file_type in directories.items():
            if is_file_type(file, file_type):
                destination = os.path.join(user_documents_path, directory)
                shutil.move(file, destination)
                break
        else:
            if file in os.listdir(os.path.join(user_documents_path, "undefined")):
                print(f"{file} Already Exists Here")
            else:
                shutil.move(file, os.path.join(user_documents_path, "undefined"))

def main():
    tkinter.Tk().withdraw()
    source_directory = filedialog.askdirectory()
    user_documents_path = get_user_documents_path()

    if not os.path.exists(source_directory):
        print("Invalid Directory")
        sys.exit()

    execute = input(f"Are you sure you want to organize {source_directory} (y/n): ").lower()

    if execute == "y":
        organize_files(source_directory, user_documents_path)
    elif execute == "n":
        sys.exit()
    else:
        sys.exit()

if __name__ == "__main__":
    main()
