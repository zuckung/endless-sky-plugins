import os



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


def filter_jobs(objs):
	print('checking for jobs with cargo/passengers')
	# filter out jobs with cargo
	cargojobs, passengerjobs = [], []
	for obj in objs:
		if obj.startswith('mission '):
			if '\tjob' in obj:
				if 'Bounty ' in obj: # exclude bounty jobs
					continue
				if '\tcargo' in obj and not '\tpassengers' in obj:
					cargojobs.append(obj)
				elif '\tpassengers' in obj and not '\tcargo' in obj:
					passengerjobs.append(obj)
	print('\t', len(cargojobs), ' cargo jobs found')
	print('\t', len(passengerjobs), ' passenger jobs found')
	# variables
	multiply_missions = 10 # generates 10 new missions for each vanilla job
	offering_chance_cargo = '5' # 5 % chance for job to offer
	offering_chance_passenger = '3' # 5 % chance for job to offer
	header = '# ' + str(len(cargojobs) * multiply_missions) + ' cargo jobs added, ' + str(multiply_missions) + ' for every of the ' + str(len(cargojobs)) + ' vanilla cargo jobs.\n'
	header += '# ' + str(len(passengerjobs) * multiply_missions) + ' passenger jobs added, ' + str(multiply_missions) + ' for every of the ' + str(len(passengerjobs)) + ' vanilla passenger jobs.\n\n'
	new_missions_colored = header
	# handle the jobs
	print('creating new jobs')
	print('\t', multiply_missions, ' new jobs for each vanilla job')
	print('\t', offering_chance_cargo, '% offering chance for cargo')
	print('\t', offering_chance_cargo, '% offering chance for passengers')
	# cargo
	for job in cargojobs:
		if '\tcargo ' in job:
			# get cargo line
			pos1 = job.find('\tcargo ')
			pos2 = job.find('\n', pos1)
			cargoline = job[pos1:pos2].strip()
			# get cargo name
			if '"' in cargoline:
				pos1 = cargoline.find('"')
				pos2 = cargoline.find('"', pos1+1)
				cargoname = cargoline[pos1:pos2+1]
			elif 'random ' in cargoline:
				cargoname = 'random '
			else:
				cargoname = ''
			# get cargo numbers
			cargo = cargoline.replace(cargoname, '').replace('cargo ', '').strip()
			cargonumbers = cargo.split(' ') # list with up to 3 values, space separated. cargo number is between first 2. 3rd is the probability
			if len(cargonumbers) == 1:
				number1 = cargonumbers[0]
				number2 = ''
				number3 = ''
			elif len(cargonumbers) == 2:
				number1 = cargonumbers[0]
				number2 = cargonumbers[1]
				number3 = ''
			elif len(cargonumbers) == 3:
				number1 = cargonumbers[0]
				number2 = cargonumbers[1]
				number3 = cargonumbers[2]
			# multiply numbers
			for i in range(2, multiply_missions + 2):
				if len(cargonumbers) == 1:
					new_number1 = int(number1)*5*i
				elif len(cargonumbers) > 1:
					new_number1 = int(number1)*5*i
					new_number2 = int(number2)*5*i
				new_cargoline = 'cargo ' + cargoname + ' ' + str(new_number1) + ' ' + str(new_number2) + ' ' + number3
				# get mission name
				pos = job.find('\n')
				mission_name = job[:pos+1]
				# get mission offering chance
				pos1 = job.find('\t\trandom ')
				pos2 = job.find('\n', pos1)
				chance = job[pos1:pos2]
				# coloring
				if not '\tcolor' in job:
					color = '\tcolor selected "coloring job cargo: selected"\n' +\
						'\tcolor unselected "coloring job cargo: unselected"\n' +\
						'\tcolor unavailable "coloring job cargo: unavailable"\n'
				else:
					color = ''
				# add mission text, replacing the stuff
				new_job = job.replace(cargoline, new_cargoline)
				new_job = new_job.replace(mission_name, mission_name[:-2] + ' Large[' + str(i-1) + ']"\n' + color)
				if chance != '':
					new_job = new_job.replace(chance, '\t\trandom < ' + offering_chance_cargo)
				new_job = new_job.replace('&#60;', '<').replace('&#62;', '>') + '\n'
				new_missions_colored += new_job
	print('\t', len(cargojobs) * multiply_missions, ' cargo jobs added')
	# passengers
	for job in passengerjobs:
		if '\tpassengers ' in job:
			# get passengers line
			pos1 = job.find('\tpassengers ')
			pos2 = job.find('\n', pos1)
			passengerline = job[pos1:pos2].strip()
			# get passenger numbers
			passenger = passengerline.replace('passengers ', '').strip()
			passengernumbers = passenger.split(' ') # list with up to 3 values, space separated. passenger number is between first 2. 3rd is the probability
			if len(passengernumbers) == 1:
				number1 = passengernumbers[0]
				number2 = ''
				number3 = ''
			elif len(passengernumbers) == 2:
				number1 = passengernumbers[0]
				number2 = passengernumbers[1]
				number3 = ''
			elif len(passengernumbers) == 3:
				number1 = passengernumbers[0]
				number2 = passengernumbers[1]
				number3 = passengernumbers[2]
			# multiply numbers
			for i in range(2, multiply_missions + 2):
				if len(passengernumbers) == 1:
					new_number1 = int(number1)*5*i
				elif len(passengernumbers) > 1:
					new_number1 = int(number1)*5*i
					new_number2 = int(number2)*5*i
				new_passengerline = 'passengers ' + str(new_number1) + ' ' + str(new_number2) + ' ' + number3
				# get mission name
				pos = job.find('\n')
				mission_name = job[:pos+1]
				# get mission offering chance
				pos1 = job.find('\t\trandom ')
				pos2 = job.find('\n', pos1)
				chance = job[pos1:pos2]
				# coloring
				if not '\tcolor' in job:
					color = '\tcolor selected "coloring job passenger: selected"\n' +\
						'\tcolor unselected "coloring job passenger: unselected"\n' +\
						'\tcolor unavailable "coloring job passenger: unavailable"\n'
				else:
					color = ''
				# add mission text, replacing the stuff
				new_job = job.replace(passengerline, new_passengerline)
				new_job = new_job.replace(mission_name, mission_name[:-2] + ' Large[' + str(i-1) + ']"\n' + color)
				if chance != '':
					new_job = new_job.replace(chance, '\t\trandom < ' + offering_chance_passenger)
				new_job = new_job.replace('&#60;', '<').replace('&#62;', '>') + '\n'
				new_missions_colored += new_job
	print('\t', len(passengerjobs) * multiply_missions, ' passenger jobs added')
	# write to file
	print('writing to file')
	with open('new_jobs.txt', 'w') as target:
		target.writelines(new_missions_colored)
	print('\tDONE')


def run():
	data_folder = 'd:/games/endless sky/data/'
	objs, obj_paths, obj_names = read_everything(data_folder)
	filter_jobs(objs)


if __name__ == "__main__":
	run()