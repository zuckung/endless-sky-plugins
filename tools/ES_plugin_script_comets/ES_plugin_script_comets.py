import os



def get_ES_data(data_folder):
	print('READING DATA FOLDER')
	started = False
	obj, obj_path, obj_name = [], [], []
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
								obj.append(txt)
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
	print('\tDONE')
	return obj, obj_path, obj_name


def initialwrite(obj):
	datasystemlist = []
	for each in obj:
		if each.startswith('system '):
			pos2 = each.find('\n')
			datasystemlist.append(each[:pos2])
	with open('cfg_systems.txt', 'w') as target:
		for system in datasystemlist:
			target.writelines(system + '\n')


def createevents():
	print('CREATING EVENTS')
	# create a whole event text
	def create_event(list1, list2, minables, no):
		print('\tWRITING EVENT', no)
		text = 'event "asteroid.pos.' + str(no) + '"\n'
		#print(list1)
		#print(len(list1))
		#print(list2)
		#print(len(list2))
		#print(minables)
		#print(len(minables))
		for each in list1:
			index = list1.index(each)
			text += '\t' + each
			if index >= len(minables) -1:
				index -= 10
			text += '\t\tadd minables ' + minables[index].strip() + ' 1 5\n'
		for each in list2:
			index = list2.index(each)
			text += '\t' + each
			if index >= len(minables) -1:
				index -= 10
			text += '\t\tremove minables ' + minables[index].strip() + ' 1 5\n'
		text += '\n\n'
		return text
	# list appearances of the minables in given list
	def indices(lst, element):
		result = []
		offset = -1
		while True:
			try:
				offset = lst.index(element, offset+1)
			except ValueError:
				return result
			result.append(offset)
	# read and format minables to list
	print('\tCREATING MINABLES LIST')
	with open('cfg_systems.txt', 'r') as source:
		systemlist = source.readlines()
	listlen = round(len(systemlist) / 10)
	with open('cfg_minables.txt', 'r') as source:
		minablelist = source.readlines()
	minables = [None] * listlen
	taken = set()
	for each in minablelist:
		minablename = each.split('|')[0]
		amount = int(each.split('|')[1].strip().replace('%', ''))
		distance = listlen / amount
		for i in range(round(amount * (listlen / 100))):
			index = round(i * distance)
			while index in taken and index < listlen:
				index += 1
			if index < listlen:
				minables[index] = minablename
				taken.add(index)
	# check if % are correct
	print('\tCHECKING MINABLES LIST')
	print('\t\tEVENT LENGTH:', listlen)
	for each in minablelist:
		minablename = each.split('|')[0]
		percent = each.split('|')[1].strip()
		count = len(indices(minables, minablename))
		print('\t\t', minablename, 'should be', percent, '| is', count, '(', round(count / (listlen / 100)), '%)')	
	# put the systems into 10 lists
	pos = 0
	l1,l2,l3,l4,l5,l6,l7,l8,l9,l10 = [], [], [], [], [], [], [], [], [], [],
	for system in systemlist:
		pos +=1
		if pos%10 == 1%10:
			l1.append(system)
		elif pos%10 == 2%10:
			l2.append(system)
		elif pos%10 == 3%10:
			l3.append(system)
		elif pos%10 == 4%10:
			l4.append(system)
		elif pos%10 == 5%10:
			l5.append(system)
		elif pos%10 == 6%10:
			l6.append(system)
		elif pos%10 == 7%10:
			l7.append(system)
		elif pos%10 == 8%10:
			l8.append(system)
		elif pos%10 == 9%10:
			l9.append(system)
		elif pos%10 == 10%10:
			l10.append(system)
	# write the events to file
	with open('events.txt', 'w') as target:
		for each in minablelist:
			target.writelines('# ' + each)
		target.writelines('\n')
		target.writelines('# event "asteroid.pos.1"\n')
		target.writelines('# event "asteroid.pos.2"\n')
		target.writelines('# event "asteroid.pos.3"\n')
		target.writelines('# event "asteroid.pos.4"\n')
		target.writelines('# event "asteroid.pos.5"\n')
		target.writelines('# event "asteroid.pos.6"\n')
		target.writelines('# event "asteroid.pos.7"\n')
		target.writelines('# event "asteroid.pos.8"\n')
		target.writelines('# event "asteroid.pos.9"\n')
		target.writelines('# event "asteroid.pos.10"\n\n\n\n')
		target.writelines(create_event(l1, l10, minables, 1))
		target.writelines(create_event(l2, l1, minables, 2))
		target.writelines(create_event(l3, l2, minables, 3))
		target.writelines(create_event(l4, l3, minables, 4))
		target.writelines(create_event(l5, l4, minables, 5))
		target.writelines(create_event(l6, l5, minables, 6))
		target.writelines(create_event(l7, l6, minables, 7))
		target.writelines(create_event(l8, l7, minables, 8))
		target.writelines(create_event(l9, l8, minables, 9))
		target.writelines(create_event(l10, l9, minables, 10))


def run():
	data_folder = 'd:/games/endless sky/data/'
	obj, obj_path, obj_name = get_ES_data(data_folder)
	initialwrite(obj) # to create the cfg_systems.txt out of the data folder
	createevents() # create the 10 events and write them to file


if __name__ == "__main__":
	run()