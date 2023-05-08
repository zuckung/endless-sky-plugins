import os
import subprocess
import sys

# read paths and files
with open("res/paths.txt") as f:
	for line in f:
		line = str((line.strip()))
		if line.find("pathtoplugins") == 0:	# i.e. pathtoplugins = myplugins/
			pathtoplugins = line.split(" = ")[1]
		elif line.find("indexfile") == 0: 		# i.e.indexfile = README.md
			indexfile = line.split(" = ")[1]
		elif line.find("assetfiles") == 0:	   # i.e. assetfiles = https://github.com/zuckung/test/releases/download/Latest/
 			assetfiles = line.split(" = ")[1]
		elif line.find("pluginurl") == 0:		 # i.e pluginurl = https://github.com/zuckung/test/tree/main/myplugins/
			pluginurl = line.split(" = ")[1]
		elif line.find("header") == 0:			# i.e. headerfile = res/header.txt
			headerfile = line.split(" = ")[1]
		elif line.find("picturefile") == 0:	  # i.e picturefile = res/icon.png
			picturefile = line.split(" = ")[1]
			
# check how deep the path is for os.chdir
pathtopluginsdeepth = pathtoplugins.count("/")
# removing the slash
pathtopluginsw = pathtoplugins[:-1]
 
 # checks for arguments in zipfiles.py call
 # has no arguments
if len(sys.argv) < 2:
	entries = os.listdir(pathtoplugins)
	entries = sorted(entries)
	# for each plugin folder
	for entry in entries:
		os.chdir(pathtoplugins) 
		# checks for spaces in folder and renames it
		if str(entry.find(" ")) != "-1":
			spaced  = entry + "/"
			entry = spaced.replace(" ", ".")
			subprocess.run(["mv", spaced , entry], stdout=subprocess.DEVNULL)
			print("found a folder with spaces in name and renamed it: " + entry)
			
		# zipping
		subprocess.run(["zip", "-r", "../" + entry + ".zip", entry], stdout=subprocess.DEVNULL) 
		os.chdir('../')
		print(entry + " zipping DONE\n")
		subprocess.run(["mv", entry + ".zip", "zip/" + entry + ".zip"], stdout=subprocess.DEVNULL)
		
# has arguments       
else:    
	#formating arguments
	changed = str(sys.argv)
	pos = changed.index(".py', '") + 7
	changed = changed[pos:]
	changed = changed.replace("', '"," ")
	changed = changed.replace("']","")

	# zipping changed
	plugins = set()
	for f in changed.split("%25%25%25"):
		if not pathtopluginsw in f:
			continue
		path = f.split(os.sep)
		index = path.index(pathtopluginsw) + 1
		if index >= len(path):
			continue
		plugins.add(path[index])
		if plugins:
			print("The following plugins have changed:")
			for p in plugins:
				print(p)
				os.chdir(pathtoplugins)
				x = p.replace(" ", ".")
				subprocess.run(["zip", "-r", "../" + x + ".zip", p], stdout=subprocess.DEVNULL)
				for am in range(pathtopluginsdeepth):
					os.chdir('../')
		else:
			print("No plugin changes have been detected.")