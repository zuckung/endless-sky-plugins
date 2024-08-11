import os
import subprocess
from datetime import datetime
import sys


def blub():
	for f in changed.split("%%%"):
		if not "myplugins" in f:
			continue
		path = f.split(os.sep)
		index = path.index("myplugins") + 1
		if index >= len(path):
			continue
		plugins.add(path[index])
	if plugins:
		print("The following plugins have changed:")
		for p in plugins:
			print(p)
			os.chdir('myplugins/')
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
			subprocess.run(["zip", "-r", "../" + corrected + ".zip", p],
				stdout=subprocess.DEVNULL)
			# versioning
			if not os.path.isdir('../versioning'):
				os.mkdir('../versioning')
			with open('../res/versioning.txt', 'r') as vfile:
				lines = vfile.readlines()
				newlines = []
				found = 0
				for line in lines:
					linesplit = line.split('|')
					if linesplit[0] == corrected:
						found = 1
						part = ''
						old_version = linesplit[1]
						osplit = old_version.split('.')
						new_version = str(int(osplit[len(osplit)-1]) + 1)
						for x in range(0, len(osplit)-1):
							part += osplit[x] + '.'
						new_version = part + new_version
						print(corrected + ' ' + old_version + ' to ' + new_version)
						line = corrected + '|' + new_version + '\n'
					newlines.append(line)
				if found == 0:
					newlines.append(corrected + '|1.0.0' + '\n')
					new_version = '1.0.0'
			with open('../res/versioning.txt', 'w') as target:
				newlines.sort()
				target.writelines(newlines)
			subprocess.run(["zip", "-r", "../versioning/" + corrected + ".zip", p],
				stdout=subprocess.DEVNULL)
			env_file = os.getenv('GITHUB_ENV')
			with open(env_file, "a") as myfile:
				myfile.write("UPDATE_TAG=v" + new_version + '-'  + corrected + '\n')
				myfile.write("UPDATE_TAG2="+ corrected + '-v' + new_version + '\n')
                
			os.chdir('../')
			# writing to news
			today = datetime.today().strftime('%Y-%m-%d')
			news = [today + ' | update: ' + p + '\n']
			with open('res/news.txt') as newsfile:
				old = newsfile.readlines()
			double = False
			for line in old:
				if line == news[0]:
					double = True
					print('double entry! NOT adding to news!')
					break
			if double == False:
				with open('res/news.txt', 'w') as newsfile:
					newsfile.writelines(news + old)
	else:
		print("No plugin changes have been detected.")


changedlist = sys.argv # ['res/src/zip.py', 'myplugins/additional.command.buttons.radial/README.md']
plugins = set()
changedlist.pop(0)
changed = ''
for i in range(0, len(changedlist)):
	print(i)
	changed += changedlist[i]
print(changed)

blub()
