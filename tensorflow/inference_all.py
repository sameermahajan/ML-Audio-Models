from os import walk
import sys
import inference

folder = sys.argv[1]

files = next(walk(folder), (None, None, []))[2]
print (files)

for file in files:
    f = folder + "\\" + file
    # print (f)
    inference.main(f)