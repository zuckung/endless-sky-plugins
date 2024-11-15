import sys
import os
import glob
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import math


def setVar():
	global dataFolder
	global backgroundImage
	global iFont
	global wormBlacklist
	global legend
	global systemNames
	global systemPosX
	global systemPosY
	global systemFactions
	global systemLinks
	global wormholes
	global systemPlanets
	global planets
	global inhabited
	global governments
	global govColor
	dataFolder = '/storage/9C33-6BBD/endless sky/data/' # change to your data folder
	backgroundImage = '/storage/9C33-6BBD/endless sky/images/' # change to your images folder
	iFont = '/system/fonts/Roboto-Regular.ttf' # causes error if it doesnt exist, change to your choice
	wormBlacklist = ['Over the Rainbow'] # dont draw these links
	legend = ['Republic', 'Syndicate', 'Pirate', 'Remnant', 'Hai', 'Hai (Unfettered)', 'Quarg', 'Pug', 'Coalition', 'Heliarch', 
		'Korath Exiles', 'Kor Efret', 'Kor Mereti', 'Kor Sestor', 'Wanderer', 'Bunrodea', 'Gegno', 'Gegno Scin', 'Gegno Vi', 'Successor'] # show these governments in the map legend
	systemNames = []
	systemPosX = []
	systemPosY = []
	systemFactions = []
	systemLinks = []
	wormholes = []
	systemPlanets = []
	planets = []
	inhabited = []
	governments = []
	govColor = []


def convertCoordinates(pos):  # 4096 x 4096, center at 2048, 2048 sagitarius a, which is  112 22
	poss = pos.split(' ')
	new_posx = float(poss[0]) + 1936
	new_posy = float(poss[1]) + 2026
	return int(new_posx), int(new_posy)


def readSystems():
	print('reading systems')
	started = False
	startedLink = False
	planet = ''
	with open(dataFolder + 'map systems.txt') as file1:
		allSys = file1.readlines()
	for line in allSys:
		if line == '\n':
			if started == True:
				systemPlanets.append(planet)
				planet = ''					
				if startedLink == True:
					systemLinks.append(links[:-1])
					startedLink = False
				elif startedLink == False:
					systemLinks.append(' ')
				started = False
				if factionsadded == False:
					systemFactions.append('Uninhabited') # new
		elif line.startswith('system'):
			factionsadded = False
			line = line.replace('\n', '').replace('system ', '').replace('"', '')
			systemNames.append(line)
			started = True
			startedLink = False
		elif line.startswith('\tpos'):
			if started == True:
				line = line.replace('\n', '').replace('pos ', '').replace('\t', '')
				x, y = convertCoordinates(line)
				systemPosX.append(x)
				systemPosY.append(y)
		elif line.startswith('\tgovernment'):
			line = line.replace('\n', '').replace('government ', '').replace('\t', '').replace('"', '')
			systemFactions.append(line)
			factionsadded = True
		elif line.startswith('\tlink'):
			line = line.replace('\n', '').replace('link ', '').replace('\t', '').replace('"', '')
			if startedLink == False:
				links = line + '|'
				startedLink = True
			elif startedLink == True:
				links += line + '|'
		elif line.startswith('\tobject ') or line.startswith('\t\tobject '):
			if planet == '':
				planet += line.strip().replace('object ', '').replace('"', '')
			else:
				planet += '|' + line.strip().replace('object ', '').replace('"', '')
	systemPlanets.append(planet)
	systemLinks.append(links[:-1])
	print('  ' + str(len(systemNames)) + ' systems found')


def readPlanets():
	print('reading planets')
	with open(dataFolder + 'map planets.txt') as file1:
		all = file1.readlines()
	started = False
	port = False
	for line in all:
		if line == '\n':
			if started == True:
				if port == True:
					inhabited.append('spaceport')
					port = False
				else:
					inhabited.append('')
				started = False
		elif line.startswith('planet '):
			planets.append(line.strip().replace('planet ','').replace('"',''))
			started = True
		elif line.startswith('\tspaceport'):
			port = True
	if port == True:
		inhabited.append('spaceport')
	else:
		inhabited.append('')
	print('  ' + str(len(planets)) + ' planets found')


def readWormholes():
	print('reading wormholes')
	with open(dataFolder + 'map planets.txt') as file1:
		all = file1.readlines()
	startedWorm = False
	for line in all:
		if line == '\n':
			if startedWorm == True:
				startedWorm = False
		elif line.startswith('wormhole '):
			startedWorm = True
		elif line.startswith('\tlink'): # these links get saved
			if startedWorm == True:
				line = line.strip().replace('link ', '')
				if line.find('"') != -1:
					if line.startswith('"'): # link from
						x = line.find('"', 1)
						first = line[1:x]
						line = line[x+2:]
					else: # no "
						pos = line.find(' ')
						first = line[:pos]
						line = line[pos + 1:]
					if line.startswith('"'): # link to
						x = line.find('"', 1)
						second = line[1:x]
					else: # no "
						second = line
					wormholes.append(first +'|' + second)
				else:
					first = line.split(' ')[0]
					second = line.split(' ')[1]
					wormholes.append(first +'|' + second)				
	print('  ' + str(len(wormholes)) + ' wormhole links found')


def readColors(): # get colors for all factions
	print('reading colors')
	with open(dataFolder + 'governments.txt') as file1:
		all = file1.readlines()
	govColorTemp = []
	for line in all:
		if line.startswith('color '): # first adding the main governments & colors
			line = line.strip().replace('color "governments: ', '')
			splitted = line.split('"')
			governments.append(splitted[0])
			govColorTemp.append(splitted[1][1:])
	gov = ''
	color = ''
	for line in all: # getting all other governments & colors
		if line =='\n':
			if color != '':
				if gov != '':
					governments.append(gov)
					govColorTemp.append(color)
					gov = ''
					color = ''
		if line.startswith('government '): # gets gov, if not allready in list
			gov = line.strip().replace('government ', '').replace('"', '')
			if gov in governments:
				gov = ''
		elif line.startswith('\tcolor "gov'): # link to color difinition of parent government
			govLink =  line.strip().replace('color "governments: ', '')[:-1]
			if govLink in governments:
				gIndex = governments.index(govLink)
				color = govColorTemp[gIndex]
		elif line.startswith('\tcolor '): # gets real color
			color = line.strip().replace('color ', '')
	for each in govColorTemp:
		govColor.append(colorConvert(each))
	print('  ' + str(len(governments)) + ' government colors found')


def colorConvert(colInput): # format from rgb 1 to: rgb(255,255,255)
	splitted = colInput.split(' ')
	r = float(splitted[0]) * 255
	r = int(r)
	g = float(splitted[1]) * 255
	g = int(g)
	b = float(splitted[2]) * 255
	b = int(b)
	color = 'rgb(' + str(r) + ',' + str(g) + ',' + str(b) +')'
	return color
	

def getColor(faction): # input government > output rgb color
	if faction in governments:
		gIndex = governments.index(faction)
		color = govColor[gIndex]
		return color


def line_points(start, end, num_points): # start (tuple): l(x1, y1) startpoint, end (tuple): (x2, y2) endpoint, num_points (int): amount of pixels to show on the line
	x1, y1 = start
	x2, y2 = end
	if x1 == x2:
		# distribute the pixels on the line
		y_values = np.linspace(y1, y2, num=num_points)
		points = [(x1, y) for y in y_values]
	else:
		# calculate the rising of the line
		m = (y2 - y1) / (x2 - x1)
		b = y1 - m * x1
		# distribute the pixels on the line
		x_values = np.linspace(x1, x2, num=num_points)
		points = [(x, m * x + b) for x in x_values]
	return points # list of pixel on the line (x, y)


def line_length(start, end): # start (tuple): l(x1, y1) startpoint, end (tuple): (x2, y2) endpoint
	x1, y1 = start
	x2, y2 = end
	length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 
	return int(length) # was float line length


def draw_arrow(x0, y0, x1, y1):
	# Now we can work out the x,y coordinates of the bottom of the arrowhead triangle
	xb = 0.95*(x1-x0)+x0
	yb = 0.95*(y1-y0)+y0
	# Work out the other two vertices of the triangle
	# Check if line is vertical
	if x0==x1:
		vtx0 = (xb-5, yb)
		vtx1 = (xb+5, yb)
	# Check if line is horizontal
	elif y0==y1:
		vtx0 = (xb, yb+5)
		vtx1 = (xb, yb-5)
	else:
		alpha = math.atan2(y1-y0,x1-x0)-90*math.pi/180
		a = 4*math.cos(alpha)
		b = 4*math.sin(alpha)
		vtx0 = (xb+a, yb+b)
		vtx1 = (xb-a, yb-b)
	return vtx0, vtx1

								
def createImage():
	print('creating image')
	im = Image.open(backgroundImage + 'ui' + os.sep + 'milky way.jpg', 'r')
	draw = ImageDraw.Draw(im, 'RGBA')
	print('  drawing links')
	for each in systemNames:
		sysIndex = systemNames.index(each)
		links = systemLinks[sysIndex].split('|')
		for link in links:
			if link != ' ':
				# drawing system link
				targetIndex = systemNames.index(link)
				# remove some pixels to not overlap the system circles
				start = (systemPosX[sysIndex], systemPosY[sysIndex]) 
				end = (systemPosX[targetIndex], systemPosY[targetIndex])
				linelength = line_length(start, end)
				linepoints = line_points(start, end, int(linelength))
				points = len(linepoints)
				start = linepoints[5]
				end = linepoints[len(linepoints) - 6]
				draw.line((start, end), fill=(128,128,128))
		for link in wormholes:
			# drawing wormhole link
			first = link.split('|')[0]
			if each == first:
				second = link.split('|')[1]
				blacklisted = False
				for black in wormBlacklist:
					if black == second or black == first:
						blacklisted = True
				if blacklisted == False:
					# drawing purple wormhole line
					targetIndex = systemNames.index(second)
					# remove some pixels to not overlap the system circles
					start = (systemPosX[sysIndex], systemPosY[sysIndex]) 
					end = (systemPosX[targetIndex], systemPosY[targetIndex])
					linelength = line_length(start, end)
					linepoints = line_points(start, end, int(linelength))
					points = len(linepoints)
					start = linepoints[5]
					end = linepoints[len(linepoints) - 6]
					draw.line((start, end), fill=(204,0,204))
					# create arrows
					x0, y0 = linepoints[len(linepoints)-20]
					x1, y1 = linepoints[len(linepoints)-30]
					vtx0, vtx1 = draw_arrow(x0, y0, x1, y1)
					draw.polygon([vtx0, vtx1, linepoints[len(linepoints) - 20]], fill=(204,0,204))				
	print('  drawing systems')
	for each in systemNames:
		inhab = False
		sysIndex = systemNames.index(each)
		# drawing colored system dots
		if systemPlanets[sysIndex] == '': # gray, nothing landable here
			inhab = False
		else : # landable planets found
			if systemPlanets[sysIndex].find('|'):
				planetlist = systemPlanets[sysIndex].split('|')
			else:
				planetlist = [systemPlanets[sysIndex]]
			for each in planetlist:
				if each in planets:
					pIndex = planets.index(each)
					if inhabited[pIndex] == 'spaceport':
						inhab = True
		if inhab == True: # inhabited! color this system			
			draw.ellipse((systemPosX[sysIndex]-7, systemPosY[sysIndex]-7, systemPosX[sysIndex]+7, 
				systemPosY[sysIndex]+7), fill=(0,0,0,0), outline=(getColor(systemFactions[sysIndex])), width=3)
		else: # color system gray
			draw.ellipse((systemPosX[sysIndex]-7, systemPosY[sysIndex]-7, systemPosX[sysIndex]+7, 
				systemPosY[sysIndex]+7), fill=(0,0,0,0), outline=(102,102,102), width=3)
		font = ImageFont.truetype(font=iFont, size=12)
		draw.text((systemPosX[sysIndex]+12, systemPosY[sysIndex]-5) , systemNames[sysIndex], fill=(255,255,255), font=font)
	#drawing legend
	print('  drawing legend')
	font = ImageFont.truetype(font=iFont, size=20)
	startX = 3400
	startY = 2400
	for each in legend:
		draw.ellipse((startX-7, startY-7, startX+7, startY+7), fill=(0,0,0,0), outline=(getColor(each)), width=3)
		draw.text((startX+15, startY-14) , each, fill=(255,255,255), font=font)
		startY += 25
	# crop image
	print('  cropping image')
	left = 200 # - 200
	top = 800 # - 800
	right = 3596 # -500
	bottom = 4096 # -0
	im = im.crop((left, top, right, bottom))
	# save now
	im = im.convert('RGB')
	print('  saving image')
	im.save("pillow.jpg")
	print('DONE')


def run():
	setVar()
	readSystems()
	readPlanets()
	readWormholes()
	readColors()
	createImage()


if __name__ == "__main__":
	run()