import os
import math


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


def return_list(objs, obj_paths, node, race):
	# returns a list of all matching nodes, optional only by race
	# node_list = return_list(objs, obj_paths, 'ship', 'human')
	# node_list = return_list(objs, obj_paths, 'outfit', False)
	obj_list = []
	for each in objs:
		if each.startswith(node):
			if race != False:
				index = objs.index(each)
				if obj_paths[index].startswith('data' + os.sep + race):
					obj_list.append(each)
			else:
				obj_list.append(each)
	return obj_list


def return_value(objs, node, subnode):
	# returns the string value of a subnode
	# value = return_value(objs, 'ship "Bastion"', 'category') > Medium Warship
	for each in objs:
		if each.startswith(node + '\n'):
			obj = each
			break
	if subnode in obj:
		pos1 = obj.find(subnode)
		pos2 = obj.find('\n', pos1-1)
		value = obj[pos1:pos2].replace(subnode + ' ', '')
	else:
		value = 'subnode not found'
	return value


def filterlist(shiplist):
	filterlist = []
	for ship in shiplist:
		pos1 = ship.find('\n')
		node = ship[:pos1]
		count = node.count('"')
		if count > 2:
			continue
		if 'automaton' in ship:
			continue
		elif not '"required crew"' in ship:
			continue
		else:
			filterlist.append(ship)
	return filterlist
	
def modify(filterlist):
	newlist = []
	def slice(node):
		pos1 = node.find('"', 2)
		value = node[pos1+2:]
		return value
	for ship in filterlist:
		# get nodes
		pos1 = ship.find('\n')
		name = ship[:pos1]
		pos1 = ship.find('"required crew"')
		pos2 = ship.find('\n', pos1-1)
		required = slice(ship[pos1:pos2])
		pos1 = ship.find('"bunks"')
		pos2 = ship.find('\n', pos1-1)
		bunks = slice(ship[pos1:pos2])
		pos1 = ship.find('"outfit space"')
		pos2 = ship.find('\n', pos1-1)
		outfit = slice(ship[pos1:pos2])
		# get new values
		if int(required) < 2 and int(bunks) < 2:
			continue
		print(name)
		print('  original bunks/required: ' + bunks + '|' + required)
		if int(required) > 1:
			newrequired = math.floor(int(required) / 2)
		else:
			newrequired = int(required)
		if int(bunks) > 1:
			newbunks = math.floor(int(bunks) / 2)
		else:
			newbunks = int(bunks)
		print('  modified bunks/required: ' + str(newbunks) + '|' + str(newrequired))
		diffbunks = int(bunks) - newbunks
		newoutfit = int(outfit) + diffbunks * 2
		print('  diffbunks: ' + str(diffbunks))
		print('  new outfit: ' + outfit + ' + 2x' + str(diffbunks) + ' = ' + str(newoutfit))
		# new definition
		ship = name + '\n' +\
			'\tattributes\n' +\
			'\t\t"required crew" ' + str(newrequired) + '\n' +\
			'\t\t"bunks" ' + str(newbunks) + '\n' +\
			'\t\t"outfit space" ' + str(newoutfit) + '\n'
			
		newlist.append(ship)
	return newlist


def writefile(list):
	with open('half.crew.txt', 'w') as t:
		for each in list:
			t.writelines(each + '\n')


def run():
	data_folder = '/storage/9C33-6BBD/endless sky/data/'
	objs, obj_paths, obj_names = read_everything(data_folder)
	shiplist = return_list(objs, obj_paths, 'ship ', False)
	filteredships = filterlist(shiplist)
	list = modify(filteredships)
	writefile(list)

if __name__ == "__main__":
	run()