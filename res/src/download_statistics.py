import requests
import os
from datetime import datetime
import json



def set_var():
	global username
	global token
	global repo
	username = ''
	token = ''
	repo = os.environ['CUR_REPO']

def get_date():
	now = datetime.now()
	date_time = now.strftime('%Y-%m-%d')
	return date_time

def analyze_write():
	rcount = 0
	downloads = 0
	plugins = []
	pcount = []
	if not os.path.isdir('res/dl_log/'):
		os.makedirs('res/dl_log/')
	with open('res/dl_log/' + get_date() + '.txt', 'w') as target:
		target.writelines('# DOWNLOADS FOR EACH RELEASE:\n')
		for i in range(1, 100): # call api for felease downloads, max 100 times if needed
			if username == '' or token == '':
				response = requests.get('https://api.github.com/repos/' + repo + '/releases?page=' + str(i) + '&per_page=100')
			else:
				response = requests.get('https://api.github.com/repos/' + repo + '/releases?page=' + str(i) + '&per_page=100', auth=(username, token))
			data = response.json()	
			if len(data) == 0:
				break
			for obj in data: # each data has max 100 releases
				rcount += 1 # number of releases
				rname = obj['tag_name']
				rdownload = obj['assets'][0]["download_count"] # number of downloads for each release 
				if rname == 'Latest':
					break
				if rname.split('-', 1)[1] in plugins:
					index = plugins.index(rname.split('-', 1)[1])
					icount = pcount[index]
					icount += rdownload
					pcount[index] = icount
				else:
					plugins.append(rname.split('-', 1)[1])
					pcount.append(rdownload)
				target.writelines(rname + ' | downloads: ' + str(rdownload) + '\n')
				downloads += rdownload
		target.writelines('\n\n')
		target.writelines('# NUMBER OF RELEASES: ' + str(rcount) + '\n')
		target.writelines('# TOTAL DOWNLOADS: ' + str(downloads) + '\n\n\n')
		target.writelines('# TOTAL DOWNLOAD NUMBER FOR EACH PLUGIN:\n')
		for each in plugins:
			index = plugins.index(each)
			plugins[index] = each + ' ' + str(pcount[index])
		plugins.sort()
		for each in plugins:
			index = plugins.index(each)
			target.writelines(each + '\n')
set_var()
analyze_write()
