import os



def read_everything(data_folder):
	print('\nreading data folder')
	objs, obj_paths, obj_names = [], [], []
	started = False
	folders = os.listdir(data_folder)
	folders.append('')
	folders.sort()
	for folder in folders:
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


def filter(objs, blacklist_attributes):
	print('filter ships')
	ships, cores, variants = [], [], []
	for obj in objs:
		if obj.startswith('ship '):
			pos1 = obj.find('"')
			pos2 = obj.find('"', pos1+1)
			if obj[pos2+1] == '\n':
				#print(obj[:pos2+1])
				ships.append(obj)
			else:
				variants.append(obj)
	print('	ships: ', len(ships))
	print('	variants: ', len(variants))
	txt = 'category "outfit"\n	"Ship Cores"\n\n\n'
	print('modifying ships')
	justone = False
	for ship in ships:
		attributes, outfits, relevantattributes = [], [], []
		outfittxt, shiptxt, attributereplace, outfitsreplace, newattributes = '','', '', '', ''
		attributesstart = False
		outfitsstart = False
		splitted = ship.split('\n')
		outfitline = False
		for line in splitted:
			# get list with attributes
			if line.startswith('	attributes'):
				attributesstart = True
				continue
			if attributesstart == True:
				if not line.startswith('		'):
					attributesstart = False
					if line.startswith('	outfits'):
						outfitline = True
					continue
				# ignore these lines:
				found = False
				for blacklisted in blacklist_attributes:
					if line.startswith(blacklisted):
						newattributes += line + '\n' # new ship attributes
						attributes.append(line)
						found = True
				if found == True:
					continue
				# adjust price
				if line.startswith('		cost') or line.startswith('		"cost"'):
					attributes.append(line) # original attribute
					costs = '		cost ' + str(int(line.strip().replace('cost', '').replace('"',''))/2) # string, 50% of cost
					line = costs
					relevantattributes.append(line) # for outfit
					newattributes += line + '\n'
				else:
					attributes.append(line)
					relevantattributes.append(line)
			# get list with outfits
			if line.startswith('	outfits'):
				outfitsstart = True
				continue
			if outfitline == True:
				outfitline = False
				outfitsstart = True
				outfits.append(line)
				continue
			if outfitsstart == True:
				if not line.startswith('		'):
					outfitsstart = False
					continue
				outfits.append(line)
		# get shipname
		pos = ship.find('\n')
		shipname = ship[:pos].replace('ship ', '').replace('"', '')
		# create outfit txt
		outfitname = 'outfit "' + shipname + ' Core"\n'
		cores.append(shipname)
		outfittxt += outfitname  + '	thumbnail "outfit/ship_core"\n	category "Ship Cores"\n	"Core Slot" -1\n'
		for attribute in relevantattributes:
			outfittxt += '	' + attribute.strip() + '\n'
		# create outfitsreplace
		for outfit in outfits:
			outfitsreplace += outfit + '\n'
		# create ship txt
		for attribute in attributes:
			attributereplace += attribute + '\n'
		newattributes += '		"Core Slot" 1\n'
		if outfitsreplace != '':
			shiptxt = ship.replace(attributereplace, newattributes).replace(outfitsreplace, outfitsreplace + '		' + outfitname.replace('outfit ', ''))
		else:
			shiptxt = ship.replace(attributereplace, newattributes) + '	outfits\n		' + outfitname.replace('outfit ', '')
		# add to txt
		txt += outfittxt + '\n\noverwrite\n' + shiptxt + '\n\n'
	# write txt
	with open('ships.txt', 'w') as target:
		target.writelines(txt)
	print('	DONE')
	# variants now
	print('modifying variants')
	txt = ''
	for variant in variants:
		started = False
		outfits = []
		splitted = variant.split('\n')
		for line in splitted:
			if line.startswith('	outfits'):
				started = True
				continue
			if started == True:
				if line.startswith('		'):
					outfits.append(line)
				else:
					started = False
					continue
		# get shipname
		pos1 = variant.find('"')
		pos2 = variant.find('"', pos1+1)
		newoutfit = '"' + variant[pos1+1: pos2] + ' Core"'
		# create replacing
		outfitreplace = ''
		if outfits != []:
			for outfit in outfits:
				outfitreplace += outfit + '\n'
			newoutfits = outfitreplace + '		' + newoutfit + '\n'
			txt += 'overwrite\n' + variant.replace(outfitreplace, newoutfits) + '\n\n'
	# write txt
	with open('variants.txt', 'w') as target:
		target.writelines(txt)
	print('	DONE')
	return cores


def create_outfitters(cores, objs):
	# get lists with planets and shipyards
	planets, shipyards, new_outfitters = [], [], []
	for obj in objs:
		if obj.startswith('planet '):
			planets.append(obj)
		elif obj.startswith('shipyard '):
			shipyards.append(obj)
	# create new outfitters
	for yard in shipyards:
		added_stuff = False
		splitted = yard.split('\n')
		outfitter_txt = 'outfitter "' + splitted[0].replace('shipyard ', '').replace('"', '') + ' Cores"\n'
		for line in splitted:
			if line.startswith('	'):
				line = line.strip().replace('"', '')
				if line in cores:
					outfitter_txt += '	"' + line + ' Core"\n'
					added_stuff = True
		if added_stuff == True: # remove empty shipyards
			new_outfitters.append(outfitter_txt)
	with open('outfitters.txt', 'w') as target:
		for outfitter in new_outfitters:
			target.writelines(outfitter + '\n\n')
	# add new outfitters to planets
	planets_txt = ''
	for planet in planets:
		change = False
		pos = planet.find('\n')
		outfitter_lines = planet[:pos+1]
		if '	shipyard ' in planet:
			splitted = planet.split('\n')
			for line in splitted:
				if line.startswith('	shipyard '):
					line = line.strip().replace('shipyard ','').replace('"', '')
					outfitter_lines += '	add outfitter "' + line + ' Cores"\n'
					change = True
			if change == True:
				planets_txt += outfitter_lines + '\n\n'
	with open('planets.txt', 'w') as target:
		target.writelines(planets_txt)




	


def run():
	data_folder = 'd:/games/endless sky/data/'
	objs, obj_paths, obj_names = read_everything(data_folder)
	blacklist_attributes = ['		category ', '		licenses', '			', '		weapon', '		"drag"', '		"outfit space"', '		"weapon capacity"', '		"engine capacity"', '		"cargo space"', '		"heat dissipation"', '		"mass"']
	cores = filter(objs, blacklist_attributes)
	create_outfitters(cores, objs)


if __name__ == "__main__":
	run()