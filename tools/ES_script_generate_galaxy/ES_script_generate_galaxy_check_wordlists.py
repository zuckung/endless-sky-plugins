


def read_starsfile():
	starfilenames = []
	with open('nameStars.txt', 'r') as source:
		lines = source.readlines()
	for line in lines:
		starfilenames.append(line.replace('\n', ''))
	return starfilenames

def read_starsdata():
	stardatanames = []
	with open(datafolder + 'map systems.txt', 'r') as source:
		lines = source.readlines()
	for line in lines:
		if line.startswith('system '):
			line = line.replace('system ', '').replace('\n', '').replace('"', '')
			stardatanames.append(line)
	return stardatanames

def compare_s(starfilenames, stardatanames):
	newlist = []
	for each in starfilenames:
		if not each in stardatanames:
			newlist.append(each)
	with open('newlist.txt', 'w') as target:
		for each in newlist:
			target.writelines(each + '\n')
	return newlist


def readplanetfile():
	planetfilenames = []
	with open('namePlanets.txt', 'r') as source:
		lines = source.readlines()
	for line in lines:
		planetfilenames.append(line.replace('\n', ''))
	return planetfilenames


def read_planetdata():
	planetdatanames = []
	with open(datafolder + 'map planets.txt', 'r') as source:
		lines = source.readlines()
	for line in lines:
		if line.startswith('planet '):
			line = line.replace('planet ', '').replace('\n', '').replace('"', '')
			planetdatanames.append(line)
	return planetdatanames


def compare_p(planetfilenames, planetdatanames):
	newlist = []
	for each in planetfilenames:
		if not each in planetdatanames:
			newlist.append(each)
	with open('newlist.txt', 'w') as target:
		for each in newlist:
			target.writelines(each + '\n')
	return newlist


def run():
	global datafolder
	datafolder = '/storage/9C33-6BBD/endless sky/data/' # folder to the ES data
	print('Compares the planet/star names of the ES data folder and the wordlist files. A new file with the cleaned wordlist gets generated.')
	print('	type 1 for comparing the stars')
	print('	type 2 for comparing the planets')
	print('	type anything else for exit')
	choice = input()
	if choice == '1':
		starfilenames = read_starsfile() # list of blank star names from file nameStars.txt
		stardatanames = read_starsdata() # list of blank star names frim ES data folder
		newlist = compare_s(starfilenames, stardatanames) # creates newlist.txt
		print('\nstarfilenames', len(starfilenames))
		print('stardatanames', len(stardatanames))
		print('newlist', len(newlist))
	elif choice == '2':
		planetfilenames = readplanetfile() # list of blank planet names from file namePlanets.txt
		planetdatanames = read_planetdata() # list of blank planet names from ES data folder
		newlist = compare_p(planetfilenames, planetdatanames)
		print('\nplanetfilenames', len(planetfilenames))
		print('planetdatanames', len(planetdatanames))
		print('newlist', len(newlist))
	else:
		exit()


if __name__ == '__main__':
	run()