
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
		'Korath Exiles', 'Kor Efret', 'Kor Mereti', 'Kor Sestor', 'Wanderer', 'Bunrodea', 'Gegno', 'Gegno Scin', 'Gegno Vi'] # show these governments in the map legend
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
		elif line.startswith('system'):
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
			gov = line.strip().replace('government "', '')[:-1]
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


'''
def line_points(m, b, x_range):
    """
    Args:
    m (float): Steigung der Linie.
    b (float): y-Achsenabschnitt der Linie.
    x_range (tuple): Ein Tupel mit dem Start- und Endwert von x (start, end).
    
    Returns:
    list of tuples: Eine Liste von Punkten (x, y) auf der Linie.
    """
    x_values = np.linspace(x_range[0], x_range[1], num=100)  # 100 Punkte in der x-Range
    points = [(x, m*x + b) for x in x_values]
    return points
# Beispielaufruf der Funktion
m = 2  # Steigung
b = 1  # y-Achsenabschnitt
x_range = (0, 10)  # Bereich für x-Werte
punkte = line_points(m, b, x_range)
print(punkte)

def line_points2(start, end, num_points=100):
    """
    Args:
    start (tuple): Ein Tupel (x1, y1) für den Startpunkt.
    end (tuple): Ein Tupel (x2, y2) für den Zielpunkt.
    num_points (int): Anzahl der Punkte auf der Linie. Standard ist 100.
    Returns:
    list of tuples: Eine Liste von Punkten (x, y) auf der Linie.
    """
    x1, y1 = start
    x2, y2 = end
    if x1 == x2:
        # Vertikale Linie: y-Werte gleichmäßig zwischen y1 und y2 verteilen
        y_values = np.linspace(y1, y2, num=num_points)
        points = [(x1, y) for y in y_values]
    else:
        # Berechnung der Steigung und des y-Achsenabschnitts
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        # Erzeuge x-Werte gleichmäßig verteilt zwischen x1 und x2
        x_values = np.linspace(x1, x2, num=num_points)
        points = [(x, m * x + b) for x in x_values]
    return points

def line_length(start, end):
    """
    Args:
    start (tuple): Ein Tupel (x1, y1) für den Startpunkt.
    end (tuple): Ein Tupel (x2, y2) für den Zielpunkt.
    Returns:
    float: Die Länge der Linie.
    """
    x1, y1 = start
    x2, y2 = end
    # Berechnung der Länge mit dem Satz des Pythagoras
    length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 
    return length'''

					
def createImage():
	print('creating image')
	im = Image.open(backgroundImage + 'ui/milky way.jpg', 'r')
	draw = ImageDraw.Draw(im, 'RGBA')
	print('  drawing links')
	for each in systemNames:
		sysIndex = systemNames.index(each)
		links = systemLinks[sysIndex].split('|')
		for link in links:
			if link != ' ':
				# drawing system link
				targetIndex = systemNames.index(link)
				#x, y = xiaoline(systemPosX[sysIndex], systemPosY[sysIndex], systemPosX[targetIndex], systemPosY[targetIndex])
				#draw.line(x[6], y[6], x[len(x)-6], y[len(y)-6], fill=(128,128,128))
				draw.line((systemPosX[sysIndex], systemPosY[sysIndex], systemPosX[targetIndex], systemPosY[targetIndex]), fill=(128,128,128))
		for link in wormholes:
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
					draw.line((systemPosX[sysIndex], systemPosY[sysIndex], systemPosX[targetIndex], systemPosY[targetIndex]), fill=(204,0,204))
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
	bottom = 3096 # -1000
	im = im.crop((left, top, right, bottom))
	# save now
	im = im.convert('RGB')
	print('  saving image')
	im.save("pillow.jpg")
	print('DONE')

setVar()
readSystems()
readPlanets()
readWormholes()
readColors()
createImage()
