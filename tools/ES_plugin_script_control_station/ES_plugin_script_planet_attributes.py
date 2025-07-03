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


def filter_planets(obj):
	event1txt, event2txt = '', ''
	event1txt = 'event "add planet attributes"\n'
	event2txt = 'event "remove planet attributes"\n'
	with open('ES_plugin_script_planet_attributes_template.txt', 'r') as source:
		mission = source.read()
	for each in obj:
		if each.startswith('planet '):
			if '\tattributes' in each:
				pos2 = each.find('\n')
				planet = each[:pos2]
				#print(planet)
				pos1 = each.find('\tattributes')
				pos2 = each.find('\n', pos1)
				attributes = each[pos1+12:pos2]
				#print(attributes)
				olddescription = ''
				while '\tdescription' in each:
					pos1 = each.find('\tdescription `')
					pos2 = each.find('`', pos1 + 15)
					olddescription += each[pos1:pos2+1] + '\n'
					each = each[pos2:]
				event1txt += '\t' + planet + '\n\t\tadd description `[attributes: ' + attributes + ']`\n'
				event2txt += '\t' + planet + '\n' + olddescription.replace('\t', '\t\t')
	with open('control.station.2.planet.attributes.txt', 'w') as target:
		target.writelines(mission + '\n\n' +event1txt + '\n\n' + event2txt)

	
def run():
	data_folder = '/storage/9C33-6BBD/endless sky/data/' # change to your folder
	obj, obj_path, obj_name = read_everything(data_folder)
	filter_planets(obj)
	

if __name__ == "__main__":
	run()
