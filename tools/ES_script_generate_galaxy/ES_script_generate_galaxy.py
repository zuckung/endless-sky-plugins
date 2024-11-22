import os
import sys
import math
import random
import re
from PIL import Image, ImageDraw, ImageFont


# 2do
# hang up @ > 624 landable planets, omg why?!
# find out why backlinks get added twice (fixed in rearrange_systemtext), fix it earlier


def setup():
	# setting variables
	global startPos, systemAmount, starRadius, startWormhole, landPlanets, density, tries, dataFolder
	global imageFolder, galaxyImage, starNames, planetNames, landImages, starTypes, planetTypes
	global usedStarnames
	usedStarnames = []
	
	# currently 521 star system names and 639 planet names  in wordlist (bug at landPlanets > 624?)
	###### start of config | modify the following variables
	startPos = -7000, -7000 # position of the first system
	systemAmount = 300 # star systems amount
	startWormhole = 'Sol' # empty for deactivated | vanilla system name for link: firstsystem-vanillasystem
	landPlanets = 100 # number of landable planets
	dataFolder = '/storage/9C33-6BBD/endless sky/data/' # folder to the ES data (for reading star types)
	imageFolder = '/storage/9C33-6BBD/endless sky/images/' # folder to the ES images (for reading planet sprites)
	galaxyImage = 'sculptor' # copy to plugin/images/ui/sculptor.jpg
	###### experimental (no need to change)
	starRadius = 100 # distance from system to system
	density = 5 # (default 5) after how many system creations the script tries to restart at the prior systems(higher means more dead system arm ends)
	tries = 15 # (default 15) how many pos generations tried on every system, before skipping (also control density, higher means denser)
	###### end of config
	
	#get starNames & planetNames
	with open('nameStars.txt', 'r') as source:
		starNames = source.readlines()
	with open('namePlanets.txt', 'r') as source:
		planetNames = source.readlines()
	# check if global variables are ok
	check_parameter()
	# get starTypes from ES datafolder
	invalid_stars = ['a-eater']
	with open(os.path.join(dataFolder, 'stars.txt'), 'r') as source:
		starTypes = [line.removeprefix('star ').strip() for line in source if line.startswith('star ') and line.replace('"', '').replace('star/', '')\
		.replace('star ', '') not in invalid_stars] #: "star/o3"
	# get planet sprites from ES imagefolder
	invalid_planets = ('alvorada', 'asura', 'dyson', 'gas3-c', 'gas7-r', 'mendez', 'panels', 'pontes', 'ringworld', 'sheragi', 'station', 'tschyss', 'wormhole', )
	planetTypes = [file[:-4] for file in os.listdir(os.path.join(imageFolder, 'planet')) if not file.startswith(invalid_planets)] #: lava-7b
	# get landing images
	invalid_land = ('badlands12','beach0', 'bwerner0', 'city', 'desert9-sfiera', 'earthrise', 'fields', 'garden1', 'industrial0', 'loc',\
	'mfield', 'mountain14', 'nasa1', 'nasa2','nasa3','nasa4','nasa5','nasa6','nasa7', 'path', 'sea6', 'sea11', 'sea12', 'sea14', 'sea18',\
	'sea20', 'sea24', 'sivael', 'snow15', 'space', 'station', 'valley1', 'valley6', 'water14', 'water16', 'water17', 'water18', 'water20', 'water24')
	landImages = [file[:-4] for file in os.listdir(os.path.join(imageFolder, 'land')) if not file.startswith(invalid_land)] #: mountain8
	# create folder for generated files
	if not os.path.isdir('generated'):
		os.mkdir('generated')
	# show
	print('conditions:')
	print('	startpos of first system: ', startPos)
	print('	amount of systems: ', systemAmount)
	print('	landable planets: ', landPlanets)
	print('	starNames in wordlist: ', len(starNames))
	print('	planetNames in wordlist: ', len(planetNames))
	if startWormhole != '':
		print('	vanilla start wormhole: ', startWormhole)
	print('	dataFolder: ', dataFolder)
	print('	imageFolder: ', imageFolder)
	print('	galaxyImage: ', galaxyImage)
	print('	distance from system to system: ', starRadius)
	print('	star density: ', density)
	print('	setting system retries: ', tries)


def check_parameter():
	# check for correct parameter, else exit script
	if not os.path.isdir(dataFolder):
		print('error: dataFolder not found!')
		sys.exit(1)
	if not os.path.isdir(imageFolder):
		print('error: imageFolder not found!')
		sys.exit(1)
	if not os.path.isfile(galaxyImage + '.jpg'):
		print('error: galaxyImage not found!')
		sys.exit(1)
	if systemAmount > len(starNames):
		print('error: systemAmount is higher than the wordlist!')
		sys.exit(1)
	if landPlanets > len(planetNames):
		print('error: landPlanets is higher than the wordlist!')
		sys.exit(1)
		

def write_other_stuff():
	with open('generated' + os.sep + 'MapGenStuff.txt', 'w') as target:
		# writing startWormhole script
		if startWormhole != '':
			target.writelines('system "' + startWormhole + '"\n\tadd object "Mysterious Wormhole"\n\t\tsprite planet/wormhole-red\n\t\tdistance 1000\n\t\tperiod 1\n\n')
			target.writelines('wormhole "Mysterious Wormhole"\n\tlink "' + startWormhole + '" "Alcor"\n\tlink "Alcor" "' + startWormhole + '"\n\n')
			target.writelines('planet "Mysterious Wormhole"\n\tspaceport ``\n\tgovernment "Republic"\n\twormhole "Mysterious Wormhole"\n\n')
		# writing galaxy image script
		target.writelines('galaxy "' + galaxyImage + '"\n\tpos ' + str(startPos[0]) + ' ' + str(startPos[1]) + '\n\tsprite "ui/' + galaxyImage + '"\n\n')


def create_systemtexts():
	def get_system_text(x, y, firstWorm):
		# create the script text for a system
		def get_starsprite():
			starsprite = random.choice(starTypes)
			if os.path.isfile(imageFolder + starsprite.replace('"', '').replace('/', os.sep) +'.png'):
				im = Image.open(imageFolder + starsprite.replace('"', '').replace('/', os.sep) +'.png')
			elif os.path.isfile(imageFolder + starsprite.replace('"', '').replace('/', os.sep) +'+.png'):
				im = Image.open(imageFolder + starsprite.replace('"', '').replace('/', os.sep) +'+.png')
			elif os.path.isfile(imageFolder + starsprite.replace('"', '').replace('/', os.sep) +'.jpg'):
				im = Image.open(imageFolder + starsprite.replace('"', '').replace('/', os.sep) +'.jpg')
			elif os.path.isfile(imageFolder + starsprite.replace('"', '').replace('/', os.sep) +'+.jpg'):
				im = Image.open(imageFolder + starsprite.replace('"', '').replace('/', os.sep) +'+.jpg')
			width, height = im.size
			return starsprite, width
		# check for name, prevent multiple use, message if no names available
		if firstWorm != '':
			name = 'Alcor'
		else:
			name = str(random.choice(starNames)).replace('\n', '')
		while name in usedStarnames:
			name = str(random.choice(starNames)).replace('\n', '')
		usedStarnames.append(name)
		# get minables
		minables = ['aluminum', 'copper', 'gold', 'iron', 'lead', 'neodymium', 'platinum', 'silicon', 'silver', 'titanium', 'tungsten', 'uranium']
		minablesstring = ''
		for i in range(0, random.randint(1,3)):
			minablesstring = minablesstring + '\tminables '+ random.choice(minables) + ' ' + str(random.randint(6,25)) + ' ' + str(random.randint(3,12)) +\
			 '\n' #: minables lead 24 9
		# get objects
		objectsstring = ''
		# stars
		staramount = random.randint(1,3) #add 1 to 3 stars
		for i in range(1, staramount+1):
			if staramount == 1:
				starsprite = random.choice(starTypes)
				objectsstring = objectsstring + '\tobject\n\t\tsprite ' + starsprite + '\n' + '\t\tperiod ' + str(random.randint(10,15)) + '\n'
			elif staramount == 2:
				if i ==1:
					starsprite, width = get_starsprite()
					objectsstring = objectsstring + '\tobject\n\t\tsprite ' + starsprite + '\n' + '\t\tdistance ' + str(random.randint(width,width + 100))\
					+ '\n\t\tperiod ' + str(random.randint(10,15)) +  '\n'
				else:
					starsprite, width = get_starsprite()
					objectsstring = objectsstring + '\tobject\n\t\tsprite ' + starsprite + '\n' + '\t\tdistance ' + str(random.randint(width,width + 100))\
					+ '\n\t\tperiod ' + str(random.randint(10,15)) + '\n\t\toffset 180\n'
			elif staramount == 3:
				if i ==1:
					starsprite, width = get_starsprite()
					objectsstring = objectsstring + '\tobject\n\t\tsprite ' + starsprite + '\n' + '\t\tdistance ' + str(random.randint(width,width + 100))\
					+ '\n\t\tperiod ' + str(random.randint(10,15)) +  '\n'
				elif i ==2:
					starsprite, width = get_starsprite()
					objectsstring = objectsstring + '\tobject\n\t\tsprite ' + starsprite + '\n' + '\t\tdistance ' + str(random.randint(width,width + 100))\
					+ '\n\t\tperiod ' + str(random.randint(10,15)) + '\n\t\toffset 120\n'
				elif i ==3:
					starsprite, width = get_starsprite()
					objectsstring = objectsstring + '\tobject\n\t\tsprite ' + starsprite + '\n' + '\t\tdistance ' + str(random.randint(width,width + 100))\
					+ '\n\t\tperiod ' + str(random.randint(10,15)) + '\n\t\toffset 240\n'
		# planets
		planetamount = random.randint(2,5) # add 2 to 5 planets
		objectsstring = objectsstring + firstWorm # add wormhole, only first system gives content, else firstWorm is empty
		for i in range(1, planetamount+1):
			objectsstring = objectsstring + '\tobject\n\t\tsprite planet/' + random.choice(planetTypes)\
			+ '\n\t\tdistance ' + str(random.randint(600,4000)) + '\n\t\tperiod ' + str(random.randint(500,1500)) + '\n'
		# create the script now
		systemtext = 'system "' + name + '"\n'\
		+ '\tpos ' + str(x) + ' ' + str(y) + '\n'\
		+ '\tgovernment "Uninhabited"\n'\
		+ '\tarrival ' + str(random.randint(500,1200)) + '\n'\
		+ '\thabitable ' + str(random.randint(500,1200)) + '\n'\
		+ '\tbelt ' + str(random.randint(800,1800)) + '\n'\
		+ minablesstring\
		+ objectsstring
		# links get added at the bottom
		return systemtext, name
	def new_pos(center_x, center_y):
		# generates a new system pos, somewhere on the border of the circle
		theta = math.radians(random.randint(1,360))
		x = center_x + starRadius * math.cos(theta)
		y = center_y + starRadius * math.sin(theta)
		return int(x), int(y)
	systemtexts, positions = [], []
	print('\ncreating systems [', systemAmount, ']')
	count = 0 # for counting systems
	densitycounter = 0
	counter2 = 0 # for changing system
	for i in range(0, systemAmount):
		if i == 0: # only for the first system
			# start system
			if startWormhole != '':
				firstWorm = '\tobject "Mysterious Wormhole"\n\t\tsprite planet/wormhole-red\n\t\tdistance 1000\n\t\tperiod 1\n'
			else:
				firstWorm = ''
			x, y = 0, 0
			systemtext, name = get_system_text(x, y, firstWorm)
			systemtexts.append(systemtext)
			positions.append([x,y])
			count +=1
			print('	found new system position (' + str(count) + '): [' + str(x) + ' ' + str(y) + '] ' + name)
			firstWorm = ''
		else: # after starting system got added
			repeat = True
			counter = 0 # for pos generating
			#
			if densitycounter > density:
				densitycounter = 1
				oldx, oldy = 0, 0
			else:
				oldx, oldy = x, y # old system
			# get new system pos
			while repeat == True:
				if counter < tries: # if not {tries} failed pos generations
					x, y = new_pos(oldx, oldy) # generate from previous system
				else: # {tries} times failed, resets counter, and changes oldx,oldy to a previous system pos
					counter = 0
					if counter2 < len(positions)-1:
						counter2 += 1
					else:
						counter2 = 1
					oldx, oldy = positions[counter2-1]
					x, y = new_pos(oldx, oldy)
				for systempos in positions:
					fx, fy = systempos
					result = dot_in_circle(fx, fy, x, y, starRadius-1)
					if result == False:
						repeat = False
					else:
						counter += 1
						repeat = True
						break
			# new system pos found, generating text
			densitycounter +=1
			systemtext, name = get_system_text(x, y, firstWorm)
			systemtexts.append(systemtext)
			positions.append([x,y]) # finally new system added
			count +=1
			print('	found new system position (' + str(count) + '): [' + str(x) + ' ' + str(y) + '] ' + name)
	print('	DONE')
	return systemtexts, positions


def dot_in_circle(fx, fy, x, y, rad):
	# checks if the pos is inside the circle
	distance = math.sqrt((fx - x)**2 + (fy - y)**2)
	if distance <= rad:
		result = True
	else:
		result = False
	return result



def create_landable_planets(systemtexts):
	if landPlanets > 0:
		print('\ncreating landable planets [', landPlanets, ']')
		used_planetNames = []
		rare = systemAmount / landPlanets # float, number of planets in each system
		count = 0
		whole = 0
		with open('generated' + os.sep + 'MapGenPlanets.txt', 'w') as planettxt:
			for i in range(1, landPlanets + 1):
				# generate unique name
				name = str(random.choice(planetNames)).replace('\n', '')
				while name in used_planetNames:
					name = str(random.choice(planetNames)).replace('\n', '')
				used_planetNames.append(name)
				print('	planet:', i, '/', landPlanets, 'added to system:', whole+1,'planetname:', name)
				# planet creation planet file
				planettxt.writelines('planet "' + name + '"\n\tattributes uninhabited sculptor\n\tlandscape land/' + random.choice(landImages) + '\n\tdescription ``\n\n')
				# planet creation system object
				addObject = '\tobject "' + name + '"\n\t\tsprite planet/' + random.choice(planetTypes) + '\n' + '\t\tdistance ' + str(random.randint(600,2000))\
					+ '\n\t\tperiod ' + str(random.randint(300,1500)) + '\n'
				# choose systems
				count += rare
				while count >= whole+1:
					whole +=1
				systemtexts[whole-1] += addObject
		print('	DONE')
	return systemtexts


def create_links(systemtexts, positions):
	def get_link(index):
		# get linkname & name from coordinates
		linkindex = positions.index(index)
		linkname = systemtexts[linkindex][systemtexts[linkindex].find(' ')+1:systemtexts[linkindex].find('\n')].replace('"', '')
		link = '\tlink "' + linkname + '"\n'
		return link, linkname
	def other_system(source, linkname):
		# writes back link to the linked system
		for system in systemtexts:
			if system.startswith('system "' + linkname + '"\n'):
				index = systemtexts.index(system)
				break
		if f'\tlink "{source}"\n' not in systemtexts2[index]:
			systemtexts2[index] += f'\tlink "{source}"\n'
	global systemtexts2
	systemtexts2 = systemtexts.copy()
	# create system links
	print('\ncreate system links')
	for system in systemtexts:
		links = ''
		index = systemtexts.index(system)
		x, y = positions[index]
		name = system[system.find(' ')+1:system.find('\n')].replace('"', '')
		# get nearest systems
		nearsys = [] # list of position of systems within the radius circle
		for position in positions:
			if position == positions[index]:
				continue
			fx, fy = position
			if dot_in_circle(fx, fy, x, y, starRadius+50) == True:
				nearsys.append(position)
		# add links
		if len(nearsys) == 1:
			for i in range(0,1):
				link, linkname = get_link(nearsys[i]) # \t link "name"\n | name
				links = links + link
				other_system(name, linkname)
		elif len(nearsys) == 2:
			for i in range(0,2):
				link, linkname = get_link(nearsys[i])
				links = links + link
				other_system(name, linkname)
		else:
			for i in range(0,random.randint(2, 3)):
				link, linkname = get_link(nearsys[i])
				links = links + link
				other_system(name, linkname)
		systemtexts2[index] = systemtexts2[index] + links
	print('	DONE')
	systemtexts = systemtexts2.copy()
	return systemtexts


def rearrange_systemtexts(systemtexts):
	# re-arranging links
	print('\nre-arranging system scripts')
	systemtexts2 = systemtexts.copy()
	# save the first part, the objects and the links into lists
	for system in systemtexts:
		first_part = [] # text till objects start
		objectlines = [] # text till links start
		links = [] # links
		startblock = True
		objectblock = True
		splitted = system.split('\n')
		for line in splitted:
			if startblock == True:
				if not line.startswith('\tobject'):
					first_part.append(line)
				else:
					objectlines.append(line)
					startblock = False
			else:
				if objectblock == True:
					if not line.startswith('\tlink'):
						objectlines.append(line)
					else:
						links.append(line)
						objectblock = False
				else:
					if not line in links: # corrects an error i can't find in create_links(), showing backlinks doubled
						links.append(line)
		# separate objects
		start = True
		objects = []
		for line in objectlines:
			if line.startswith('\tobject'):
				if start == True:
					text = line + '\n'
					start = False
				else:
					objects.append(text)
					text = line + '\n'
			elif line.startswith('\t\t'):
				text += line + '\n'
		objects.append(text)
		# get new list with distances
		distance = []
		for obj in objects:
			if not '\tdistance ' in obj:
				distance.append(0)
			else:
				pos1 = obj.find('\tdistance')
				pos2 = obj.find('\n', pos1)
				distance.append(int(obj[pos1+10:pos2]))
		# sort both lists
		distance, objects = zip(*sorted(zip(distance, objects)))
		objtext = ''
		for obj in objects:
			objtext += obj
		# lists are created
		final_text = '\n'.join(first_part) + '\n' + '\n'.join(links) + objtext
		index = systemtexts2.index(system)
		systemtexts2[index] = final_text
		systemtexts = systemtexts2.copy()
	print('	DONE')
	return systemtexts


def write_map_file(systemtexts):
	print('\nwriting map file')
	addx, addy = startPos
	# correct pos with startpos
	with open('generated' + os.sep + 'MapGenSystems.txt', 'w') as mapfile:
		print('	correcting pos with startpos')
		for text in systemtexts:			
			pos1 = text.find('\tpos ')
			pos2 = text.find('\n', pos1)
			splitted = text[pos1+5:pos2].split(' ')
			x = int(splitted[0])
			y = int(splitted[1])
			text = text.replace(text[pos1+5:pos2], str(x + addx) + ' ' + str(y + addy))
			# write to mapfile
			mapfile.writelines(text + '\n')
	print('	DONE')


def create_image(systemtexts, positions):
	# creating overview image, just to see result
	def findpos(text):
		pos1 = text.find('pos')
		pos2 = text.find('\n', pos1)
		x, y = text[pos1+4:pos2].split(' ')
		return int(x), int(y)
	print('\ncreating image')
	# analyzing positions to get right picture size
	print('	getting drawn image size')
	hx = max((x for x, _ in positions if x >= 0), default=0)
	lx = min((x for x, _ in positions if x < 0), default=0)
	hy = max((y for _, y in positions if y >= 0), default=0)
	ly = min((y for _, y in positions if y < 0), default=0)
	x = max(hx, -lx)
	y = max(hy, -ly)
	sizex = x*2 + 300
	sizey = y*2 + 300
	# define image
	iFont = '/system/fonts/Roboto-Regular.ttf'
	print('		drawn size will be:', sizex, sizey)
	#im = Image.open(mode = "RGB", size = (sizex, sizey), color=(10,10,10)) # black background, and cut to relevant parts
	im = Image.open(galaxyImage + '.jpg')
	width, height = im.size
	print('		background size will be:', width, height)
	draw = ImageDraw.Draw(im, 'RGBA')
	font = ImageFont.truetype(font=iFont, size=15)
	print('	drawing systems and links')
	for system in systemtexts:
		# get positions
		pos1 = system.find('system ')
		pos2 = system.find('\n')
		name = system[pos1+7:pos2]
		x, y = findpos(system)
		pos = [x +(width/2), y +(height/2)]
		# draw systems
		draw.ellipse((pos[0]-7, pos[1]-7, pos[0]+7, pos[1]+7), fill=(0,0,0,0), outline=(255,255,255), width=3)
		draw.text((pos[0]+15, pos[1]-14) , name.replace('"', ''), fill=(255,255,255), font=font)
		# draw link lines
		start = x +(width/2), y +(height/2)
		othersystem = []
		splitted = system.split('\n')
		for line in splitted:
			if line.startswith('\tlink '):
				pos1 = line.find('"')
				pos2 = line.find('"', pos1+1)
				linked = line[pos1+1:pos2]
				othersystem.append(linked) # system name
		for linked in othersystem:
			for checksystem in systemtexts:
				if checksystem.startswith('system "' + linked + '"'):
					x,y = findpos(checksystem)
					end = x +(width/2), y +(height/2)
					draw.line((start, end), fill=(128,128,128))
	# save image
	im = im.convert('RGB')
	print('	saving image')
	im.save('generated' + os.sep + 'MapGenMap.jpg')
	print('	DONE')


def run():
	setup() # setup variables and doing som checks
	write_other_stuff() # write generated/MapGenStuff.txt
	systemtexts, positions = create_systemtexts() # creates system scripts
	systemtexts = create_landable_planets(systemtexts) # updates system scripts with landable planets and writes generated/MapGenPlanets.txt
	systemtexts = create_links(systemtexts, positions) # updates system scripts with links
	systemtexts = rearrange_systemtexts(systemtexts) # puts objects and links of systems in the correct order
	write_map_file(systemtexts) # writes generated/MapGenSystems.txt
	create_image(systemtexts, positions) # creates generated/MapGenMap.jpg just for the overview


if __name__ == '__main__':
	run()