# designed for Endless Sky PRs
# downloads changed files of a PR
# just change PRurl variable and start
# the script downloads all files and puts them into the right folders
# with that it is possible to get a content PR into a plugin


import json
import requests
import os
import shutil


def set_var():
	global username
	global token
	global PRurl
	global files
	username = '' # insert your github name, increases the api request limit, most of the time not needed
	token = '' # insert your github token,  increases the api request limit, most of the time not needed
	PRurl = 'https://github.com/endless-sky/endless-sky/pull/9172' # i.e. 'https://github.com/endless-sky/endless-sky/pull/8949'

		
def get_files():
	# cut PRurl
	splitted = PRurl.split('/')
	repo = splitted[3] + '/' + splitted[4]
	PR = splitted[6]
	# get file urls from github api
	count = 0
	for i in range(1, 100):
		if username == '' or token == '':
			response = requests.get('https://api.github.com/repos/' + repo + '/pulls/' + PR + '/files?page=' + str(i) + '&per_page=100')
		else:
			response = requests.get('https://api.github.com/repos/' + repo + '/pulls/' + PR + '/files?page=' + str(i) + '&per_page=100', auth=(username, token))
		data = response.json()
		if len(data) == 0:
			break 
		# for each file
		for obj in data:
			count += 1
			blob_url = obj['blob_url'].replace('blob', 'raw')
			splitted = obj['blob_url'].split('/')
			path = splitted[7].replace('%2F', os.sep).replace('%20', ' ').replace('%2B', '+').replace('%7E', '~').replace('%40', '@') # gives the folder structure i.e. images/ship/ship1.png
			path = path.replace('/', os.sep)
			print('downloading file ' + str(count) + ': ' + path)
			os.makedirs(os.path.dirname(PR + os.sep + path), exist_ok=True)
			# download the file
			with open(PR + os.sep + path, "wb") as target:
				r = requests.get(blob_url, allow_redirects=True, stream = True)
				r.raw.decode_content = True
				shutil.copyfileobj(r.raw, target)
				

def run():
	set_var()
	get_files()


if __name__ == "__main__":
	run()