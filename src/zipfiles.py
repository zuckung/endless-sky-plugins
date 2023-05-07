import os
import subprocess
import sys

# formating arguments
changed = str(sys.argv)
pos = changed.index(".py', '") + 7
changed = changed[pos:]
changed = changed.replace("', '"," ")
changed = changed.replace("']","")
print("arguments are : " + changed)


plugins = set()
for f in changed.split("%25%25%25"):
    if not "myplugins" in f:
        continue
    path = f.split(os.sep)
    index = path.index("myplugins") + 1
    if index >= len(path):
        continue
    plugins.add(path[index])
    if plugins:
        print("The following plugins have changed:")
        for p in plugins:
            print(p)
            os.chdir('myplugins/')
            x = p.replace(" ", ".")
            subprocess.run(["zip", "-r", "../" + x + ".zip", p], stdout=subprocess.DEVNULL)
            os.chdir('../')
    else:
        print("No plugin changes have been detected.")
