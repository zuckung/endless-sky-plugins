# change the path to your data_folder and run the script.
# it generates space.fauna.map.txt with all system definitions 
# and adds the fleet "space fauna 01" with a random spawn time.


import os
import random


def set_globals():
	print('setting global variables')
	global data_folder
	global obj
	global obj_path
	global obj_name
	global systems_empty
	global systems_land
	obj, obj_path, obj_name, systems_empty, systems_land = [], [], [], [], []
	data_folder = '/storage/9C33-6BBD/endless sky/data/' # change to your folder

	
def read_everything():
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
				print('reading: ' + folder + os.sep + text_file + spaces, end = '\r', flush= True)
				with open(data_folder + folder + os.sep + text_file, 'r') as source_file:
					lines = source_file.readlines()
				for line in lines:
					if line[:1] == '#':
						continue
					elif line == '\n':
						continue
					elif line == '\t\n':
						continue
					elif line == '\t\t\n':
						continue
					elif line[:1] != '\t':
							if started == True:
								obj.append(txt.replace('<', '&#60;').replace('>', '&#62;'))
								obj_path.append(txt2)
								obj_name.append(txt3.replace('\t', ' '))
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


def list_systems():
	for each in obj_name:
		if each.startswith('system '):
			index = obj_name.index(each)
			text = obj[index]
			pos = text.find('object ', 0)
			if not pos > 0: # no landable objects
				systems_empty.append(each)
				continue
			elif pos > 0: # landable objects
				systems_land.append(each)
				continue
		
def write_list():
	with open('space.fauna.map.txt', 'w') as target:
		target.writelines('# for systems WITHOUT landable planets the fleet spawn is between 6.000 and 12.000\n') # 100 - 200 seconds
		target.writelines('# for systems WITH landable planets the fleet spawn is between 12.000 and 24.000\n') # 200 - 400 seconds
		target.writelines('# systems without landable planets:\n')
		for each in systems_empty:
			target.writelines(each + '\n')
			target.writelines('\tadd fleet "space fauna 01" ' + str(random.randrange(6000, 12000, 1)) + '\n')
		target.writelines('# systems with landable planets:\n')
		for each in systems_land:
			target.writelines(each + '\n')
			target.writelines('\tadd fleet "space fauna 01" ' + str(random.randrange(12000, 24000, 1)) + '\n')


def run():
	set_globals()
	read_everything()
	list_systems()
	write_list()


if __name__ == "__main__":
	run()