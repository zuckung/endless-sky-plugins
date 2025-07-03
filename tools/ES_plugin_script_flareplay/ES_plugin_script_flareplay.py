import os
from PIL import Image


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


def find_flares(objs):
	def find_flare_effect(obj, special):
		started = False
		flare_effect = ''
		flare_list = []
		lines = obj.split('\n')
		for line in lines:
			# check for any flare lines
			if special != '':
				if special in line:
					if started == True:
						started = False
						flare_list.append(flare_effect)
						flare_effect = ''
					else:
						started = True
						flare_effect += line + '\n'
				elif line.startswith('\t\t'):
					if started == True:
						flare_effect += line + '\n'
				else:
					if started == True:
						started = False
						flare_list.append(flare_effect)
						flare_effect = ''
			else:
				if 'flare sprite' in line or 'afterburner effect' in line:
					if started == True:
						started = False
						flare_list.append(flare_effect)
						flare_effect = ''
					else:
						started = True
						flare_effect += line + '\n'
				elif line.startswith('\t\t'):
					if started == True:
						flare_effect += line + '\n'
				else:
					if started == True:
						started = False
						flare_list.append(flare_effect)
						flare_effect = ''
		return flare_list
	# get all flare outfits
	flare_effect_scripts, flare_effects, flare_effects0, obj_effects_list, obj_outfits_list = [], [], [], [], []
	print('FILTERING FLARE EFFECTS')
	print('\tfiltering all objs')
	for obj in objs:
		if obj.startswith('effect '):
			obj_effects_list.append(obj)
		elif obj.startswith('outfit '):
			if 'flare sprite' in obj or 'afterburner effect' in obj:
				obj_outfits_list.append(obj)
	print('\tfiltering all flaresprites')
	for obj in obj_outfits_list:
		flare_list = find_flare_effect(obj, '')
		for each in flare_list:
			if not each in flare_effect_scripts:
				flare_effect_scripts.append(each)
				flare_effects0.append(each)
	for each in flare_effects0:
		if 'afterburner effect' in each:
			afterburner_effect_name = each.replace('"afterburner effect" ', '').strip()
			pos2 = afterburner_effect_name.find('"', 2)
			afterburner_effect_name = afterburner_effect_name[0:pos2+1]
			for effect in obj_effects_list:
				if effect.startswith('effect ' + afterburner_effect_name):
					flare_list = find_flare_effect(effect, 'sprite')
					for item in flare_list:
						flare_effects.append(item) # flare effect script
					break
		else:
			flare_effects.append(each)					
	print('\t\tscript parts found:', len(flare_effect_scripts)) # 155 # 187 if not checked for doubles
	print('\t\tflare effects found:', len(flare_effects)) # 155
	# sort lists here			
	flare_effect_scripts, flare_effects = (list(x) for x in zip(*sorted(zip(flare_effect_scripts, flare_effects))))
	list1, list1b, list2, list2b, list3, list3b, list4, list4b = [], [], [], [], [], [], [], []
	index = -1
	for each in flare_effect_scripts:
		index += 1
		if 'afterburner effect' in each:
			if 'remass injection' in each:
				list1.append(each)
				list1b.append(flare_effects[index])
			elif 'successor' in each:
				list2.append(each)
				list2b.append(flare_effects[index])
			else:
				list3.append(each)
				list3b.append(flare_effects[index])
		else:
			list4.append(each)
			list4b.append(flare_effects[index])
	flare_effect_scripts = list3 + list1 + list2 + list4
	flare_effects = list3b + list1b + list2b + list4b
	return flare_effect_scripts, flare_effects
	



def writetxtfile(flare_effect_scripts, flare_effects):
	# check folders
	print('CREATING FOLDERS')
	if not os.path.isdir('data'):
		os.mkdir('data')
	if not os.path.isdir('images'):
		os.mkdir('images')
	if not os.path.isdir('images' + os.sep + 'effect'):
		os.mkdir('images' + os.sep + 'effect')
	if not os.path.isdir('images' + os.sep + 'effect' + os.sep + 'newflares'):
		os.mkdir('images' + os.sep + 'effect' + os.sep + 'newflares')
	print('CREATING OUTFITS')
	# preset texts
	outfitter_text = 'outfitter "FlarePlay"\n'
	outfitter_line = '\t"%outfitname%"\n'
	outfit_text_template = '\noutfit "%outfitname%"\n' +\
		'\t"display name" "%displayname%"\n' +\
		'\tcategory "FlarePlay"\n' +\
		'\t"thumbnail" "%thumbnail%"\n' +\
		'\t"cost" %cost%\n' +\
		'\t"mass" 1\n' +\
		'%flarestats%' +\
		'\tseries "Flareplay"\n' +\
		'\tindex %index%\n' +\
		'\tdescription `This is an engine additive of a company named FlarePlay. An engine exhaust coloration appears ' +\
		'when additives like strontium, copper, cesium or others are introduced, burning at high temperatures and ' +\
		'emitting vivid colors... red from strontium, green from copper, blue from cesium. The result is a striking exhaust ' +\
		'plume used for flight shows, research on combustion efficiency, or just to let your spaceship look cool.`\n' +\
		'\tdescription `Due to varying engine characteristics, additives are limited to their designated propulsion systems: ' +\
		'afterburner flare for afterburners, reverse flare for reverse thrusters, steering flare for steering thrusters, ' +\
		'and standard flare for primary thrusters.`\n' +\
		"\tdescription `You don't know what it means or if it is important, but on the package you can read:`\n" +\
		"\tdescription `'%original%'`\n"
	# getting variables
	counter = 5000
	outfit_texts = []
	outfitter_texts = []
	original_paths, effect_types = [], []
	for each in flare_effect_scripts:
		index = flare_effect_scripts.index(each)
		first_line = each[0:each.find('\n')].strip()
		first_line_split = first_line.split('" "')
		part1 = first_line_split[0].replace('"','').strip()
		# original_path, frame_rate, scale for all except afterburner
		original_path = first_line_split[1][0:first_line_split[1].find('"')] # effect/bla/bla
		frame_rate = each[each.find("frame rate")+12:each.find('\n', each.find("frame rate")+13)] if 'frame rate' in each else '1' # 30
		scale = each[each.find("scale")+7:each.find('\n', each.find("scale")+7)] if 'scale' in each else '' # 0.6
		# effect_type
		effect_type = part1
		effect_type = effect_type.replace(' effect', '') if effect_type == 'afterburner effect' else effect_type
		effect_type = effect_type.replace(' sprite', '') if effect_type == 'flare sprite' else effect_type
		effect_type = effect_type.replace(' flare sprite', '') if effect_type == 'reverse flare sprite' else effect_type
		effect_type = effect_type.replace(' flare sprite', '') if effect_type == 'steering flare sprite' else effect_type # afterburner, flare, reverse, steering
		# original_path, frame_rate, scale for afterburner
		if effect_type == 'afterburner': # fix for afterburner stats
			original_path = flare_effects[index][0:flare_effects[index].find('\n')].strip().replace('sprite ', '').replace('"','') # effect/bla/bla
			frame_rate = flare_effects[index][flare_effects[index].find("frame rate")+12:flare_effects[index].find('\n', \
				flare_effects[index].find("frame rate")+12)] if 'frame rate' in flare_effects[index] else '1' # 30
			scale = flare_effects[index][flare_effects[index].find("scale")+7:flare_effects[index].find('\n', \
				flare_effects[index].find("scale")+7)] if 'scale' in flare_effects[index] else '' # 0.6
		scale = '0' + scale if scale.startswith('.') else scale
		scale = scale + '.0' if len(scale) == 1 else scale
		# setting lists for image creation
		original_paths.append(original_path)
		effect_types.append(effect_type)
		# outfitname
		new_scale = '1.0' if scale == '' else scale
		outfitname = effect_type + ' ' + original_path.replace('effect', '').replace('/', ' ').strip() + ' ' + new_scale + ' ' + frame_rate
		# outfitter
		outfitter_texts.append('\t"' + outfitname + '"\n')
		# displayname
		if 'tiny' in original_path:
			sizeword = 'Tiny'
			cost_multiplier = '0.2'
		elif 'small' in original_path:
			sizeword = 'Small'
			cost_multiplier = '0.4'
		elif 'medium' in original_path:
			sizeword = 'Medium'
			cost_multiplier = '0.6'
		elif 'med' in original_path:
			sizeword = 'Medium'
			cost_multiplier = '0.8'
		elif 'large' in original_path:
			sizeword = 'Large'
			cost_multiplier = '1.0'
		elif 'huge' in original_path:
			sizeword = 'Huge'
			cost_multiplier = '1.2'
		else:
			sizeword = ''
			cost_multiplier = '1.0'
		sizeword = sizeword if scale == '' and sizeword != '' else scale
		sizeword = sizeword if sizeword != '' else '1.0'
		displayname = 'FP%counter%' + ' size: ' + sizeword
		# cost & index
		if effect_type == 'afterburner':
			cost = 20000
			findex = '99900'
		if effect_type == 'reverse':
			cost = 30000
			findex = '99700'
		if effect_type == 'steering':
			cost = 30000
			findex = '99800'
		if effect_type == 'flare':
			cost = 40000
			findex = '99600'
		# thumbnail
		scale = '1.0' if scale == '' else scale
		thumbnail = 'effect' + os.sep + 'newflares' + os.sep + original_path.replace('effect', '').replace('/', ' ').strip() + ' ' + effect_type
		outfit_text = outfit_text_template
		outfit_text = outfit_text.replace('%outfitname%', outfitname).replace('%displayname%', displayname)
		outfit_text = outfit_text.replace('%cost%', str(int(cost*float(scale)*float(cost_multiplier))))
		outfit_text = outfit_text.replace('%thumbnail%', thumbnail).replace('%flarestats%', each).replace('%index%', findex)
		outfit_text = outfit_text.replace('%original%', original_path.replace('effect/', '') + ' sc:' + scale + '/fr:' + frame_rate)
		outfit_texts.append(outfit_text)
	outfit_texts.sort()
	outfitter_texts.sort()
	# write new color outfits
	filelist = os.listdir('images/effect/newcolors/')
	counter2 = 0
	for file in filelist:
		pos1 = file.find('+')
		pos2 = file.find('.', pos1)
		if file[pos1:pos2] == '+0' or file[pos1:pos2] == '+00':
			cost = 50000
			counter2 += 10
			str_counter2 = str(counter2)
			str_counter2 = '0' + str_counter2 if len(str_counter2) == 3 else str_counter2
			str_counter2 = '00' + str_counter2 if len(str_counter2) == 2 else str_counter2
			frame_rate = file[:pos1].split('_')[2]
			scale = '1.0'
			relevant = file[:pos1]
			outfitname = 'chromatic ' + relevant + ' ' + scale
			original_path = 'effect/newcolors/' + relevant
			outfitter_texts.append('\t"' + outfitname + '"\n')
			displayname = 'FP' + str_counter2 + ' size: ' + scale
			thumbnail = 'effect/newflares/newcolors ' + relevant + ' chromatic'
			flarestat = '\t"flare sprite" "' + 'effect/newcolors/' + relevant + '"\n' +\
				'\t\t"frame rate" ' + frame_rate + '\n' +\
				'\t\t"scale" ' + scale + '\n'
			outfit_text = outfit_text_template
			outfit_text = outfit_text.replace('%outfitname%', outfitname).replace('%displayname%', displayname).replace('%cost%', str(int(cost*float(scale))))
			outfit_text = outfit_text.replace('%thumbnail%', thumbnail).replace('%flarestats%', flarestat).replace('%index%', '99100')
			outfit_text = outfit_text.replace('%original%', original_path.replace('effect/', '').replace('/', ' ').replace('_', ' ') +\
				' sc:' + scale + '/fr:' + frame_rate)
			outfit_texts.append(outfit_text)
			# double size outfit
			counter2 += 10
			str_counter2 = str(counter2)
			str_counter2 = '0' + str_counter2 if len(str_counter2) == 3 else str_counter2
			str_counter2 = '00' + str_counter2 if len(str_counter2) == 2 else str_counter2
			scale = '2.0'
			outfitname = 'chromatic ' + file[:pos1] + ' ' + scale
			original_path = 'effect/newcolors/' + relevant
			outfitter_texts.append('\t"' + outfitname + '"\n')
			displayname = 'FP' + str_counter2 + ' size: ' + scale
			flarestat = flarestat.replace('1.0', scale)
			outfit_text = outfit_text_template
			outfit_text = outfit_text.replace('%outfitname%', outfitname).replace('%displayname%', displayname).replace('%cost%', str(int(cost*float(scale))))
			outfit_text = outfit_text.replace('%thumbnail%', thumbnail).replace('%flarestats%', flarestat).replace('%index%', '99100')
			outfit_text = outfit_text.replace('%original%', original_path.replace('effect/', '').replace('/', ' ').replace('_', ' ') +\
				' sc:' + scale + '/fr:' + frame_rate)
			outfit_texts.append(outfit_text)
			original_paths.append(original_path)
			effect_types.append('chromatic')
	# write to file
	print('WRITING DATA')
	with open('data' + os.sep + 'flare.play.outfits.txt', 'w') as target:
		target.writelines(outfitter_text)
		for outfitter_text in outfitter_texts:
			target.writelines(outfitter_text)
		for outfit_text in outfit_texts:
			counter += 10
			str_counter = str(counter)
			str_counter = '0' + str_counter if len(str_counter) == 3 else str_counter
			str_counter = '00' + str_counter if len(str_counter) == 2 else str_counter
			target.writelines(outfit_text.replace('%counter%', str_counter))
	return original_paths, effect_types


def createimages(path, flarenames, flaretypes):
	print('CREATING THUMBNAIL IMAGES')
	count = 0
	for each in flarenames: 
		flaretype = flaretypes[count]
		if flaretype == 'chromatic':
			new_path = 'images' + os.sep
		else:
			new_path = path
		flarename = each
		count += 1
		print('\tCREATING FILE ' + str(count) + ' ' + flarename + '+.png')
		# find out filename
		found = True
		if os.path.isfile(new_path + each.replace('/', os.sep) + '+01.png'):
			filename = '+01.png'
		elif os.path.isfile(new_path + each.replace('/', os.sep) + '+00.png'):
			filename = '+00.png'
		elif os.path.isfile(new_path + each.replace('/', os.sep) + '+0.png'):
			filename = '+0.png'
		elif os.path.isfile(new_path + each.replace('/', os.sep) + '^0.png'):
			filename = '^0.png'
		elif os.path.isfile(new_path + each.replace('/', os.sep) + '+.png'):
			filename = '+.png'
		else:
			print(new_path + each + ' NOT FOUND!')
			found = False
		if found == True:
			# open images
			outfitimagesize = (180,180) # possible to change to 360,360 to make the flares in the thumbnail smaller
			im = Image.open(new_path + each + filename).convert('RGBA') # flare
			bg = Image.new(mode='RGBA', size=outfitimagesize, color=(0,0,0,0)) # black background
			# title image
			if flaretype == 'afterburner':
				font = Image.open('logo_afterburner.png').convert('RGBA')
			elif flaretype == 'flare':
				font = Image.open('logo_flare.png').convert('RGBA')
			elif flaretype == 'reverse':
				font = Image.open('logo_reverse.png').convert('RGBA')
			elif flaretype == 'steering':
				font = Image.open('logo_steering.png').convert('RGBA')
			elif flaretype == 'chromatic':
				font = Image.open('logo_chromatic.png').convert('RGBA')
			# resize if it is too big
			if outfitimagesize == 360:
				fontposv = 50
			else:
				fontposv = 25
				font = font.resize(((180,35)))
			width, height = im.size
			maxflareheight = outfitimagesize[1]
			ratio = width / height
			if height > maxflareheight:
				width = maxflareheight * ratio
				height = maxflareheight
				im = im.resize((int(width), int(height)))
			# paste image and fontimage to the background
			pos1 = outfitimagesize[1] / 2 - width / 2
			pos2 = outfitimagesize[1] / 2 - height / 2
			bg.paste(im, (int(pos1), int(pos2)))
			bg.paste(font, (0, fontposv))
			flarename = 'images' + os.sep + 'effect' + os.sep + 'newflares' + os.sep + flarename.replace('effect' + os.sep, '').replace(os.sep, ' ')  + ' ' + flaretype
			# resize both, in case outfitimagesize got changed
			bg = bg.resize(((180,180)))
			bg.save(flarename + '+.png')
			bg = bg.resize(((360,360)))
			bg.save(flarename + '+@2x.png')
	print('\tDONE')


def run():
	path = '/storage/9C33-6BBD/endless sky/' # change to your ES directory (which should contain data and images)
	obj, obj_path, obj_name = get_ES_data(path + 'data/')
	flare_effect_scripts, flare_effects = find_flares(obj)
	original_paths, effect_types = writetxtfile(flare_effect_scripts, flare_effects)
	print('CREATE NEW THUMBNAIL IMAGES? y/n')
	choice = input()
	if choice == 'y':
		createimages(path + 'images/', original_paths, effect_types)
		
		


if __name__ == '__main__':
	run()