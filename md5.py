import hashlib
import os

def md5_for_file(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

with open('md5.txt', 'w') as f:
    for filename in os.listdir('.'):
        if os.path.isfile(filename):
            md5 = md5_for_file(filename)
            f.write(f'{filename}: {md5}\n')
