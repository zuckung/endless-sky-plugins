# copy "map sys5ems.txt" from endless sky data folder to the folder this script is in
# run this script
# the created file "pillow.jpg" is the result

import sys
import os
from PIL import Image, ImageDraw


def setVar():
	global systemsFile
	global systemNames
	global systemPosX
	global systemPosY
	global systemFactions
	global systemLinks
	global draw
	systemsFile = "map systems.txt"
	systemNames = []
	systemPosX = []
	systemPosY = []
	systemFactions = []
	systemLinks = []

def convert_coordinates(pos):  # 4096 x 4096 center 2048, 2048 sagitarius a, which is  112 22
	poss = pos.split(' ')
	new_posx = float(poss[0]) + 1936
	new_posy = float(poss[1]) + 2026
	return int(new_posx), int(new_posy)

def readSystems():
	print('reading systems')
	started = False
	startedLink = False
	wormhole = ''
	with open(systemsFile) as file1:
		allSys = file1.readlines()
	for line in allSys:
		if line == '\n':
			if started == True:
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
				x, y = convert_coordinates(line)
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
	systemLinks.append(links[:-1])
	print('  ' + str(len(systemNames)) + ' systems found')

def getColor(faction):
		if faction == 'Coalition':
			color = 'rgb(248,187,208)'
		elif faction == 'Heliarch':
			color = 'rgb(248,187,208)'
		elif faction == 'Syndicate':
			color = 'rgb(0,0,255)'
		elif faction == 'Uninhabited':
			color = 'rgb(96,96,96)'
		elif faction == 'Republic':
			color = 'rgb(153,75,0)'
		elif faction == 'Quarg':
			color = 'rgb(253,216,53)'
		elif faction == 'Quarg (Gegno)':
			color = 'rgb(253,216,53)'
		elif faction == 'Quarg (Kor Efret)':
			color = 'rgb(253,216,53)'
		elif faction == 'Quarg (Hai)':
			color = 'rgb(253,216,53)'
		elif faction == 'Pirate':
			color = 'rgb(255,0,0)'
		elif faction == 'Pirate (Devil-Run Gang)':
			color = 'rgb(255,0,0)'
		elif faction == 'Wanderer':
			color = 'rgb(212,225,87)'
		elif faction == 'Remnant':
			color = 'rgb(240,98,146)'
		elif faction == 'Kor Sestor':
			color = 'rgb(136,14,79)'
		elif faction == 'Kor Mereti':
			color = 'rgb(156,39,176)'
		elif faction == 'Kor Efret':
			color = 'rgb(186,104,200)'
		elif faction == 'Korath':
			color = 'rgb(230,81,0)'
		elif faction == 'Gegno':
			color = 'rgb(188,174,164)'
		elif faction == 'Gegno Vi':
			color = 'rgb(141,110,99)'
		elif faction == 'Gegno Scin':
			color = 'rgb(161,136,127)'
		elif faction == 'Hai':
			color = 'rgb(244,173,177)'
		elif faction == 'Hai (Unfettered)':
			color = 'rgb(103,58,183)'
		elif faction == 'Pug':
			color = 'rgb(215,204,200)'
		elif faction == 'Pug (Wanderer)':
			color = 'rgb(215,204,200)'
		elif faction == 'Bunrodea':
			color = 'rgb(76,175,80)'
		elif faction == 'Bunrodea (Guard)':
			color = 'rgb(76,175,80)'
		elif faction == 'Drak':
			color = 'rgb(253,216,53)'
		else:
			color = 'rgb(255,255,255)'
		return color
					
def createImage():
	print('creating image')
	#im = Image.new("RGB", (2800, 1800), (0, 0, 0))
	im = Image.open('milky way.jpg', 'r')
	draw = ImageDraw.Draw(im)
	print('  drawing links')
	for each in systemNames:
		sysIndex = systemNames.index(each)
		links = systemLinks[sysIndex].split('|')
		for link in links:
			if link != ' ':
				targetIndex = systemNames.index(link)
				draw.line((systemPosX[sysIndex], systemPosY[sysIndex], systemPosX[targetIndex], systemPosY[targetIndex]), fill=(255,255,255))
	print('  drawing systems')
	for each in systemNames:
		sysIndex = systemNames.index(each)
		draw.ellipse((systemPosX[sysIndex]-7, systemPosY[sysIndex]-7, systemPosX[sysIndex]+7, systemPosY[sysIndex]+7), fill=getColor(systemFactions[sysIndex]), outline=(0, 0, 0))
		draw.text((systemPosX[sysIndex]+12, systemPosY[sysIndex]-5) , systemNames[sysIndex], fill=(255,255,255))
	im = im.convert('RGB')
	print('  saving image')
	im.save("pillow.jpg")


setVar()
readSystems()
createImage()

