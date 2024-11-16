# change the sourcefile to your data folder with "map systems.txt".
# run this py-file.
# use the created asteroids.txt in your plugin.
# i.e. too.many.asteroids/data/asteroids.txt
# with this python script you will allways get an up-to-date plugin.


def remove_asteroids():
	systemcount = 0
	asteroidcount = 0
	wlines = []
	sourcefile = "/storage/9C33-6BBD/endless sky/data/map systems.txt"
	targetfile = "asteroids.txt"
	with open(sourcefile, "r") as sourcefile:
		lines = sourcefile.readlines()
	for line in lines:
		if line[:6] == "system":
			systemcount = systemcount + 1 
			wlines.append("\n")
			wlines.append(line)
		if line[:23] == '	asteroids "small rock"':
			asteroidcount = asteroidcount + 1
			wlines.append('	remove asteroids "small rock"\n')
		if line[:24] == '	asteroids "medium rock"':
			asteroidcount = asteroidcount + 1
			wlines.append('	remove asteroids "medium rock"\n')
		if line[:23] == '	asteroids "large rock"':
			asteroidcount = asteroidcount + 1
			wlines.append('	remove asteroids "large rock"\n')
		if line[:24] == '	asteroids "small metal"':
			asteroidcount = asteroidcount + 1
			wlines.append('	remove asteroids "small metal"\n')
		if line[:25] == '	asteroids "medium metal"':
			asteroidcount = asteroidcount + 1
			wlines.append('	remove asteroids "medium metal"\n')
		if line[:24] == '	asteroids "large metal"':
			asteroidcount = asteroidcount + 1
			wlines.append('	remove asteroids "large metal"\n')
	with open(targetfile, "w") as targetfile:
		targetfile.writelines("# number of systems: " + str(systemcount) + "\n")	
		targetfile.writelines("# number of asteroid entries: " + str(asteroidcount) + "\n")
		for line in wlines:
			targetfile.writelines(line)


if __name__ == "__main__":
	remove_asteroids()