import os



def read_everything(data_folder):
	print('\nreading data folder')
	obj, obj_path, obj_name = [], [], []
	started = False
	folders = os.listdir(data_folder)
	folders.append('')
	folders.sort()
	for folder in  folders:
		if os.path.isdir(data_folder + folder):
			text_files = os.listdir(data_folder + folder)
			text_files.sort()
			for text_file in text_files:
				if os.path.isfile(data_folder + folder + '/' + text_file) == False:
					continue
				if len(folder + text_file)  < 80: # just for displaying / max len = 44(currently)
					count = 80 - len(folder + text_file)
					spaces = ''
					for i in range(0, count):
						spaces += ' '
				print('	reading: ' + folder + '/' + text_file + spaces, end = '\r', flush= True)
				with open(data_folder + folder + '/' + text_file, 'r') as source_file:
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
								folder_fix = folder + '/'
							else:
								folder_fix = folder
							txt2 = 'data/' + folder_fix + text_file
							txt3 = line[:len(line)-1]
							started = True
					else:
						if started == True:
							txt += line
	print('	\n	DONE')
	return obj, obj_path, obj_name


def write_ships(tiers, obj, ship_exclude, nodes_exclude):
	# get ships
	ships, ship_names, all_tiers = [], [], []
	for each in obj:
		if each.startswith('ship '):
			line = each[:each.find('\n')]
			pos1 = line.find('"')
			pos2 = line.find('"', pos1 +1)
			ship = line[pos1+1:pos2]
			if not ship in ship_exclude:
				if line == 'ship "' + ship + '"':
					ships.append(each)
	# get raw ship names
	for ship in ships:
		pos1 = ship.find('"')
		pos2 = ship.find('"', pos1 +1)
		ship_names.append(ship[pos1+1:pos2])
	# alter ships
	for tier in tiers:
		for ship in ships:
			part1, part2, attributes = '', '', ''
			# get attributes
			splitted = ship.split('\n')
			started = False
			ended = False
			for line in splitted:
				if line.startswith('\tattributes'):
					started = True
					attributes += line + '\n'
					continue
				if started == False:
					if ended == False:
						part1 += line + '\n'
				if started == True:
					if line.startswith('\t\t'):
						attributes += line + '\n'
					else:
						started = False
						ended = True
						part2 += line + '\n'
				if started == False and ended == True:
					part2 += line + '\n'
			# alter attributes
			splitted = attributes.split('\n')
			new_attributes = ''
			for line in splitted:
				minus = False
				skip = False
				for node in nodes_exclude:
					if line.startswith(node):
						skip = True
				if skip == True:
					new_attributes += line + '\n'
					continue
				if line == '':
					continue
				if '"' in line:
					pos1 = line.find('"')
					pos2 = line.find('"', pos1+1)
					number = line[pos2+2:]
					if number.startswith('-'):
						minus = True
						number = number[1:]
					if number.startswith('.'):
						number = '0' + number
					if minus == True:
						number = '-' + number
					new_attributes += line[:pos2+1] + ' ' + str(float(number) * (tier + 1)) + '\n'
				else:
					spaced = line.split(' ')
					number = spaced[1]
					if number.startswith('.'):
						number = '0' + number
					new_attributes += spaced[0] + ' ' + str(float(number) * (tier + 1)) + '\n'
			# rename with tier
			pos1 = part1.find('\n')
			oldnameline = part1[:pos1-1]
			newnameline = part1[:pos1-1] + ' (T' + str(tier) + ')'
			part1 = part1.replace(oldnameline, newnameline)
			pos1 = oldnameline.find('"')
			pos2 = oldnameline.find('"', pos1 +1)
			if tier < 10:
				ship_names.append(oldnameline[pos1+1:] + ' (T' + str(tier) + ')')
			# double bay/gun/turret
			newsplitted = part2.split('\n')
			part2 = ''
			for line in newsplitted:
				if line.startswith('\tgun'):
					if '"' in line:
						pos1 = line.find('"')
						line = line[:pos1-1]
						part2 += line + '\n'
						for i in range(1, tier):
							part2 += line + '\n'
					else:
						if line.count(' ') > 2:
							newline = line.split(' ')[0] + ' ' + line.split(' ')[1] + ' ' + line.split(' ')[2] + '\n'
							part2 += newline
							for i in range(1, tier):
								part2 += newline
						else:
							part2 += line + '\n'
							for i in range(1, tier):
								part2 += line + '\n'
				if line.startswith('\tturret'):
					if '"' in line:
						pos1 = line.find('"')
						line = line[:pos1-1]
						part2 += line + '\n'
						for i in range(1, tier):
							part2 += line + '\n'
					else:
						part2 += line + '\n'
						for i in range(1, tier):
							part2 += line + '\n'
				if line.startswith('\tbay'):
					part2 += line + '\n'
					for i in range(1, tier):
						part2 += line + '\n'
				else:
					part2 += line + '\n'
			# put everything into a list
			all_tiers.append(part1 + new_attributes + part2)
	with open('ship_upgrades_ships.txt', 'w') as t:
		for each in all_tiers:
			t.writelines(each)
	return ship_names


def write_mission(ship_names):
	# mission start text
	missiontxt = '' + \
		'mission "upgrade ships"\n' +\
		'	job\n' +\
		'	repeat\n' +\
		'	name "(Upgarde Ships)"\n' +\
		'	"description" "Combine a ship +3 base versions of that ship into one of a higher tier, up to a max of T10."\n' +\
		'	color selected "ship_upgrades job: selected"\n' +\
		'	color unselected "ship_upgrades job: unselected"\n' +\
		'	source "su_planet1"\n' +\
		'	on accept\n' +\
		'		conversation\n' +\
		'			label "start"\n' +\
		'			label "menu"\n' +\
		'			`Ship Upgrade Menu`\n' +\
		'			``\n' +\
		'			`- only active ships in your fleet will be considered`\n' +\
		'			`- on merging, all ship outfits are lost, and the new ship has the standard outfits`\n' +\
		'			``\n' +\
		'			`i.e.: own 4 ships of the same kind and merge them into one T1 ship of that kind with doubled attributes`\n' +\
		'			`i.e.: own 3 ships of the same kind and one T4 of that kind, and merge it into one T5 ship of that kind with 6 times the attributes (of the base version)`\n' +\
		'			``\n' +\
		'			`The following ships can be merged into a higher tier:`\n' +\
		'			choice\n'
	# choice
	for ship in ship_names:
		no = '3'
		if 'T1' in ship:
			tier = 1
			base = ship.replace(' (T1)', '')
		elif 'T2' in ship:
			tier = 2
			base = ship.replace(' (T2)', '')
		elif 'T3' in ship:
			tier = 3
			base = ship.replace(' (T3)', '')
		elif 'T4' in ship:
			tier = 4
			base = ship.replace(' (T4)', '')
		elif 'T5' in ship:
			tier = 5
			base = ship.replace(' (T5)', '')
		elif 'T6' in ship:
			tier = 6
			base = ship.replace(' (T6)', '')
		elif 'T7' in ship:
			tier = 7
			base = ship.replace(' (T7)', '')
		elif 'T8' in ship:
			tier = 8
			base = ship.replace(' (T8)', '')
		elif 'T9' in ship:
			tier = 9
			base = ship.replace(' (T9)', '')
		elif 'T10' in ship:
			tier = 10
			continue
		else:
			tier = 0
			no = '4'
			base = ship
		if tier < 10:
			if tier == 0:
				missiontxt += \
				'				`	merge ' + no + 'x "' + ship + '" into a "' + ship + ' (T' + str(tier + 1) + ')"`\n' +\
				'					to display\n' +\
				'						"ship model: ' + base + '" >= 4\n' +\
				'					goto "' + ship + '"\n'
			else:
				missiontxt += \
				'				`	merge ' + no + 'x "' + base + '" and 1x "' + ship + '" into a "' + base + '(T' + str(tier + 1) + ')"`\n' +\
				'					to display\n' +\
				'						"ship model: ' + base + '" >= 3\n' +\
				'						"ship model: ' + ship + '" >= 1\n' +\
				'					goto "' + ship + '"\n'
	missiontxt += \
		'				`close`\n' +\
		'					goto "end"\n'
	# action labels
	for ship in ship_names:
		no = '3'
		if 'T1' in ship:
			tier = 1
			give_ship = ship.replace('T1', 'T2')
			base = ship.replace(' (T1)', '')
		elif 'T2' in ship:
			tier = 2
			give_ship = ship.replace('T2', 'T3')
			base = ship.replace(' (T2)', '')
		elif 'T3' in ship:
			tier = 3
			give_ship = ship.replace('T3', 'T4')
			base = ship.replace(' (T3)', '')
		elif 'T4' in ship:
			tier = 4
			give_ship = ship.replace('T4', 'T5')
			base = ship.replace(' (T4)', '')
		elif 'T5' in ship:
			tier = 5
			give_ship = ship.replace('T5', 'T6')
			base = ship.replace(' (T5)', '')
		elif 'T6' in ship:
			tier = 6
			give_ship = ship.replace('T6', 'T7')
			base = ship.replace(' (T6)', '')
		elif 'T7' in ship:
			tier = 7
			give_ship = ship.replace('T7', 'T8')
			base = ship.replace(' (T7)', '')
		elif 'T8' in ship:
			tier = 8
			give_ship = ship.replace('T8', 'T9')
			base = ship.replace(' (T8)', '')
		elif 'T9' in ship:
			tier = 9
			give_ship = ship.replace('T9', 'T10')
			base = ship.replace(' (T9)', '')
		elif 'T10' in ship:
			tier = 10
		else:
			tier = 0
			give_ship = ship + ' (T1)'
			base = ship
			no = '4'
		if not tier == 10:
			if tier == 0:
				missiontxt += \
				'			label "' + ship + '"\n' +\
				'			action\n' +\
				'				take ship "' + base + '"\n' +\
				'					count 4\n' +\
				'				give ship "' + give_ship + '"\n' +\
				'			`' + no + 'x "' + base + '" removed, 1x "' + give_ship + '" given`\n' +\
				'				goto menu\n'
			else:
				missiontxt += \
				'			label "' + ship + '"\n' +\
				'			action\n' +\
				'				take ship "' + base + '"\n' +\
				'					count 3\n' +\
				'				take ship "' + ship + '"\n' +\
				'				give ship "' + give_ship + '"\n' +\
				'			`' + no + 'x "' + base + '" removed, 1x "' + ship + '" removed, 1x "' + give_ship + '" given`\n' +\
				'				goto menu\n'
	missiontxt += \
		'			label "end"\n' +\
		'			`bye`\n' +\
		'		fail\n'
	# write file
	with open('ship_upgrades_mission.txt', 'w') as t:
		t.writelines(missiontxt)



def run():
	data_folder = '/storage/9C33-6BBD/endless sky/data/'
	node_exclude = ['\tattributes', '\t\tcategory', '\t\tlicenses', '\t\tweapon', '\t\t\t', '\t\t"flare', '\t\t"steering', '\t\t"reverse', '\t"heat dissipation', '\t\t"waterlining', '\t\t"gaslining', '\t\t"automaton', '#', '\t\t#']
	ship_exclude = ["Mammoth", "Anomalocaris", "vyu-Ir", "Modified Hauler VI", "Waverider", "Modified Ladybug", "Modified Battleship", "Modified Boxwing", "Marauder Bactrian", "Shooting Star", "Ursa Polaris", "Modified Osprey", "Lampyrid-Class Transport", "Marauder Fury","Wardragon", "Ayym", "Korath Dredger", "Korath Raider", "Korath Chaser", "Korath World-Ship", "Quarg Skylark", "Windjammer", "Bluejacket", "Pollen", "Sprout", "Archon", "Subsidurial", "Void Sprite", "Ember Waste Node", "Embershade", "Embersylph", "Hallucination", "Asteroid", "Science Drone", "Emergency Shuttle", "Unknown Ship Type", "Surveillance Drone", "Aberrant Latte", "Aberrant Chomper", "Aberrant Pileup", "Aberrant Hugger", "Aberrant Longfellow", "Aberrant Dancer", "Aberrant Junior", "Aberrant Icebreaker", "Aberrant Pike", "Aberrant Mole", "Aberrant Whiskers", "Aberrant Trip", "Aberrant Triplet", "Asteroid Large 1", "Asteroid Large 2", "Asteroid Large 3", "Asteroid Large 4", "Asteroid Large 5", "Asteroid Medium", "Asteroid Young 1", "Asteroid Young 2", "Asteroid Young 3", "Asteroid Young 4", "Cloak Check", "Asteroid Planet", "Remnant Satellite", "Asteroid Blocker", "Maeri'het", "Telis'het", "Vareti'het", "Selii'mar", "Faes'mar", "Fetri'sei", "Nanobot",  "_Ion Timer Ship", "Rescue Dummy", "Timer Ship", "Vyrmeid", "Astral Cetacean", "Pincer Beast"]
	tiers = [1,2,3,4,5,6,7,8,9,10]
	obj, obj_path, obj_name = read_everything(data_folder)
	ship_names = write_ships(tiers, obj, ship_exclude, node_exclude)
	write_mission(ship_names)


if __name__ == '__main__':
	run()