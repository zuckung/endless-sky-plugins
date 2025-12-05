import os
import random

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
				print('	reading: ' + folder + os.sep + text_file + spaces, end = '\r', flush= True)
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
							objs.append(txt.replace('<', '&#60;').replace('>', '&#62;'))
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
	print('	\n	DONE')
	return objs, obj_paths, obj_names

def get_name(check_name):
	if '`' in check_name:
		pos1 = check_name.find('`')
		pos2 = check_name.find('`', pos1+1)
		cleaned_name = check_name[pos1:pos2+1]
	elif '"' in check_name:
		pos1 = check_name.find('"')
		pos2 = check_name.find('"', pos1+1)
		cleaned_name = check_name[pos1:pos2+1]
	else:
		pos1 = check_name.find(' ')
		cleaned_name = check_name[pos1:]
	return cleaned_name

def get_nodes_txt(objs, obj_names, blacklist, node):
	# create a string of all "obj_names" matching "node"
	node_names, node_names2 = [], []
	nodes_txt = ''
	for obj_name in obj_names:
		if obj_name.startswith(node):
			# check if there is a dispay name
			index = obj_names.index(obj_name)
			if "display name" in objs[index]:
				pos1 = objs[index].find('"display name" ')
				pos2 = objs[index].find('\n', pos1+1)
				display_name = objs[index][pos1:pos2]
				if display_name == '???':
					obj_name = get_name(obj_name)
				else:
					obj_name = get_name(obj_name)
			else:
				obj_name = get_name(obj_name)
			# check if it is already in list, to exclude ship variant, also exclude blacklist
			if obj_name not in node_names:
				if obj_name.replace('"', '') not in blacklist:
					node_names.append(obj_name)
					node_names2.append(obj_name)
	# shuffle now
	for node_name in node_names:
		replacer_name = random.choice(node_names2)
		node_names2.remove(replacer_name)
		nodes_txt += node + ' ' + node_name + '\n' + '	"display name" ' + replacer_name + '\n\n'
	return nodes_txt

def write_to_file(full_txt, file_name):
	with open(file_name, 'w') as target:
		target.writelines(full_txt)

if __name__ == "__main__":
	data_folder = '/storage/9C33-6BBD/endless sky/data/'
	blacklist_ships = ["Asteroid Large 1", "Asteroid Large 2", "Asteroid Large 3", "Asteroid Large 4", "Asteroid Large 5", "Asteroid Medium", "Asteroid Young 1", "Asteroid Young 2", "Asteroid Young 3", "Asteroid Young 4", "Cloak Check", "Asteroid Planet", "Asteroid Blocker", "_Ion Timer Ship", "Rescue Dummy", "Timer Ship"]
	blacklist_outfits = ["ion hail", "rslug", "creeper1 print", "creeper1 static", "creeper2 print", "creeper2 static", "creeper3 print", "creeper3 static", "creeper4 print", "creeper4 static", "creeper5 print", "creeper5 static", "creeper6 print", "creeper6 static", "creeper7 print", "creeper7 static", "creeper8 print", "creeper8 static", "creeper9 print", "creeper9 static", "creeper10 print", "creeper10 static", "creeper11 print", "creeper11 static", "creeper12 print", "creeper12 static", "creeper13 print", "creeper13 static", "creeper14 print", "creeper14 static", "creeper15 print", "creeper15 static", "asteroid launch", "Asteroid Weapon Large 2", "spin1 print right", "spin1 print left", "track1 print right", "track1 print left", "spin2 print right", "spin2 print left", "track2 print right", "track2 print left", "spin3 print right", "spin3 print left", "track3 print right", "track3 print left", "spin4 print right", "spin4 print left", "track4 print right", "track4 print left", "asteroid laser 1", "Asteroid Weapon Large 3", "asteroid missile", "magic deployer1", "magic deployer2", "magic deployer3", "magic deployer4", "magic deployer5", "magic deployer6", "Asteroid Weapon Large 4", "wep1 print", "wep2 print", "wep3 print", "wep4 print", "wep5 print", "wep6 print", "wep7 print", "wep8 print", "wep9 print", "wep10 print", "wep11 print", "wep12 print", "wep13 print", "wep14 print", "wep15 print", "wep16 print", "wep17 print", "wep18 print", "wep19 print", "wep20 print", "wep21 print", "wep22 print", "wep23 print", "wep24 print", "wep25 print", "wep26 print", "wep27 print", "wep28 print", "wep29 print", "wep30 print", "wep31 print", "wep32 print", "wep33 print", "wep34 print", "wep35 print", "wep36 print", "wep37 print", "wep38 print", "wep39 print", "wep40 print", "wep41 print", "wep42 print", "wep static", "asteroid fragment", "ribault unguided", "ribault guided", "_Ion Storm Timer: Generator", "Mouthparts?"]
	blacklist = blacklist_ships + blacklist_outfits
	objs, obj_paths, obj_names = read_everything(data_folder)
	ships_txt = get_nodes_txt(objs, obj_names, blacklist, 'ship ')
	outfits_txt = get_nodes_txt(objs, obj_names, blacklist, 'outfit ')
	systems_txt = get_nodes_txt(objs, obj_names, blacklist, 'system ')
	full_txt = ships_txt + outfits_txt + systems_txt
	write_to_file(full_txt, 'total_confusion.txt')