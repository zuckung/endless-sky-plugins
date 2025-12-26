#pylint:disable=E0001
import os

def read_everything(data_folder):
	print('\nreading data folder')
	objs, obj_paths, obj_names = [], [], []
	started = False
	folders = os.listdir(data_folder)
	folders.append('')
	folders.sort()
	for folder in  folders:
		if os.path.isdir(data_folder + folder):
			text_files = os.listdir(data_folder + folder)
			text_files.sort()
			for text_file in text_files:
				if os.path.isfile(data_folder + folder + os.sep + text_file) == False:
					continue
				if len(folder + text_file)  < 80: # just for displaying / max len = 44(currently)
					count = 80 - len(folder + text_file)
					spaces = ''
					for i in range(0, count):
						spaces += ' '
				print('\treading: ' + folder + os.sep + text_file + spaces, end = '\r', flush= True)
				with open(data_folder + folder + os.sep + text_file, 'r') as source_file:
					lines = source_file.readlines()
				index = 0
				for line in lines:
					index += 1
					if line[:1] == '#':
						continue
					elif line == '\n':
						continue
					elif line == '\t\n':
						continue
					elif line == '\t\t\n':
						continue
					elif line[:1] != '\t' or index == len(lines):
						if started == True:
							objs.append(txt) #.replace('<', '&#60;').replace('>', '&#62;'))
							obj_paths.append(txt2)
							obj_names.append(txt3.replace('\t', ' '))
							started = False
						txt = line
						if folder != '':
							folder_fix = folder + os.sep
						else:
							folder_fix = folder
						txt2 = 'data' + os.sep + folder_fix + text_file
						txt3 = line[:len(line)-1]
						started = True
					else:
						if started == True:
							txt += line
	print('	\n\tDONE')
	return objs, obj_paths, obj_names

def recolor_jobs(objs):
	full_text = '' +\
		'# passenger blue\n' +\
		'color "coloring job passenger: selected" 0.30 0.65 0.85 0.\n' +\
		'color "coloring job passenger: unselected" 0.22 0.50 0.65 0.\n' +\
		'color "coloring job passenger: unavailable" 0.14 0.32 0.45 0.\n\n' +\
		'# cargo cyan\n' +\
		'color "coloring job cargo: selected" 0.20 0.75 0.70 0.\n' +\
		'color "coloring job cargo: unselected" 0.18 0.55 0.55 0.\n' +\
		'color "coloring job cargo: unavailable" 0.12 0.32 0.38 0.\n\n' +\
		'# escort yellow\n' +\
		'color "coloring job escort: selected" 0.95 0.80 0.30 0.\n' +\
		'color "coloring job escort: unselected" 0.75 0.65 0.30 0.\n' +\
		'color "coloring job escort: unavailable" 0.50 0.45 0.25 0.\n\n' +\
		'# bounty orange\n' +\
		'color "coloring job bounty: selected" 0.95 0.55 0.20 0.\n' +\
		'color "coloring job bounty: unselected" 0.75 0.45 0.25 0.\n' +\
		'color "coloring job bounty: unavailable" 0.50 0.32 0.22 0.\n\n' +\
		'# mining brown\n' +\
		'color "coloring job mining: selected" 0.60 0.45 0.25 0.\n' +\
		'color "coloring job mining: unselected" 0.45 0.35 0.22 0.\n' +\
		'color "coloring job mining: unavailable" 0.30 0.25 0.18 0.\n\n' +\
		'disable mission\n'
	all_jobs = []
	# get all jobs
	for obj in objs:
		if '	job\n' in obj:
			if not '	color ' in obj: # ignore 65 pirate jobs, already red colored
				all_jobs.append(obj)
	print('\tjobs found: ', str(len(all_jobs)))
	# disable all jobs
	for job in all_jobs:
		pos = job.find('\n')
		name = job[:pos].replace('mission ', '')
		full_text += '	' + name + '\n'
	full_text += '\n'
	# add changed jobs
	uncolored = 0
	uncolored_list = []
	for job in all_jobs:
		pos = job.find('\n')
		firstline = job[:pos]
		name = firstline.replace('"', '').replace('mission ', '')
		# set old mission name done
		oncomplete = '\ton complete\n' +\
			'\t\tset "' + name + ': done"\n' +\
			'\t\tset "' + name + ': offered"\n'
		# decide coloring
		if '	passengers' in job:
			replace = '\nmission "' + name.strip() + ' "\n	color selected "coloring job passenger: selected"\n	color unselected "coloring job passenger: unselected"\n	color unavailable "coloring job passenger: unavailable"'
		elif '	cargo' in job:
			replace = '\nmission "' + name.strip() + ' "\n	color selected "coloring job cargo: selected"\n	color unselected "coloring job cargo: unselected"\n	color unavailable "coloring job cargo: unavailable"'
		elif '	npc accompany save' in job:
			replace = '\nmission "' + name.strip() + ' "\n	color selected "coloring job escort: selected"\n	color unselected "coloring job escort: unselected"\n	color unavailable "coloring job escort: unavailable"'
		elif '	npc kill' in job:
			replace = '\nmission "' + name.strip() + ' "\n	color selected "coloring job bounty: selected"\n	color unselected "coloring job bounty: unselected"\n	color unavailable "coloring job bounty: unavailable"'
		elif '	name "Harvested' in job or 'Asteroid Mining' in job:
			replace = '\nmission "' + name.strip() + ' "\n	color selected "coloring job mining: selected"\n	color unselected "coloring job mining: unselected"\n	color unavailable "coloring job mining: unavailable"'
		else: # no change
			uncolored += 1
			uncolored_list.append(name)
			replace = '\nmission "' + name.strip() + ' "'
			oncomplete = '\ton complete\n'
		# create script text
		full_text += job.replace(firstline, replace).replace('\ton complete\n', oncomplete)
	# list missed jobs
	print('\tuncolored: ', uncolored)
	for each in uncolored_list:
		print('\t\t' + each)
	return full_text

def write_file(full_text):
	with open('coloring.jobs.txt', 'w') as target:
		target.writelines(full_text)
	
	
			


if __name__ == "__main__":
	data_folder = 'C:/Users/woot/AppData/Local/ESLauncher2/instances/release/data/'
	objs, obj_paths, obj_names = read_everything(data_folder)
	full_text = recolor_jobs(objs)
	write_file(full_text)