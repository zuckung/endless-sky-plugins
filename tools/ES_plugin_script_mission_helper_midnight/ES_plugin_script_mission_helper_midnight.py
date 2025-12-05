import os


def set_globals():
	print('setting global variables')
	global obj, obj_path, obj_name, data_folder, data_folders
	obj, obj_path, obj_name = [], [], []
	#data_folder = '/storage/9C33-6BBD/endless sky/data/' # change to your folder
	data_folders = 'D:/download/ES_plugin_script_mission_helper/Lost in Midnight/data/','D:/download/ES_plugin_script_mission_helper/Midnight Expansion/data/', 'D:/download/ES_plugin_script_mission_helper/Midnight Scrapyard/data/'


def read_everything(): # reading the data folder
	started = False
	for data_folder in data_folders:
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


def list_missions(): # lists the mission names, paths and relevant script texts
	missions, mission_texts, mission_paths, starts = [], [], [], []
	for name in obj_name:
		if not name.startswith('mission '):
			continue
		index = obj_name.index(name)
		if '\trepeat' in obj[index]:
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


def write_mission(missions, mission_texts, mission_paths, blacklist, starts): # write all to a single mission
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
		target.writelines('mission "Mission Helper Midnight"\n')
		target.writelines('\tname "(Mission Helper Midnight)"\n')
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
		target.writelines('\t\t\t`Have fun with this plugin!`\n')
		target.writelines('\t\t\tchoice\n')
		target.writelines('\t\t\t\t`continue`\n')
		target.writelines('\t\t\t\t\tgoto start\n')
		target.writelines('\t\t\tlabel "start"\n')
		target.writelines('\t\t\t`Choose a category, choose a sub category, and choose a mission to see the conditions for offering.`\n')
		target.writelines('\t\t\t`Categories:`\n')
		target.writelines('\t\t\tchoice\n')
		target.writelines('\t\t\t\t`[help]`\n')
		target.writelines('\t\t\t\t\tgoto "help"\n')
		# start menu races/folder
		categories = []
		for path in mission_paths:
			splitted = path.split(os.sep)
			if len(splitted) > 2:
				pathpath = ''
				for i in range(0, len(splitted)-1):
					pathpath += splitted[i] + os.sep
				pathfile = splitted[-1]
			elif len(splitted) == 2:
				pathpath = splitted[0] + os.sep
				pathfile = splitted[1]
			if pathpath in categories:
				continue
			# filter races
			categories.append(pathpath)
			target.writelines('\t\t\t\t`' + pathpath + '`\n')
			target.writelines('\t\t\t\t\tgoto "' + pathpath + '"\n')
		target.writelines('\t\t\t\t`[close]`\n')
		target.writelines('\t\t\t\t\tgoto "close"\n')
		# sub category menu/files	
		for category in categories:
			#print(category)
			files = []
			target.writelines('\t\t\tlabel "' + category + '"\n')
			target.writelines('\t\t\t`Choose a category, choose a sub category, and choose a mission to see the conditions for offering.`\n')
			target.writelines('\t\t\t`' + category + ' | Sub category:`\n')
			target.writelines('\t\t\tchoice\n')
			target.writelines('\t\t\t\t`[back to "Categories"]`\n')
			target.writelines('\t\t\t\t\tgoto "start"\n')	
			for path in mission_paths:
				splitted = path.split(os.sep)
				path = ''
				file = splitted[-1]
				for i in range(0, len(splitted)-1):
					path += splitted[i] + os.sep
				if not path == category:
					continue
				if file in files:
					continue
				files.append(file)
				target.writelines('\t\t\t\t`' + file.replace('.txt', '') + '`\n')
				target.writelines('\t\t\t\t\tgoto "' + category + file + '"\n')
			# missions menu
			for file in files:
				target.writelines('\t\t\tlabel "'+ category + file + '"\n')
				target.writelines('\t\t\t`Choose a category, choose a sub category, and choose a mission to see the conditions for offering.`\n')
				target.writelines('\t\t\t`' + category + file + ' | Missions:`\n')
				target.writelines('\t\t\tchoice\n')
				target.writelines('\t\t\t\t`[back to "' + category + '"]`\n')
				target.writelines('\t\t\t\t\tgoto "' + category + '"\n')
				target.writelines('\t\t\t\t`[back to "Categories"]`\n')
				target.writelines('\t\t\t\t\tgoto "start"\n')
				for mission in missions:
					index = missions.index(mission)
					if not category + file == mission_paths[index]:
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
			splitted = mission_paths[index].split(os.sep)

			if len(splitted) < 2:
				category = ''
				subcategory = mission_paths[index]
			elif len(splitted) > 2:
				category = ''
				paths = splitted
				for i in range(0, len(paths)-1):
					category += paths[i] + os.sep
				subcategory = paths[-1]
			else:
				category = splitted[0] + os.sep
				subcategory = splitted[1]
				
			# display what the player has got
			splitted = mission_texts[index].split('\n')
			for each in splitted:
				target.writelines('\t\t\t`' + each + '`\n')
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
			target.writelines('\t\t\t\t`[back to "' + category + subcategory + '""]`\n')
			target.writelines('\t\t\t\t\tgoto "' + category + subcategory + '"\n')
			target.writelines('\t\t\t\t`[back to "' + category + '"]`\n')
			target.writelines('\t\t\t\t\tgoto "' + category + '"\n')
			target.writelines('\t\t\t\t`[back to "Categories"]`\n')
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
	missions, mission_texts, mission_paths, starts = list_missions()
	blacklist = [''] # exclude these races from the race menu (no missions/no systems)
	write_mission(missions, mission_texts, mission_paths, blacklist, starts)


if __name__ == "__main__":
	run()