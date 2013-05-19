
import os

def write_file(file_):
    if not os.path.exists(file_):
        open(file_, 'w').close()

def macster(path):
    for root, sub_directories, files in os.walk(path):
        write_file(os.path.join(root, '.DS_Store'))
        for sub_directory in sub_directories:
            write_file(os.path.join(root, sub_directory, '.DS_Store'))

if __name__=="__main__":
    macster(".")

