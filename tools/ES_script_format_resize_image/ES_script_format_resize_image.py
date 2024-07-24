from PIL import Image
import os
import sys


def set_var():
	global outputf
	global inputf
	global outputext
	global resx
	global resy
	global format
	outputf = './out/'
	inputf = './raw/'
	outputformat = 'land' # land, scene, icon, portrait, portrait@2x, outfit, outfit@2x
	if outputformat == 'land':
		resx = 720
		resy = 360
		format = "jpg"
	elif outputformat == 'scene':
		resx = 560
		resy = 340
		format = "jpg"
	elif outputformat == 'icon':
		resx = 150
		resy = 150
		format = "png"
	elif outputformat == 'portrait':
		resx = 120
		resy = 120
		format = "png"
	elif outputformat == 'portrait@2x':
		resx = 240
		resy = 240
		format = "png"
	elif outputformat == 'outfit':
		resx = 180
		resy = 180
		format = "png"
	elif outputformat == 'outfit':
		resx = 360
		resy = 360
		format = "png"

def resize():
	print("ES image converter/resizer")
	print("Converting all files in " + inputf + " to " + outputf)
	for file in os.listdir(inputf):
		with Image.open(inputf + file) as im:
			print("	Converting: " + inputf + file)
			width, height = im.size
			ratio = height / width
			resized = im.resize((resx, int(resx * ratio)), Image.LANCZOS)
			new_name = file.split(".")[0]
			resized.save(outputf + new_name + '.' + format)
			print("		Created: " + outputf + new_name)
	print("Done")


set_var()
resize()




