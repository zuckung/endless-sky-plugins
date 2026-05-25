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
					elif line[:1] != '\t' or index == len(lines)+1:
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


def change_fleets(objs, blacklisted):
	def get_personality(obj):
		started = False
		personality_lines = ''
		lines = obj.split('\n')
		for line in lines:
			if line.startswith('\tpersonality'):
				started = True
				personality_lines += line + '\n'
				continue
			if started == True:
				if line.startswith('\t\t'):
					personality_lines += line + '\n'
				else:
					started = False
		return personality_lines
	allfleets, disablefleets, modfleets = [], [], []
	# get all fleets and modify if neccessary
	for obj in objs:
		if obj.startswith('fleet '):
			found_blacklisted = False
			allfleets.append(obj) # counting all fleets
			for black in blacklisted:
				if black in obj:
					found_blacklisted = True
					break
			if found_blacklisted == True:
				continue
			personality_lines = get_personality(obj)
			if 'disables' in personality_lines:
				disablefleets.append(obj) # counting fleets with 'disables'
				continue
			if personality_lines == '':
				new_personality_lines = '\tpersonality\n\t\tdisables\n'
				obj = obj + new_personality_lines
			else:
				splitted = personality_lines[:-1].split(' ')
				if splitted[len(splitted)-1].isnumeric():
					new_personality_lines = personality_lines + '\t\tdisables\n'
				else:
					new_personality_lines = personality_lines[:-1] + ' disables\n'
				#obj = obj.replace(personality_lines, new_personality_lines)
				pos = obj.find('\n')
				new_obj = obj[:pos+1] + new_personality_lines
			modfleets.append(new_obj)
	print('reading fleets')
	print('\tall fleets ', len(allfleets))
	print('\tfleets with "disables" ', len(disablefleets))
	print('\tblacklisted fleets " ', len(blacklisted))
	print('\tfleets changed ', len(modfleets))
	# write to file
	print('writing to file')
	with open('disables_fleets.txt', 'w') as target:
		target.writelines('# fleets found: ' + str(len(allfleets)) + '\n')
		target.writelines('# fleets with "disables": ' + str(len(disablefleets)) + '\n')
		target.writelines('# blacklisted fleets: ' + str(len(blacklisted)) + '\n')
		target.writelines('# fleets changed: ' + str(len(modfleets)) + '\n\n\n')
		for each in modfleets:
			target.writelines(each + '\n\n')
	print('\tDONE')


if __name__ == "__main__":
	data_folder = 'D:/games/Endless Sky/data/'
	blacklisted = ['fleet "Derelict Northern"', 'fleet "Derelict Southern"', 'fleet "Derelict Core"', 'fleet "Derelict Pirate"']
	objs, obj_paths, obj_names = read_everything(data_folder)
	change_fleets(objs, blacklisted)