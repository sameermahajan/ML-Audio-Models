import os
import sys

start = sys.argv[1]
end = sys.argv[2]
step = sys.argv[3]
dest = sys.argv[4]

for i in range(int(start), int(end), int(step)):
    cmd = 'copy ..\\samples\\' + str(i) + '\\* ' + dest
    print (cmd) 
    os.system(cmd)