import os
import subprocess
from datetime import datetime


def check_spelling(plugin):
	if not os.path.isdir('myplugins/' + plugin + '/'):
		print('There is no plugin: "' + plugin + '"')
		print('failing workflow now!')
		fail_workflow


def correct_characters(p):
	corrected = p.replace(" ", ".")
	corrected = corrected.replace("'", ".") 
	corrected = corrected.replace(",", ".") 
	corrected = corrected.replace("(", ".") 
	corrected = corrected.replace(")", ".") 
	corrected = corrected.replace("&", ".") 
	corrected = corrected.replace(",", ".") 
	corrected = corrected.replace("...", ".")
	corrected = corrected.replace("..", ".") 
	if corrected[len(corrected)-1] == ".":
		corrected = corrected[:len(corrected)-1]
	return corrected

def create_zip(p, corrected):
	os.chdir('myplugins/')
	subprocess.run(["zip", "-r", "../" + corrected + ".zip", p], stdout=subprocess.DEVNULL)

def versioning(p, corrected):
	# read all versions
	if not os.path.isdir('../versioning'):
		os.mkdir('../versioning')
	with open('../res/versioning.txt', 'r') as vfile:
		lines = vfile.readlines()
	# find right version for plugin
	newlines = []
	found = 0
	for line in lines:
		linesplit = line.split('|')
		if linesplit[0] == corrected:
			found = 1
			part = ''
			old_version = linesplit[1]
			osplit = old_version.split('.')
			new_version = str(int(osplit[len(osplit)-1]) + 1) # new_version = last number + 1
			for x in range(0, len(osplit)-1): # part = first part of version - last number
				part += osplit[x] + '.'
			new_version = part + new_version
			print(corrected + ' ' + old_version + ' to ' + new_version)
			line = corrected + '|' + new_version + '\n' # complete updated line
		newlines.append(line)
	if found == 0: # if new plugin, without version number
		newlines.append(corrected + '|1.0.0' + '\n')
		new_version = '1.0.0'
	with open('../res/versioning.txt', 'w') as target: # write back all versions
		newlines.sort()
		target.writelines(newlines)
	subprocess.run(["zip", "-r", "../versioning/" + corrected + ".zip", p], stdout=subprocess.DEVNULL)
	env_file = os.getenv('GITHUB_ENV') # write environment variables, for use in realease action
	with open(env_file, "a") as myfile:
		myfile.write("UPDATE_TAG=v" + new_version + '-'  + corrected + '\n')
		myfile.write("UPDATE_TAG2="+ corrected + '-v' + new_version + '\n')
	os.chdir('../')

def write_news(p):
	today = datetime.today().strftime('%Y-%m-%d')
	news = [today + ' | update: ' + p + '\n']
	with open('res/news.txt') as newsfile:
		old = newsfile.readlines()
	double = False
	for line in old: # check if today the same plugin got updated, and if so, don't add it again
		if line == news[0]:
			double = True
			print('double entry! NOT adding to news!')
			break
	if double == False: # if not, then write
		with open('res/news.txt', 'w') as newsfile:
			newsfile.writelines(news + old)


def run():
	p = os.environ['INPUT_STORE'] # plugin.name
	check_spelling(p)
	corrected = correct_characters(p) # correct characters that get changed by github release
	create_zip(p, corrected)
	versioning(p, corrected)
	write_news(p)

if __name__ == "__main__":
	run()


