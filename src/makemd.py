import os
import requests
import datetime

pathtoplugins = "myplugins/"
indexfile = "README.md"
assetfiles = "https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/"
pluginurl = "https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/"
header = "src/header.file"

# write header
file1 = open(indexfile, "w")
file2 = open(header, "r")
file1.writelines(file2.readlines())
file2.close

# read folders, and write to README.md
entries = os.listdir(pathtoplugins)
entries = sorted(entries)
for entry in entries:
	withdots = entry.replace(" ", ".")
	forweb  = entry.replace(" ", "%20")
	file1.writelines("### " + entry + "\n")
	file1.writelines("[" + withdots + ".zip](" + assetfiles + withdots + ".zip) ")
           
	response = requests.head(assetfiles + withdots + ".zip", allow_redirects=True)
	modif = response.headers['Last-Modified']
	modif = datetime.strptime(modif, '%a, %d %b %Y %H:%M:%S %Z').date()
	
	
	size = int(response.headers['Content-Length']) / 1024
	f = " kb"
	if size > 1024 :
		size = size / 1024
		f = " mb"
	file1.writelines(str(round(size, 2)) + f) 
          
	file1.writelines(" | \n[view data](" + pluginurl + forweb + "/data/) | last modified: " + modif + "<br>\n")
	file2 = open(pathtoplugins + entry + "/about.txt" , "r")
	x = file2.readlines()
	x = [item.replace("github.com/zuckung/endless-sky-plugins", "") for item in x]
	file1.writelines(x)
	file1.writelines("\n \n")
	file2.close
	print(entry + " DONE")
file1.close
