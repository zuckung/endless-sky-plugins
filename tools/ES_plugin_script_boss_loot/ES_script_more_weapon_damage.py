import os
from PIL import Image



def setup():
	print('setting global variables')
	global data_folder, image_folder
	global damage_increase, price_increase, rarity, ranks, upgrades
	data_folder = 'C:/Users/woot/AppData/Local/ESLauncher2/instances/release/data/' # change to your folder
	image_folder = 'C:/Users/woot/AppData/Local/ESLauncher2/instances/release/images/' # change to your folder
	damage_increase = [1.33, 1.66, 2] # weapon damages * damage_increase
	price_increase = [1.33, 1.66, 2]
	rarity = ['(T1)', '(T2)', '(T3)'] # name changes
	ranks = [1, 2, 3] # 1, 2 or 3, just counter
	upgrades = ['outfit "Nanite Swarm Blue"', 'outfit "Nanite Swarm Purple"', 'outfit "Nanite Swarm Orange"']
	weapon_blacklist = ["Korath Grab-Strike","Korath Banisher","Korath Fire-Lance","Korath Repeater",
		"Korath Repeater Turret","Korath Piercer Launcher","Korath Minelayer","Korath Disruptor",
		"Korath Slicer","Korath Slicer Turret","Drak Draining Field (Augmented)","Drak Turret",
		"Drak Turret (Augmented)","Drak Antimatter Fragment","Drak Antimatter Fragment (Augmented)",
		"Mouthparts?","Absorption Organ","Plankton Mouth","Astral Mouth","Pincer","Thunderhead"]


def read_everything():
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


def find_weapons(obj, obj_name):
	# find weapon outfits
	weapons = []
	weapon_names = []
	print('	filtering outfits')
	for each in obj:
		if each.startswith('outfit '):
			if '\tweapon\n' in each:
				index = obj.index(each)
				weapons.append(each)
				weapon_names.append(obj_name[index])
	return weapons, weapon_names


def filter_weapons(obj, obj_name, rank, weapons, weapons_names):
	def find_value(weapon,dmg,changed,name):
		# find the damage value and replace it
		if dmg in weapon:
			pos1 = weapon.find(dmg)
			pos2 = weapon.find('\n', pos1)
			value = weapon[pos1:pos2].split(' ')[2].strip()
			newvalue = round(float(value)*damage_increase[rank-1], 2)
			weapon = weapon.replace(dmg + ' ' + value, dmg + ' ' + str(newvalue))
			changed = True
		elif '"submunition"' in weapon:
			pos1 = weapon.find('"submunition" ')
			pos2 = weapon.find('\n', pos1)
			submun = weapon[pos1+14:pos2]
			if not 'T'+str(rank) in submun:
				pos2 = submun.find('"', 2)
				submunname = submun[1:pos2]
				newsubmunname = submunname + '(T' + str(rank) + ')'
				weapon = weapon.replace('"submunition" "' + submunname, '"submunition" "' + newsubmunname)
			changed = True
		#print ('	changed', name, '|', dmg.replace('\t\t', ''), 'from', value, 'to', newvalue)
		return weapon, changed
	# change weapon outfits
	new_weapons = []
	thumbnails = []
	print('	changing weapon texts')
	for weapon in weapons:
		changed = False
		index = weapons.index(weapon)
		name = weapons_names[index]
		dmg = '\t\t"shield damage"'
		weapon, changed = find_value(weapon,dmg,changed,name)
		dmg = '\t\t"hull damage"'
		weapon, changed = find_value(weapon,dmg,changed,name)
		dmg = '\t\t"heat damage"'
		weapon, changed = find_value(weapon,dmg,changed,name)
		dmg = '\t\t"minable damage"'
		weapon, changed = find_value(weapon,dmg,changed,name)
		dmg = '\t\t"disruption damage"'
		weapon, changed = find_value(weapon,dmg,changed,name)
		dmg = '\t\t"slowing damage"'
		weapon, changed = find_value(weapon,dmg,changed,name)
		dmg = '\t\t"ion damage"'
		weapon, changed = find_value(weapon,dmg,changed,name)
		dmg = '\t\t"scrambling damage"'
		weapon, changed = find_value(weapon,dmg,changed,name)
		dmg = '\t\t"energy damage"'
		weapon, changed = find_value(weapon,dmg,changed,name)
		dmg = '\t\t"fuel damage"'
		weapon, changed = find_value(weapon,dmg,changed,name)
		if changed:
			# change cost
			if '\t"cost"' in weapon or '\tcost' in weapon:
				if '\t"cost"' in weapon:
					pos1 = weapon.find('\t"cost"')
					pos2 = weapon.find('\n', pos1+1)
					cost = weapon[pos1+8:pos2]
					newcost = int(int(cost) * price_increase[rank-1])
					weapon = weapon.replace(cost, str(newcost))
				else:
					pos1 = weapon.find('\tcost')
					pos2 = weapon.find('\n', pos1+1)
					cost = weapon[pos1+6:pos2]
					newcost = int(int(cost) * price_increase[rank-1])
					weapon = weapon.replace(cost, str(newcost))
			# change outfit name
			pos1 = weapon.find(' ')
			pos2 = weapon.find('\n')
			pos3 = weapon.find('"')
			pos4 = weapon.find('`')
			outfitname = weapon[:pos2] # outfit "Heavy Laser" | outfit `"bunga" something` | outfit mouthparts?
			weaponname = outfitname[pos1+1:pos2] # "Heavy Laser"
			if not '"' in weaponname:
				weaponname = '"' + weaponname + '"'
			weaponname = weaponname[:len(weaponname)-1] + rarity[rank-1]
			if not '`' in weaponname:
				weaponname = 'outfit ' + weaponname + '"'
			else:
				weaponname = 'outfit ' + weaponname + '`'
			weapon = weapon.replace(outfitname, weaponname, 1)
			# submunition
			if '"submunition"' in weapon: # "submunition" "Drag Projectile" 3
				pos1 = weapon.find('"submunition"')
				pos2 = weapon.find('\n', pos1+1)
				submunition = weapon[pos1+14:pos2] # "Drag Projectile" 3
				pos2 = submunition.find('"',1)
				submunition = submunition[1:pos2] # Drag Projectile
				new_sub = submunition + rarity[rank-1]
				weapon = weapon.replace('"submunition" '+ submunition, '"submunition" ' + new_sub)
			# create thumbnail lists
			if '\tthumbnail ' in weapon:
				pos1 = weapon.find('\tthumbnail')
				pos2 = weapon.find('\n', pos1)
				thumbnail = weapon[pos1+12:pos2-1]
				weapon = weapon.replace(thumbnail, thumbnail + rarity[rank-1])
				if not thumbnail in thumbnails:
					thumbnails.append(thumbnail)
			new_weapons.append(weapon + '\n')
	# writing files
	weaponcount = 0
	print('	writing weapons.txt')
	with open('dun.weapons' + str(rarity[rank-1]) + '.txt', 'w') as target:
		for weapon in new_weapons:
			weaponcount += 1
			target.writelines(weapon)
	print('	weapons changed:', str(weaponcount))
	print('	DONE')
	return thumbnails, weapons


def create_thumbnails(thumbnails, rank):
	# create new sprites for the changed outfits with a star on the right side
	print('\ncreating new outfit sprites')
	print('	new weapon outfits:', len(thumbnails))
	if not os.path.isdir('outfit'):
		os.mkdir('outfit')
	for thumbnail in thumbnails:
		im1 = Image.open(image_folder + thumbnail + '.png')
		width, height = im1.size
		im2 = Image.open('star25.png')
		img = Image.new('RGBA', (width + 50, height), (255, 0, 0, 0))
		img.paste(im1, (25, 0))
		for i in range(1, rank+1):
			img.alpha_composite(im2, (width +25, -30 + (i*30)))
		img.save(thumbnail + rarity[rank-1] + '.png', quality=95)
	print('	DONE')


def create_mission():
	# reading weapons
	weapons0 = []
	weapons1 = []
	weapons2 = []
	with open('dun.weapons' + rarity[0] + '.txt', 'r') as source:
		lines = source.readlines()
	name = ''
	for line in lines:
		if line.startswith('outfit '):
			name = line
		elif '\tthumbnail' in line: # exclude submunition
			weapons0.append(name.strip().replace(rarity[0], ''))
			weapons1.append(name.strip())	
	# reading upgraded weapons
	with open('dun.weapons' + rarity[1] + '.txt', 'r') as source:
		lines = source.readlines()
	for line in lines:
		if line.startswith('outfit ') :
			name = line
		elif '\tthumbnail' in line: # exclude submunition
			weapons2.append(name.strip())
	# writing mission
	with open('dun.upgrade.mission.txt', 'w') as target:
		# start block
		target.writelines('mission "upgrade outfits"\n')
		target.writelines('\tjob\n')
		target.writelines('\trepeat\n')
		target.writelines('\tname "[services] Weapon Upgrades"\n')
		target.writelines('\tdescription "Upgrade your flagship installed weapons with Nanite Swarms."\n')
		target.writelines('\tcolor selected "endgame job: selected"\n')
		target.writelines('\tcolor unselected "endgame job: unselected"\n')
		target.writelines('\tsource "dun_station_01"\n')
		target.writelines('\tto offer\n')
		target.writelines('\t\tor\n')
		target.writelines('\t\t\thas "outfit (flagship installed): Nanite Swarm Blue"\n')
		target.writelines('\t\t\thas "outfit (flagship installed): Nanite Swarm Purple"\n')
		target.writelines('\t\t\thas "outfit (flagship installed): Nanite Swarm Orange"\n')
		target.writelines('\ton accept\n')
		target.writelines('\t\tconversation\n')
		target.writelines('\t\t\tlabel start\n')
		target.writelines('\t\t\t``\n')
		target.writelines('\t\t\tlabel menu\n')
		target.writelines('\t\t\t`The engineers inspect your ship and check what upgrades are possible...`\n')
		target.writelines('\t\t\t``\n')
		target.writelines('\t\t\t`You have:`\n')
		target.writelines('\t\t\t`Nanite Swarm Blue: &[outfit: Nanite Swarm Blue]`\n')
		target.writelines('\t\t\t`Nanite Swarm Purple: &[outfit: Nanite Swarm Purple]`\n')
		target.writelines('\t\t\t`Nanite Swarm Orange: &[outfit: Nanite Swarm Orange]`\n')
		target.writelines('\t\t\t``\n')
		target.writelines('\t\t\t`Possible flagship outfit upgrades:`\n')
		target.writelines('\t\t\tchoice\n')
		# normal weapon choices
		for weapon in weapons0:
			target.writelines('\t\t\t\t`\t' + weapon.replace('outfit ', '').replace('`', '') + ' (&[outfit (flagship installed): ' + weapon.replace('outfit ', '')\
				.replace('`', '').replace('"', '') + '])`\n')
			target.writelines('\t\t\t\t\tto display\n')
			if '`' in weapon:
				target.writelines('\t\t\t\t\t\thas `' + weapon.replace('outfit', 'outfit (flagship installed):').replace('`', '') + '`\n')
			else:
				target.writelines('\t\t\t\t\t\thas "' + weapon.replace('outfit', 'outfit (flagship installed):').replace('"','') + '"\n')
				target.writelines('\t\t\t\t\t\thas "' + upgrades[0].replace('outfit', 'outfit (flagship installed):').replace('"', '') + '"\n')
			target.writelines('\t\t\t\t\tgoto ' + weapon.replace('outfit ', '') + '\n')
		# first upgrade weapons
		for weapon in weapons1:
			target.writelines('\t\t\t\t`\t' + weapon.replace('outfit ', '').replace('`', '') + ' (&[outfit (flagship installed): ' + weapon.replace('outfit ', '')\
				.replace('`', '').replace('"', '') + '])`\n')
			target.writelines('\t\t\t\t\tto display\n')
			if '`' in weapon:
				target.writelines('\t\t\t\t\t\thas `' + weapon.replace('outfit', 'outfit (flagship installed):').replace('`', '') + '`\n')
			else:
				target.writelines('\t\t\t\t\t\thas "' + weapon.replace('outfit', 'outfit (flagship installed):').replace('"','') + '"\n')
				target.writelines('\t\t\t\t\t\thas "' + upgrades[1].replace('outfit', 'outfit (flagship installed):').replace('"', '') + '"\n')
			target.writelines('\t\t\t\t\tgoto ' + weapon.replace('outfit ', '') + '\n')
		# second upgrade weapons
		for weapon in weapons2:
			target.writelines('\t\t\t\t`\t' + weapon.replace('outfit ', '').replace('`', '') + ' (&[outfit (flagship installed): ' + weapon.replace('outfit ', '')\
				.replace('`', '').replace('"', '') + '])`\n')
			target.writelines('\t\t\t\t\tto display\n')
			if '`' in weapon:
				target.writelines('\t\t\t\t\t\thas `' + weapon.replace('outfit', 'outfit (flagship installed):').replace('`', '') + '`\n')
			else:
				target.writelines('\t\t\t\t\t\thas "' + weapon.replace('outfit', 'outfit (flagship installed):').replace('"','') + '"\n')
				target.writelines('\t\t\t\t\t\thas "' + upgrades[2].replace('outfit', 'outfit (flagship installed):').replace('"', '') + '"\n')
			target.writelines('\t\t\t\t\tgoto ' + weapon.replace('outfit ', '') + '\n')
		# end choice
		target.writelines('\t\t\t\t`\tcancel`\n')
		target.writelines('\t\t\t\t\tgoto end\n')
		# actions for normal weapons
		for weapon in weapons0:
			target.writelines('\t\t\tlabel ' + weapon.replace('outfit ', '') + '\n')
			target.writelines('\t\t\taction\n')
			target.writelines('\t\t\t\t' + weapon + ' -1\n')
			target.writelines('\t\t\t\t' + upgrades[0] + ' -1\n')
			if '`' in weapon:
				new_weapon = weapon[:len(weapon)-1] + rarity[0] + '`'
			else:
				new_weapon = weapon[:len(weapon)-1] + rarity[0] + '"'
			target.writelines('\t\t\t\t' + new_weapon + ' 1\n')
			target.writelines('\t\t\t`\t' + new_weapon.replace('`', '') + ' +1`\n')
			target.writelines('\t\t\t\tgoto menu\n')
		# actions for first upgrade weapons
		for weapon in weapons1:
			target.writelines('\t\t\tlabel ' + weapon.replace('outfit ', '') + '\n')
			target.writelines('\t\t\taction\n')
			target.writelines('\t\t\t\t' + weapon + ' -1\n')
			target.writelines('\t\t\t\t' + upgrades[1] + ' -1\n')
			new_weapon = weapon.replace(rarity[0],rarity[1])
			target.writelines('\t\t\t\t' + new_weapon + ' 1\n')
			target.writelines('\t\t\t`\t' + new_weapon.replace('`', '') + ' +1`\n')
			target.writelines('\t\t\t\tgoto menu\n')
		# actions for second upgrade weapons
		for weapon in weapons2:
			target.writelines('\t\t\tlabel ' + weapon.replace('outfit ', '') + '\n')
			target.writelines('\t\t\taction\n')
			target.writelines('\t\t\t\t' + weapon + ' -1\n')
			target.writelines('\t\t\t\t' + upgrades[2] + ' -1\n')
			new_weapon = weapon.replace(rarity[1],rarity[2])
			target.writelines('\t\t\t\t' + new_weapon + ' 1\n')
			target.writelines('\t\t\t`\t' + new_weapon.replace('`', '') + ' +1`\n')
			target.writelines('\t\t\t\tgoto menu\n')
		#target.writelines('\t\t\t\t')
		# end block
		target.writelines('\t\t\tlabel end\n')
		target.writelines('\t\t\t`The engineers wish you lots of fun with your upgraded weapons.`\n')
		target.writelines('\t\tfail\n')
		print()


def create_universal_outfitter(weapons, ranks):
	# creating universal ammo restock rule outfitters
	outfitter_text = ''
	ammo_types, ammo_weapons = [], []
	for weapon in weapons:
		if '		ammo ' in weapon:
			ammo_weapons.append(weapon)
			ammo_name = weapon[weapon.find('		ammo ')+7:weapon.find('\n', weapon.find('		ammo '))]. strip()
			if '`' in ammo_name:
				ammo_name = ammo_name[1:ammo_name.find('`', 1)]  #: Cluster Mine
			else:
				ammo_name = ammo_name[1:ammo_name.find('"', 1)]  #: Cluster Mine
			if not ammo_name in ammo_types:
				ammo_types.append(ammo_name)
	for ammo_type in ammo_types:
		outfitter_text += '' +\
			'outfitter "dun ' + ammo_type.replace('"', '') + ' Restock"\n' +\
			'	to sell\n' +\
			'		has "gamerule: universal ammo restocking"\n' +\
			'		or\n'
		for weapon in ammo_weapons:
			ammo_name = weapon[weapon.find('		ammo ')+7:weapon.find('\n', weapon.find('		ammo '))]. strip()
			if '`' in ammo_name:
				ammo_name = ammo_name[1:ammo_name.find('`', 1)]  #: Cluster Mine
			else:
				ammo_name = ammo_name[1:ammo_name.find('"', 1)]  #: Cluster Mine
			if not ammo_name in ammo_types:
				ammo_types.append(ammo_name)
			if ammo_type == ammo_name:
				weapon_name = weapon[:weapon.find('\n')].replace('outfit ', '')[1:-1] #: Cluster Mine Layer
				for rank in ranks:
					if '"' in weapon_name:
						outfitter_text += '			has `outfit: ' + weapon_name + '(T' + str(rank) + ')`\n'
					else:
						outfitter_text += '			has "outfit: ' + weapon_name + '(T' + str(rank) + ')"\n'
		outfitter_text += '' +\
			'	location\n' +\
			'		attributes "outfitter"\n' +\
			'	stock\n' +\
			'		"' + ammo_type + '"\n\n'
	# write to file
	with open('outfitters.txt', 'w') as target:
		target.writelines(outfitter_text)


def menu():
	setup()
	obj, obj_path, obj_name = read_everything()
	weapons, weapon_names = find_weapons(obj, obj_name)
	for rank in ranks:
		print('\ncreating stuff for rank:', rank, rarity[rank-1])
		thumbnails, weapons = filter_weapons(obj, obj_name, rank, weapons, weapon_names)
		create_thumbnails(thumbnails, rank)
	create_mission()
	create_universal_outfitter(weapons, ranks)



if __name__ == '__main__':
	menu()