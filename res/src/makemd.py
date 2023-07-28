import os
import shutil
import requests
from datetime import datetime, date

# for local testing
if os.getcwd() == "/storage/emulated/0/Download/mgit/test/res/src": # check for local testing
	os.chdir("../../")

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
		elif line.find("template") == 0:			# i.e. template = res/template.txt
			templatefile = line.split(" = ")[1]
		elif line.find("picturefile") == 0:	  # i.e picturefile = res/icon.png
			picturefile = line.split(" = ")[1]

# read templates
with open(templatefile, "r") as file1:
	template = file1.read()
header = template.split("%plugin template below this line%")[0]
p_template =  template.split("%plugin template below this line%")[1]


# write header
with open(indexfile, "w") as file1:
	file1.writelines(header)


# read folders, and write to README.md
entries = os.listdir(pathtoplugins)
entries = sorted(entries)
for entry in entries:
	withdots = entry.replace(" ", ".")
	forweb  = entry.replace(" ", "%20")
	pa_template = p_template

	# get description out of about.txt
	with open(pathtoplugins + entry + "/about.txt" , "r") as file1:
		description_list = file1.readlines()
	description = ""
	for line in description_list:
		description = description + ">" + line
		
          
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
	### %name%
# [%name%](%assetfullpath%%assetfile%) | %size% | %lastmodified% | [view files](%pluginurl%%pluginnameurl%/) <br>
# %description% p_template

	pa_template = pa_template.replace("%name%", entry)
	pa_template = pa_template.replace("%assetfullpath%", assetfiles)
	pa_template = pa_template.replace("%assetfile%", withdots + ".zip")
	pa_template = pa_template.replace("%size%", str(round(assetsize, 2)) + form)
	pa_template = pa_template.replace("%lastmodified%", modif)
	pa_template = pa_template.replace("%pluginurl%", pluginurl)
	pa_template = pa_template.replace("%pluginnameurl%", forweb)
	pa_template = pa_template.replace("%description%", description)
	
	
	with open(indexfile, "a") as file1:
		file1.writelines(pa_template)
	
	print(entry + " WRITTEN")
	
# deleting zip from workflow
files = os.listdir()
for file in files:
	if file[len (file)  -3:] == "zip":
		os.remove(file)
		print("\n" + file + " REMOVED")
