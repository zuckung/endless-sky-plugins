# copy the file "map systems.txt" from your ES data folder to the same folder this py-file is in.
# run this py-file
# use the created asteroids.txt in your plugin
# i.e. too.many.asteroids/data/asteroids.txt

# with this python script you will allways get an up to date plugin

with open("map systems.txt", "r") as sourcefile:
	with open("asteroids.txt", "w") as targetfile:
		systemcount = 0
		asteroidcount = 0
		wlines = []
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
		
		targetfile.writelines("# number of systems: " + str(systemcount) + "\n")	
		targetfile.writelines("# number of asteroid entries: " + str(asteroidcount) + "\n")		
		for line in wlines:
			targetfile.writelines(line)			