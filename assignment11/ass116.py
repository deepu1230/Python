import os

def check_file_permissions(filename):
    if os.access(filename, os.R_OK):
        print(f"{filename} has read access")
    else:
        print(f"{filename} does not have read access")

    if os.access(filename, os.W_OK):
        print(f"{filename} has write access")
    else:
        print(f"{filename} does not have write access")

check_file_permissions('example.txt')