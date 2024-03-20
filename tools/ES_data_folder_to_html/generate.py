import os
import time

def read_template():
	with open('template.txt', 'r') as file1:
		templates_all = file1.read()
		templates = templates_all.split('%cut template here%')
	menu_template = templates[0]
	category_template = templates[1]
	object_template = templates[2]
	return menu_template, category_template, object_template
	
def read_everything():
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
				if os.path.isfile(data_folder + folder + '/' + text_file) == False:
					continue
				if len(folder + text_file)  < 80: # just for displaying / max len = 44(currently)
					count = 80 - len(folder + text_file)
					spaces = ''
					for i in range(0, count):
						spaces += ' '
				print('reading: ' + folder + '/' + text_file + spaces, end = '\r', flush= True)
				#time.sleep(.01)
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
	return obj, obj_path, obj_name

def get_object_categories():
	categories = []
	for obj in object_names:
		if obj[:1] == '"':
			pos = obj.find('"', 1) + 1
			category = obj[:pos]
		else:
			category = obj.split(' ')[0]
		if category in categories:
			continue
		else:
			categories.append(category)
	categories.sort()
	return categories

def write_menu():
	splitted = menu_template.split('%categories%')
	with open('page/menu.html', 'w') as file1:
		print('creating menu.html')
		file1.writelines(splitted[0])
		catpos = 0
		for each in categories:
			each = each.replace('"', '').replace(' ', '_')
			file1.writelines('<a href="' + each + '.html" target="main">' + each + '</a>  (' + str(counting[catpos]) + ')<br>\n')
			catpos += 1
		file1.writelines(splitted[1])

def write_html():
	counting = []
	for category in categories:
		catcount = 0
		catfile = category.replace('"', '').replace(' ', '_')
		print('creating ' + catfile.strip() + '.html')
		with open('page/' + catfile.strip() + '.html', 'w') as file1:
			splitted = category_template.split('%tmpl%')
			file1.writelines(splitted[0])
			for obj_name in object_names:
				if obj_name.startswith(category + ' ') or obj_name.startswith(category + '\t') or obj_name == (category):
					catcount += 1
					o_index = object_names.index(obj_name)
					obj_path = object_paths[o_index]
					obj = objects[o_index]
					txt = object_template.replace('%filename%', obj_path).replace('%objectname%', obj_name).replace('%object%', obj)
					#print(each)		
					file1.writelines(txt + '\n')
			file1.writelines(splitted[1])
			counting.append(catcount)
	return counting

data_folder = '/storage/9C33-6BBD/endless sky/data/'
menu_template, category_template, object_template = read_template()
objects, object_paths, object_names = read_everything() # creates list of objects, a list of each path and each name
categories = get_object_categories()

counting = write_html()
write_menu()