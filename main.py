# Stage 1/4: Here come the files
import sys
import os

#print(os.getcwd())
args = sys.argv
if len(args) == 1:
    print("Directory is not specified")
else:
    for root, dirs, files in os.walk(args[1], topdown=True):
        for name in files:
            print(os.path.join(root, name))
        # for name in dirs:
        #    print(os.path.join(root, name))
