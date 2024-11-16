# change data_folder path to your data folder and run the script
# it generates 'show.reputation.mission.txt'
# which contains the scripted mission to show all found reputations


import os


def set_globals():
	print('setting global variables')
	global data_folder
	global govs
	global selected_govs
	data_folder = '/storage/9C33-6BBD/endless sky/data/' # change to your folder
	govs = []
	# see goverment list in data/governments.txt or inside the generated mission file
	# and choose here which you want inside the selected list.
	selected_govs =  [
			"Author", 
			"Bunrodea", 
			"Coalition", 
			"Deep", 
			"Deep Security", 
			"Free Worlds", 
			"Gegno", 
			"Gegno Scin", 
			"Gegno Vi", 
			"Hai", 
			"Hai Merchant (Sympathizers)", 
			"Hai (Unfettered)", 
			"Heliarch", 
			"Independent", 
			"Ka'het", 
			"Korath", 
			"Korath (Civilian)", 
			"Kor Efret", 
			"Lunarium", 
			"Merchant", 
			"Militia", 
			"Navy Intelligence", 
			"Navy (Oathkeeper)", 
			"Pirate", 
			"Pug", 
			"Pug (Wanderer)", 
			"Quarg", 
			"Quarg (Hai)", 
			"Quarg (Kor Efret)", 
			"Quarg (Gegno)", 
			"Remnant", 
			"Republic", 
			"Republic Intelligence", 
			"Syndicate", 
			"Wanderer"
			]


def read_everything():
	print('reading data folder')
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
				print('\treading: ' + folder + os.sep + text_file + spaces, end = '\r', flush= True)
				#time.sleep(.01)
				with open(data_folder + folder + os.sep + text_file, 'r') as source_file:
					lines = source_file.readlines()
				for line in lines:
					if line[:1] == '#':
						continue
					elif line == '\n':
						continue
					elif line[:1] == '\t':
						continue
					elif line[:4] == 'gove':
						line = line.replace('government "', '').replace('government ', '').replace('"\n', '').replace('\n', '')
						govs.append(line)
					

def create_txt():
	print('')
	print('creating text file')
	targetfile = "show.reputation.mission.txt"
	with open(targetfile, "w") as targetfile:
		targetfile.writelines('mission "show reputation"\n')
		targetfile.writelines('\tjob\n')
		targetfile.writelines('\trepeat\n')
		targetfile.writelines('\tname "(Show Reputations)"\n')
		targetfile.writelines('\tdescription "Shows a list of reputations. Accept mission, start and land again."\n')
		targetfile.writelines('\ton accept\n')
		targetfile.writelines('\t\tconversation\n')
		targetfile.writelines('\t\t\tlabel menu\n')
		targetfile.writelines('\t\t\tscene "outfit/icon"\n')
		targetfile.writelines('\t\t\t``\n')
		targetfile.writelines('\t\t\t`Menu:`\n')
		targetfile.writelines('\t\t\tchoice\n')
		targetfile.writelines('\t\t\t\t`\tReputation List (selected 35)`\n')
		targetfile.writelines('\t\t\t\t\tgoto selrep\n')
		targetfile.writelines('\t\t\t\t`\tReputation List (all)`\n')
		targetfile.writelines('\t\t\t\t\tgoto fullrep\n')
		targetfile.writelines('\t\t\t\t`\tclose this conversation`\n')
		targetfile.writelines('\t\t\t\t\tgoto end\n')
		targetfile.writelines('\t\t\tlabel selrep\n')
		targetfile.writelines('\t\t\t`Reputation List (selected 35)`\n')
		targetfile.writelines('\t\t\t``\n')
		for gov in selected_govs:
			targetfile.writelines('\t\t\t`&[reputation: ' + gov + ']\t' + gov + '`\n')
		targetfile.writelines('\t\t\t\tgoto menu\n')
		targetfile.writelines('\t\t\tlabel fullrep\n')
		targetfile.writelines('\t\t\t`Reputation List (all)`\n')
		targetfile.writelines('\t\t\t``\n')
		for gov in govs:
			targetfile.writelines('\t\t\t`&[reputation: ' + gov + ']\t' + gov + '`\n')
		targetfile.writelines('\t\t\t\tgoto menu\n')
		targetfile.writelines('\t\t\tlabel end\n')
		targetfile.writelines('\t\t\t\tdecline\n')
		targetfile.writelines('\ton daily\n')
		targetfile.writelines('\t\tfail\n')

				
def run():
	set_globals()
	read_everything()
	create_txt()


if __name__ == "__main__":
	run()