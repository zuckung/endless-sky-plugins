# checks every object of the datafolder and writes every matching object to a text file
# i.e seach='system' and attribute=''Large Kor Mereti'' gives all systems names, which have a large mereti fleet spawn


import os


def set_globals():
	print('setting global variables')
	global data_folder
	global planets
	global obj
	global obj_path
	global obj_name
	global output
	global final_output
	global search
	global attribute
	obj, obj_path, obj_name, output, final_output = [], [], [], [], []
	search = 'ship'  # first filter, always lowercase
	attribute = "remnant capital" # content filter, gets converted to lowercase
	data_folder = '/storage/9C33-6BBD/endless sky/data/' # change to your folder


def read_everything():
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


def search_obj():
	print('\nsearching object and attribute')
	for line in obj_name:
		pos = 0
		if line.startswith(search): # checks for object
			index = obj_name.index(line)
			pos = obj[index].lower().find(attribute.lower(), 0) # checks for attribute
			if pos > 0:
				output.append(obj_name[index])
				objlines = obj[index].split('\n')
				for objline in objlines:
					if objline.lower().find(attribute.lower(), 0) > 0:
						final_output.append(objline + '\n')
				print(obj_name[index])
				index2 = output.index(obj_name[index])
				print(final_output[index2])


def write_list():
	with open('list.txt', 'w') as target:
		for each in output:
			index = output.index(each)
			target.writelines(each + '\n')
			target.writelines(final_output[index] + '\n')


def run():
	set_globals()
	read_everything()
	search_obj()
	write_list()


if __name__ == "__main__":
	run()