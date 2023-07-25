from hashlib import sha1
import sys
import os

def unique_hash(file_path: str, block_size: int = 2**20) -> str:
    """ Small function to generate a hash to uniquely generate
    a file. Inspired by MD5 version here:
    http://stackoverflow.com/a/1131255/712997

    Works with large files.

    :param file_path: path to file.
    :param block_size: read block size.
    :return: a hash in an hexagesimal string form.
    """
    s = sha1()
    with open(file_path, "rb") as f:
        while True:
            buf = f.read(block_size)
            if not buf:
                break
            s.update(buf)
    return s.hexdigest().upper()

dirname = sys.argv[1]
file_list = os.listdir(dirname)
print (file_list)

print(dirname)

for file in file_list:
    print (file)
    hash = unique_hash(dirname + "\\" + file)
    print(file, hash)
