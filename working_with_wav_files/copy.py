import os
import sys

start = sys.argv[1]
end = sys.argv[2]
dest = sys.argv[3]

for i in range(int(start), int(end)):
    cmd = 'copy ..\\samples\\' + str(i) + '\\* ' + dest
    print (cmd) 
    os.system(cmd)