import os
import requests
from datetime import datetime, date

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

# write header
file2 = open(headerfile, "r")
header = file2.readlines()
file2.close
file1 = open(indexfile, "w")
file1.writelines(header)


# read folders, and write to README.md
entries = os.listdir(pathtoplugins)
entries = sorted(entries)
for entry in entries:
	withdots = entry.replace(" ", ".")
	forweb  = entry.replace(" ", "%20")

	# get description out of about.txt
	file2 = open(pathtoplugins + entry + "/about.txt" , "r")
	description = file2.readlines()
	description = [item.replace("github.com/zuckung/endless-sky-plugins", "") for item in description]
	file2.close
          
	# get last modified date from the assetfiles
	response = requests.head(assetfiles + withdots + ".zip", allow_redirects=True)
	modif = response.headers['Last-Modified']
	datetime_object = datetime.strptime(modif, '%a, %d %b %Y %H:%M:%S %Z')
	modif = str(datetime_object.date())

	# get file size of the assetfiles in kb or mb
	assetsize = int(response.headers['Content-Length']) / 1024
	form = " kb"
	if assetsize > 1024 :
		assetsize = assetsize / 1024
		form = " mb"
	
	# write the plugin informations to README.md
	file1.writelines("### " + entry + "\n")
	file1.writelines("[" + withdots + ".zip](" + assetfiles + withdots + ".zip) | ")
	file1.writelines(str(round(assetsize, 2)) + form)    
	file1.writelines(" | last modified: " + modif + "\n")
	file1.writelines(" | [view files](" + pluginurl + forweb + "/) <br>\n")
	file1.writelines(description)
	file1.writelines("\n \n")
	
	print(entry + " DONE")
file1.close
