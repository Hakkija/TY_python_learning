import os

def file_size(filename):
    if os.path.isfile(filename):
        return os.path.getsize(filename)
    else:
        return 0

def size_convert(file_size):
    if file_size < 1024:
        value = f"{file_size} B"
    elif file_size< 1024**2:
        value = f"{round(file_size/1024, 1)} KB"
    else:
        value = file_size
    return value

def size_string(filename):
    size = file(filename)
    if size > 0:
        return file_size(size)
    else:
        return 0
filename = input("Enter filename: ")
print("File size:", size_string(filename))