import os
import requests
from datetime import datetime, date

pathtoplugins = "myplugins/"
indexfile = "README.md"
assetfiles = "https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/"
pluginurl = "https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/"
header = "src/header.file"

# write header
file2 = open(header, "r")
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
