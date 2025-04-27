import os
import shutil
import requests
from datetime import datetime, date
from PIL import Image



def check_local():
	# for local testing
	# get the path to the plugins, this is the %pluginurl% (pluginurl) variable, useable in the template.txt
	if os.getcwd() == '/storage/emulated/0/Download/mgit/endless-sky-plugins/res/src':
		os.chdir('../../')
		current_repo = 'zuckung/endless-sky-plugins'
		pluginurl = 'https://github.com/zuckung/endless-sky-plugins/tree/main/myplugins/'
	else:
		current_repo = os.environ['CUR_REPO']
		pluginurl = 'https://github.com/' + current_repo + '/tree/main/myplugins/'
	return pluginurl, current_repo


def make_imagemd(name, current_repo):
	# get images
	graphicFiles = []
	for root, dirs, files in os.walk('myplugins/' + name + '/', topdown=True):
		for file in files:
			if file.endswith('.png') or file.endswith('.jpg'):
				graphicFiles.append(os.path.join(root, file))
	graphicFiles.sort()
	# write images md
	if len(graphicFiles) > 0:
		if not os.path.isdir('res/imagemd/'):
			os.mkdir('res/imagemd/')
		with open('res/imagemd/' + name + '.md', 'w') as target:
			pos = 0
			target.writelines('graphic files for the plugin: ' + name + '<br>\n<br>\n')
			target.writelines('<table>\n')
			for file in graphicFiles:
				last = file.split('/')[len(file.split('/')) - 1]
				with Image.open(file) as im:
					width, height = im.size
				if width > 200 or height > 200:
					if width > height:
						pic = '		<td><a href="https://github.com/' + current_repo + '/blob/main/' + file \
						+ '"><img src="https://raw.githubusercontent.com/' + current_repo + '/refs/heads/main/' + file + '" width="200"></a><br>\n'
					else:
						pic = '		<td><a href="https://github.com/' + current_repo + '/blob/main/' + file \
						+ '"><img src="https://raw.githubusercontent.com/' + current_repo + '/refs/heads/main/' + file + '" height="200"></a><br>\n'
				else:
					pic = '		<td><a href="https://github.com/' + current_repo + '/blob/main/' + file \
					+ '"><img src="https://raw.githubusercontent.com/' + current_repo + '/refs/heads/main/' + file + '" width="' + str(width) \
					+ '" height="' + str(height) + '"></a><br>\n'	
				pic2 = '		' + last + ' [' + str (width) + 'x' + str(height) + ']</td>\n'
				pos += 1
				if pos%3 == 1%3:
					target.writelines('	<tr valign="bottom">\n')
					target.writelines(pic)
					target.writelines(pic2)
				elif pos%3 == 2%3:
					target.writelines(pic)
					target.writelines(pic2)
				elif pos%3 == 3%3:
					target.writelines(pic)
					target.writelines(pic2)
					target.writelines('	</tr>\n')
			if pos%3 == 1%3:
				target.writelines('		<td></td>\n')
				target.writelines('		<td></td>\n')
				target.writelines('	</tr>\n')
			elif pos%3 == 2%3:
				target.writelines('		<td></td>\n')
				target.writelines('	</tr>\n')
			target.writelines('</table>\n')
		link = '<a href="res/imagemd/' + name + '.md">view images</a> [' + str(pos) + ']'
	else:
		link = 'N/A'
	print(name + '.md with all images written to res/imagemd/')
	return link


def make_readme(templatefile, pathtoplugins, indexfile, pluginurl, current_repo):
	# useable variables inside template.txt:
	# %news%           html table of the news
	# %pluginlist%     html table of anchor links to the plugins
	# %name%           the plugin name
	# %icon%           html img with plugin icon url
	# %assetfile%      release zip name of the plugin, special chars and spaces are replaced by dots
	# %assetfullpath%  url to the plugin release
	# %size%           plugin size in mb or kb, or 'N/A' if no release found
	# %lastmodified%   last modified date of the plugin release zip file, or 'N/A' if no release found
	# %pluginurl%      url path to the plugin folder
	# %pluginnameurl%  plugin folder name, with space replaced by %20
	# %imagemd%        html link to a seperate plugin md file with all images of that plugin
	# %description%    content of the plugin's' plugin.txt or about.txt, or 'N/A' if none found
	# %readme%         content of the plugin's' README.md or 'N/A' if none found
	# %screenshots%    html table of the plugin screenshots from the screenshot folder, or '' if none found
	# %version%        version number

	# read templates
	with open(templatefile, 'r') as file1:
		template = file1.read()
	header = template.split('%plugin template below this line%')[0]
	p_template =  template.split('%plugin template below this line%')[1]
	# creating the news table, this will be the %news% (news) variable in template.txt
	with open('res/news.txt') as file1:
		allnews = file1.readlines()
	news = ''
	amount = 0
	for each in allnews:
		each = each.replace('\n', '')
		amount += 1
		if amount <= 10: # amount of entries shown
			news += each + '<br>\n'
		else:
			break
	news = '## Latest News:\n<table>\n<tr>\n<td><img width="882" height="1"><br>\n' + news + '<img width="882" height="1"><br>\n</td>\n</tr>\n</table>\n'
	# creating plugin list table, this will be the %pluginlist% (pluginlist) variable
	entries = os.listdir(pathtoplugins)
	entries = sorted(entries)
	pluginlist = '<table>\n<tr valign="top">\n<td><img width="294" height="1"><br>\n'
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
	# writes the template header to the README.md
	with open(indexfile, 'w') as file1:
		file1.writelines(header.replace('%pluginlist%', pluginlist).replace('%news%', news))
	print('README.md header WRITTEN!')
	# read plugin folders, and create a plugin view for each
	entries = os.listdir(pathtoplugins)
	entries = sorted(entries)
	screenshots = os.listdir('screenshots' + os.sep)
	screenshots = sorted(screenshots)
	for entry in entries:
		withdots = entry.replace(' ', '.')
		# this is the %pluginnameurl% (forweb) variable, currently only replacing spaces
		forweb  = entry.replace(' ', '%20')
		pa_template = p_template
		# checking for screenshots, this will be the %screenshot% (screenshotcode) variable
		screenshotlist = []
		screenshotcode = ''
		screenpos = 0
		for screenshot in screenshots:
			if screenshot.startswith(entry):
				if len(screenshot) - 6 == len(entry):
					screenshotlist.append(screenshot)
		if len(screenshotlist) > 0:
			screenshotcode += '<br>\nscreenshots(click to enlarge):<br>\n<table>\n'
			for screenshot in screenshotlist:
				screenpos += 1
				if screenpos%3 == 1%3:
					screenshotcode += '\t<tr>\n\t\t<td>'
					screenshotcode += '<img src="https://raw.githubusercontent.com/' + current_repo + '/master/screenshots/' + screenshot + '" width="200">'
					screenshotcode += '</td>\n'
				elif screenpos%3 == 2%3:
					screenshotcode += '\t\t<td>'
					screenshotcode += '<img src="https://raw.githubusercontent.com/' + current_repo + '/master/screenshots/' + screenshot + '" width="200">'
					screenshotcode += '</td>\n'
				elif screenpos%3 == 3%3:
					screenshotcode += '\t\t<td>'
					screenshotcode += '<img src="https://raw.githubusercontent.com/' + current_repo + '/master/screenshots/' + screenshot + '" width="200">'
					screenshotcode += '</td>\n\t</tr>\n'
			if not len(screenshotlist)%3 == 3%3:
				screenshotcode = screenshotcode + '\t</tr>\n'
			screenshotcode = screenshotcode + '</table>\n<br>\n'
		# gets the %version% (version_number) variable out of versioning.txt
		with open('res/versioning.txt', 'r') as read_version:
			version_lines = read_version.readlines()
		found = 0
		for vline in version_lines:
			split = vline.split('|')
			if split[0] == withdots:
				version_number = split[1].replace('\n', '')
				found = 1
				break
		if found == 0:
			version_number = '1.0.0'
		# gets the %assetfullpath% (assetfiles) variable
		assetfiles = 'https://github.com/' + current_repo + '/releases/download/v' + version_number + '-' + withdots + '/'
		# gets the %description% (description) variable out of about.txt
		description = ''
		if os.path.isfile(pathtoplugins + entry + '/plugin.txt'):
			with open(pathtoplugins + entry + '/plugin.txt' , 'r') as file1:
				description_list = file1.readlines()
			for line in description_list:
				if line.startswith('about "'):
					pos1 = line.find('"')
					pos2 = line.find('"', pos1+1)
					line = line[pos1+1:pos2]
					description = description + '>' + line + '\n'
		elif os.path.isfile(pathtoplugins + entry + '/about.txt'):
			with open(pathtoplugins + entry + '/about.txt' , 'r') as file1:
				description_list = file1.readlines()
			for line in description_list:
				description = description + '>' + line
		else:
			description = '>N/A'		
		# gets the %readme% (readme) variable out of the plugin readme.md
		readme = ''
		if os.path.isfile(pathtoplugins + entry + '/README.md'):
			with open(pathtoplugins + entry + '/README.md' , 'r') as file1:
				readme_list = file1.readlines()
			for line in readme_list:
				readme = readme + line + '\n' 
		else:
			readme = 'N/A'
		# gets the last modified date from the assetfile, this is the %lastmodified% (modif) variable
		try:
			response = requests.head(assetfiles + withdots + '.zip', allow_redirects=True)
			if response.status_code == 404:
				assetfiles = assetfiles.replace('1.0.0', '1.0')
				response = requests.head(assetfiles + withdots + '.zip', allow_redirects=True)
			modif = response.headers['Last-Modified']
			datetime_object = datetime.strptime(modif, '%a, %d %b %Y %H:%M:%S %Z')
			modif = str(datetime_object.date())
		# gets the file size of the assetfile in kb or mb, this is the %size% (assetsize) variable
			assetsize = int(response.headers['Content-Length']) / 1024
			form = ' kb'
			if assetsize > 1024 :
				assetsize = assetsize / 1024
				form = ' mb'
		except:
			modif = 'N/A'
			form = ''
			assetsize = 'N/A'
		# gets the %icon% (icon) variable, as an html img
		if os.path.isfile(pathtoplugins + entry + '/icon.png'):
			icon = '<img src="' + pathtoplugins + entry + '/icon.png" height="100">'
		else:
			icon = ''
		# create imagemd and return link, this is the %imagemd% (imagemdlink) variable
		imagemdlink = make_imagemd(entry, current_repo)
		# replace template with %variables%
		pa_template = pa_template.replace('%name%', entry)
		pa_template = pa_template.replace('%assetfullpath%', assetfiles)
		pa_template = pa_template.replace('%assetfile%', withdots + '.zip')
		if assetsize != 'N/A':
			pa_template = pa_template.replace('%size%', str(round(assetsize, 2)) + form)
		else:
			pa_template = pa_template.replace('%size%', assetsize)
		pa_template = pa_template.replace('%lastmodified%', modif)
		pa_template = pa_template.replace('%pluginurl%', pluginurl)
		pa_template = pa_template.replace('%pluginnameurl%', forweb)
		pa_template = pa_template.replace('%imagemd%', imagemdlink)
		pa_template = pa_template.replace('%description%', description)
		pa_template = pa_template.replace('%readme%', readme)
		pa_template = pa_template.replace('%icon%', icon)
		pa_template = pa_template.replace('%screenshots%', screenshotcode)
		pa_template = pa_template.replace('%version%', version_number)
		# write index file, appending this plugin entry
		with open(indexfile, 'a') as file1:
			file1.writelines(pa_template)
		print(entry + ' WRITTEN')
	print(indexfile + ' COMPLETE!')	
	# deleting zip from runner, in case release.py is run before this py
	files = os.listdir()
	for file in files:
		if file[len (file)  -3:] == 'zip':
			os.remove(file)
			print('\n' + file + ' REMOVED')
	if os.path.isdir('versioning'):
		shutil.rmtree('versioning')


def run():
	pathtoplugins = 'myplugins/'
	indexfile = 'README.md'
	templatefile = 'res/template.txt'
	pluginurl, current_repo = check_local()
	make_readme(templatefile, pathtoplugins, indexfile, pluginurl, current_repo)


if __name__ == "__main__":
	run()
