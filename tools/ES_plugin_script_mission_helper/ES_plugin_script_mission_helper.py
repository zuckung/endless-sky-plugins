import os


def set_globals():
	print('setting global variables')
	global obj, obj_path, obj_name, data_folder
	obj, obj_path, obj_name = [], [], []
	data_folder = '/storage/9C33-6BBD/endless sky/data/' # change to your folder


def read_everything(): # reading the data folder
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
	print('\n\n')


def list_systems():
	systems, govs = [], []
	for each in obj:
		if each.startswith('system'):
			system = each[:each.find('\n')].replace('system ','').replace('"', '').strip()
			gov = each[each.find('\tgovernment '):each.find('\n', each.find('\tgovernment '))+1].replace('government ', '').replace('"', '').strip()
			if gov !=  'Republic' and not 'Pirate' in gov and gov != 'Syndicate':
				if gov == 'Bunrodea (Guard)':
					gov = 'bunrodea'
				elif gov == 'Bunrodea':
					gov = 'bunrodea'
				elif gov == 'Heliarch':
					gov = 'coalition'
				elif gov == 'Coalition':
					gov = 'coalition'
				elif gov == 'Gegno Scin':
					gov = 'gegno'
				elif gov == 'Gegno':
					gov = 'gegno'
				elif gov == 'Gegno Vi':
					gov = 'gegno'
				elif gov == 'Hai (Unfettered)':
					gov = 'hai'
				elif gov == 'Hai':
					gov = 'hai'
				elif gov == 'Successor':
					gov = 'successors'
				elif gov == 'Old Houses':
					gov = 'successors'
				elif gov == 'New Houses':
					gov = 'successors'
				elif gov == 'Wanderer':
					gov = 'wanderer'
				elif gov == "People's Houses":
					gov = 'successors'
				elif gov == 'Avgi (Consonance)':
					gov = 'avgi'
				elif gov == 'Avgi (Dissonance)':
					gov = 'avgi'
				elif gov == 'Avgi (Twilight Guard)':
					gov = 'avgi'
				elif gov == 'Avgi':
					gov = 'avgi'
				elif gov == 'Hicemus':
					gov = 'incipias'
				elif gov == 'Kor Mereti':
					gov = 'korath'
				elif gov == 'Kor Sestor':
					gov = 'korath'
				elif gov == 'Kor Efret':
					gov = 'korath'
				elif gov == 'Korath':
					gov = 'korath'				
				elif gov == "Ka'het":
					gov = "kahet"
				elif gov == 'Rulei':
					gov = "rulei"
				elif gov == 'Drak':
					gov = "drak"
				elif gov == 'Remnant':
					gov = "remnant"
				elif 'Pug' in gov:
					gov = 'pug'
				elif 'Quarg' in gov:
					gov = 'quarg'
				elif '"graveyard"' in each:
					gov = 'kahet'
				elif '"rulei"' in each:
					gov = 'rulei'
				else:
					if gov != 'Uninhabited':
						print(gov)
				systems.append(system)
				govs.append(gov)
	return systems, govs
		
	

def list_missions(): # lists the mission names, paths and relevant script texts
	missions, mission_texts, mission_paths, starts = [], [], [], []
	for name in obj_name:
		if not name.startswith('mission '):
			continue
		index = obj_name.index(name)
		if '\trepeat' in obj[index]:
			continue
		if 'deprecated' in obj_path[index] or 'globals.txt' in obj_path[index] or 'starts.txt' in obj_path[index]:
			continue
		# get starts
		if '\tlanding\n' in obj[index]:
			starts.append('landing')
		elif '\tassisting\n' in obj[index]:
			starts.append('assisting')
		elif '\tboarding\n' in obj[index]:
			starts.append('boarding')
		elif '\tshipyard\n' in obj[index]:
			starts.append('shipyard')
		elif '\toutfitter\n' in obj[index]:
			starts.append('outfitter')
		elif '\t"job board"\n' in obj[index]:
			starts.append('job board')
		elif '\tentering\n' in obj[index]:
			starts.append('entering')
		else:
			starts.append('spaceport')
		# clean up mission name	
		pos1 = name.find('"')
		pos2 = name.find('"', pos1 +1)
		name = name[pos1+1:pos2]
		# clean up mission path
		path = obj_path[index].replace('data/','')
		# clean up the mission text
		source = ''
		started, started2, started3, started4 = 0, 0, 0, 0
		lines = obj[index].split('\n')
		for line in lines:
			# get passengers/cargo
			if line.startswith('\tpassengers '):
				source += line + '\n'
				continue
			elif line.startswith('\tcargo '):
				source += line + '\n'
				continue
		for line in lines:
			# get source block
			if line.startswith('\tsource'):
				source += line + '\n'
				started = 1
				continue
			elif started == 1:
				if line.startswith('\t\t'):
					source += line + '\n'
					continue
				else:
					started = 0
		for line in lines:
			# get to offer block
			if line.startswith('\tto offer'):
				source += line + '\n'
				started = 1
				continue
			if started == 1:
				if line.startswith('\t\t'):
					source += line.replace('&#60;','<').replace('&#62;', '>') + '\n'
					continue
				else:
					started = 0
			# get to fail block
			if line.startswith('\tto fail'):
				source += line + '\n'
				started2 = 1
				continue
			if started2 == 1:
				if line.startswith('\t\t'):
					source += line.replace('&#60;','<').replace('&#62;', '>') + '\n'
					continue
				else:
					started2 = 0
			# get to complete block
			if line.startswith('\tto complete'):
				source += line + '\n'
				started3 = 1
				continue
			if started3 == 1:
				if line.startswith('\t\t'):
					source += line.replace('&#60;','<').replace('&#62;', '>') + '\n'
					continue
				else:
					started3 = 0
			# get to accept block
			if line.startswith('\tto complete'):
				source += line + '\n'
				started4 = 1
				continue
			if started4 == 1:
				if line.startswith('\t\t'):
					source += line.replace('&#60;','<').replace('&#62;', '>') + '\n'
					continue
				else:
					started4 = 0			
		missions.append(name)
		mission_texts.append(source)
		mission_paths.append(path)
	return missions, mission_texts, mission_paths, starts


def write_mission(missions, mission_texts, mission_paths, systems, govs, blacklist, starts): # write all to a single mission
	with open('mission.helper.txt', 'w') as target:
		target.writelines('# mission "Mission Helper"\n')
		target.writelines('# 2x color\n')
		target.writelines('\n')
		target.writelines('\n')
		target.writelines('\n')
		target.writelines('color "mission helper job: selected" .1 .8 .1 0.\n')
		target.writelines('color "mission helper job: unselected" .1 .5 .2 0.\n')
		target.writelines('\n')
		target.writelines('\n')
		target.writelines('mission "Mission Helper"\n')
		target.writelines('\tname "(Mission Helper)"\n')
		target.writelines('\tcolor selected "mission helper job: selected"\n')
		target.writelines('\tcolor unselected "mission helper job: unselected"\n')
		target.writelines('\tjob\n')
		target.writelines('\trepeat\n')
		target.writelines('\tdescription "Shows a list of non-repeatable, not-offered missions. You only see missions you have not done. The missions show their offering conditions, so you can easily check where to go and what to do for them to start."\n')
		target.writelines('\ton accept\n')
		target.writelines('\t\tconversation\n')
		target.writelines('\t\t\tlabel "realstart"\n')
		target.writelines('\t\t\t`This job shows a list of non-repeatable, not-offered missions. You only see missions you have not done. But there are also missions you can not do, because you took another path in these mission chains. The missions show their offering conditions, so you can easily check where to go and what to do for them to start.`\n')
		target.writelines('\t\t\t`Navigate through the races and their mission sub categories to find missions you have not done. In the races menu you can choose [help] to get a small overview on how to read the conditions for mission offering.`\n')
		target.writelines('\t\t\tchoice\n')
		target.writelines("\t\t\t\t`\t(NO SPOILERS) exclude races you haven't met`\n")
		target.writelines('\t\t\t\t\tgoto nospoil\n')
		target.writelines('\t\t\t\t`\t(SPOILERS) show all races`\n')
		target.writelines('\t\t\t\t\tgoto spoil\n')
		target.writelines('\t\t\tlabel spoil\n')
		target.writelines('\t\t\taction\n')
		target.writelines('\t\t\t\tset "helper spoiler"\n')
		target.writelines('\t\t\t\tclear "helper no spoiler"\n')
		target.writelines('\t\t\t`You have chosen the SPOILER version`\n')
		target.writelines('\t\t\t\tgoto afterspoil\n')
		target.writelines('\t\t\tlabel nospoil\n')
		target.writelines('\t\t\taction\n')
		target.writelines('\t\t\t\tset "helper no spoiler"\n')
		target.writelines('\t\t\t\tclear "helper spoiler"\n')
		target.writelines('\t\t\t`You have chosen the NO SPOILER version`\n')
		target.writelines('\t\t\tlabel "afterspoil"\n')
		target.writelines('\t\t\t`Have fun with this plugin!`\n')
		target.writelines('\t\t\tchoice\n')
		target.writelines('\t\t\t\t`continue`\n')
		target.writelines('\t\t\t\t\tgoto start\n')
		target.writelines('\t\t\tlabel "start"\n')
		target.writelines('\t\t\t`Choose a race, choose a sub category, and choose a mission to see the conditions for offering.`\n')
		target.writelines('\t\t\t`Races:`\n')
		target.writelines('\t\t\tchoice\n')
		target.writelines('\t\t\t\t`[help]`\n')
		target.writelines('\t\t\t\t\tgoto "help"\n')
		# start menu races/folder
		categories = []
		for path in mission_paths:
			pathpath, pathfile = path.split('/')
			if pathpath in categories:
				continue
			# filter races
			categories.append(pathpath)
			target.writelines('\t\t\t\t`' + pathpath + '`\n')
			if pathpath == 'human':
				stub = 1
			elif pathpath in blacklist:
				target.writelines('\t\t\t\t\tto display\n')
				target.writelines('\t\t\t\t\t\thas "not in blacklist"\n')
			elif pathpath == 'sheragi':
				target.writelines('\t\t\t\t\tto display\n')
				target.writelines('\t\t\t\t\t\tor\n')
				target.writelines('\t\t\t\t\t\t\thas "helper spoiler"\n')
				target.writelines('\t\t\t\t\t\t\thas "Rim Archaeology 6: declined"\n')
			else:
				target.writelines('\t\t\t\t\tto display\n')
				target.writelines('\t\t\t\t\t\tor\n')
				target.writelines('\t\t\t\t\t\t\thas "helper spoiler"\n')
				target.writelines('\t\t\t\t\t\t\tor\n')
				for system in systems:
					sysindex = systems.index(system)
					if govs[sysindex].lower() == pathpath:
						target.writelines('\t\t\t\t\t\t\t\thas "visited system: ' + system + '"\n')
			target.writelines('\t\t\t\t\tgoto "' + pathpath + '"\n')
		target.writelines('\t\t\t\t`[close]`\n')
		target.writelines('\t\t\t\t\tgoto "close"\n')
		# sub category menu/files	
		for category in categories:
			files = []
			target.writelines('\t\t\tlabel "' + category + '"\n')
			target.writelines('\t\t\t`Choose a race, choose a sub category, and choose a mission to see the conditions for offering.`\n')
			target.writelines('\t\t\t`' + category.capitalize() + ' | Sub category:`\n')
			target.writelines('\t\t\tchoice\n')
			target.writelines('\t\t\t\t`[back to "Races"]`\n')
			target.writelines('\t\t\t\t\tgoto "start"\n')	
			for path in mission_paths:
				if not path.startswith(category):
					continue
				file = path.split('/')[1]
				if file in files:
					continue
				files.append(file)
				target.writelines('\t\t\t\t`' + file.replace('.txt', '') + '`\n')
				target.writelines('\t\t\t\t\tgoto "' + category + '/' + file + '"\n')
			# missions menu
			for file in files:
				target.writelines('\t\t\tlabel "'+ category + '/' + file + '"\n')
				target.writelines('\t\t\t`Choose a race, choose a sub category, and choose a mission to see the conditions for offering.`\n')
				target.writelines('\t\t\t`' + category.capitalize() + ' | ' + file.capitalize().replace('.txt', '') + ' | Mission:`\n')
				target.writelines('\t\t\tchoice\n')
				target.writelines('\t\t\t\t`[back to "' + category.capitalize() + '"]`\n')
				target.writelines('\t\t\t\t\tgoto "' + category+ '"\n')
				target.writelines('\t\t\t\t`[back to "Races"]`\n')
				target.writelines('\t\t\t\t\tgoto "start"\n')
				for mission in missions:
					index = missions.index(mission)
					if not category + '/' + file in mission_paths[index]:
						continue
					target.writelines('\t\t\t\t`' + mission + '`\n')
					target.writelines('\t\t\t\t\tto display\n')
					target.writelines('\t\t\t\t\t\tnot "' + mission + ': offered"\n')
					target.writelines('\t\t\t\t\tgoto "' + mission + '"\n')
		# each mission display		
		for mission in missions:
			index = missions.index(mission)
			target.writelines('\t\t\tlabel "' + mission + '"\n')
			target.writelines('\t\t\t`' + mission_paths[index] + ' | mission "' + mission + '"`\n')
			target.writelines('\t\t\t`starts at: ' + starts[index] + '`\n')
			category, subcategory = mission_paths[index].split('/')
			splitted = mission_texts[index].split('\n')
			for each in splitted:
				target.writelines('\t\t\t`' + each + '`\n')
			# display what the player has got
			target.writelines('\t\t\t`You have the following missions, events and conditions:`\n')
			started = 0
			for each in splitted:
				if each.startswith('\tsource'):
					started = 1
					continue
				elif started == 1:
					if each.startswith('\t\t'):
						continue
					elif each.startswith('\t'):
						started = 0
						continue
				elif each.startswith('\tto offer'):
					continue
				elif each == '':
					continue
				elif '#'in each:
					continue
				elif '\tor' in each or '\tand' in each or 'random' in each:
					continue
				elif each.startswith('\tto fail'):
					continue
				elif each.startswith('\tto complete'):
					continue
				elif each.startswith('\tto accept'):
					continue
				elif each.startswith('\tpassengers'):
					continue
				elif each.startswith('\tcargo'):
					continue
				else:
					mstatus = each.replace('\t', '').strip()
					target.writelines('\t\t\t`' + mstatus + '`\n')
					target.writelines('\t\t\t\tto display\n')
					target.writelines('\t\t\t\t\t' + mstatus + '\n')
			target.writelines('\t\t\t``\n')	
			target.writelines('\t\t\tchoice\n')
			target.writelines('\t\t\t\t`[back to "' + category.capitalize() + ' | ' + subcategory.capitalize().replace('.txt', '') + '""]`\n')
			target.writelines('\t\t\t\t\tgoto "' + category + '/' + subcategory + '"\n')
			target.writelines('\t\t\t\t`[back to "' + category.capitalize() + '"]`\n')
			target.writelines('\t\t\t\t\tgoto "' + category + '"\n')
			target.writelines('\t\t\t\t`[back to "Races"]`\n')
			target.writelines('\t\t\t\t\tgoto "start"\n')
		# write the help text
		target.writelines('\t\t\tlabel help\n')
		with open('template.txt', 'r') as source:
			lines = source.readlines()
		for line in lines:
			target.writelines('\t\t\t`' + line.replace('\n', '') + '`\n')
		target.writelines('\t\t\tchoice\n')
		target.writelines('\t\t\t\t`[back to "Races"]`\n')
		target.writelines('\t\t\t\t\tgoto "start"\n')
		# when all is done write the mission end
		target.writelines('\t\t\tlabel "close"\n')
		target.writelines('\t\t\t`I hope that helped!`\n')
		target.writelines('\t\t\t\tdecline\n')
		target.writelines('\t\tfail\n')
		

def run():
	set_globals()
	read_everything()
	systems, govs = list_systems()
	missions, mission_texts, mission_paths, starts = list_missions()
	blacklist = [''] # exclude these races from the race menu (no missions/no systems)
	write_mission(missions, mission_texts, mission_paths, systems, govs, blacklist, starts)


if __name__ == "__main__":
	run()