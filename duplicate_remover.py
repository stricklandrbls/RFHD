import sys
import hashlib
import os

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
files_hashed = {}
files_to_remove = []

def load_file_hashes():
    print("Loading file & hash pairs...")
    files = os.listdir()
    for f in files:
        #print(f'\n{f}\n')
        if f != '.lostfound':
            if '.jpg' in f:
                files_hashed[f] = hash(f)
    #print(files_hashed)

def minimalize():
    print("Reducing file/hash pair dictionary...")
    for key in files_hashed:
        index_hash = hash(key)
        for duplicate in files_hashed:
            if(index_hash == files_hashed[duplicate]):
                print(f"Removing {duplicate}...")
                files_to_remove.append(duplicate)
                #files_hashed.pop(duplicate)
def remove_files():
    for f in files_to_remove:
        print(f'Removing file {f}...')
        os.remove(f)

def hash(file):

    md5 = hashlib.md5()
    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)

    return format(md5.hexdigest())

## Star Script
load_file_hashes()
minimalize()
remove_files()