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

# reading news.txt
with open('res/news.txt') as file1:
	allnews = file1.readlines()
news = ''
amount = 0
for each in allnews:
	each = each.replace('\n', '')
	amount += 1
	if amount <= 10:
		news += each + '<br>\n'
	else:
		break
news = '## Latest News:\n<table><tr><td><img width="882" height="1"><br>' + news + '<img width="882" height="1"><br></td></tr></table>'

# write header
entries = os.listdir(pathtoplugins)
entries = sorted(entries)
pluginlist = '<table><tr valign="top"><td><img width="294" height="1"><br>\n'
amount = len(entries)
column = amount//3
remainder = amount%3
index = 0
for entry in entries:
	index += 1
	pluginlist += '<a href="' + indexfile + '#' + entry.replace('.','') + '">' + entry + '</a><br>\n'
	if remainder == 0:
		if index  == column or index == 2*column:
			pluginlist += '<img width="294" height="1"><br></td><td><img width="294" height="1"><br>\n'
	elif remainder == 1:
		if index == column +1 or index == 2*column +1:
			pluginlist += '<img width="294" height="1"><br></td><td><img width="294" height="1"><br>\n'
	elif remainder == 2:
		if index == column +1 or index == 2*column +2:
			pluginlist += '<img width="294" height="1"><br></td><td><img width="294" height="1"><br>\n'
pluginlist += '<img width="294" height="1"><br></td></tr></table>\n'
with open(indexfile, "w") as file1:
	file1.writelines(header.replace('%pluginlist%', pluginlist).replace('%news%', news))


# read folders, and write to README.md
entries = os.listdir(pathtoplugins)
entries = sorted(entries)
for entry in entries:
	withdots = entry.replace(" ", ".")
	forweb  = entry.replace(" ", "%20")
	pa_template = p_template
	
	# get version number
	with open('res/versioning.txt', 'r') as read_version:
		version_lines = read_version.readlines()
	for vline in version_lines:
		split = vline.split('|')
		if split[0] == withdots:
			version_number = split[1].replace('\n', '')
			break

	# get description out of about.txt
	# https://github.com/zuckung/endless-sky-plugins/releases/download/v1.0.1-landing.images.android/landing.images.android.zip
	assetfiles = 'https://github.com/zuckung/endless-sky-plugins/releases/download/' + version_number + '-' + withdots + '/'
	with open(pathtoplugins + entry + "/about.txt" , "r") as file1:
		description_list = file1.readlines()
	description = ""
	for line in description_list:
		description = description + ">" + line
		
	# get readme.md
	with open(pathtoplugins + entry + "/README.md" , "r") as file1:
		readme_list = file1.readlines()
	readme = ""
	for line in readme_list:
		readme = readme + line + "\n"
          
	# get last modified date from the assetfiles
	try:
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
	except:
		modif = 'N/A'
		form = ''
		assetsize = 'N/A'
	if os.path.isfile(pathtoplugins + entry + '/icon.png'):
		icon = '<img src="' + pathtoplugins + entry + '/icon.png" height="100">'
	else:
		icon = ''
	# write the plugin informations to README.md
	### %name%
	# [%name%](%assetfullpath%%assetfile%) | %size% | %lastmodified% | [view files](%pluginurl%%pluginnameurl%/) <br>
	# %description% p_template

	pa_template = pa_template.replace("%name%", entry)
	pa_template = pa_template.replace("%assetfullpath%", assetfiles)
	pa_template = pa_template.replace("%assetfile%", withdots + ".zip")
	if assetsize != 'N/A':
		pa_template = pa_template.replace("%size%", str(round(assetsize, 2)) + form)
	else:
		pa_template = pa_template.replace("%size%", assetsize)
	pa_template = pa_template.replace("%lastmodified%", modif)
	pa_template = pa_template.replace("%pluginurl%", pluginurl)
	pa_template = pa_template.replace("%pluginnameurl%", forweb)
	pa_template = pa_template.replace("%description%", description)
	pa_template = pa_template.replace("%readme%", readme)
	pa_template = pa_template.replace("%icon%", icon)
	
	
	with open(indexfile, "a") as file1:
		file1.writelines(pa_template)
	
	print(entry + " WRITTEN")
	
# deleting zip from workflow
files = os.listdir()
for file in files:
	if file[len (file)  -3:] == "zip":
		os.remove(file)
		print("\n" + file + " REMOVED")

if os.path.isdir('versioning'):
	shutil.rmtree('versioning')
