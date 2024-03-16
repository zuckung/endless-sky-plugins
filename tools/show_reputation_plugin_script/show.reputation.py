import os

def set_globals():
	print('setting global variables')
	global data_folder
	global govs
	global selected_govs
	data_folder = '/storage/9C33-6BBD/endless sky/data_0.10.5/'
	govs = []
	selected_govs =  [
			#"Alpha", 
			"Author", 
			#"Bad Trip", 
			#"Builder", 
			"Bunrodea", 
			#"Bunrodea (Erabu)", 
			#"Bunrodea (Guard)", 
			#"Bunrodea (Megasa)", 
			#"Bounty", 
			#"Bounty (Disguised)", 
			#"Bounty Hunter", 
			#"Bounty Hunter that Won't Enter Hai Space", 
			"Coalition", 
			"Deep", 
			"Deep Security", 
			#"Derelict", 
			#"Drak", 
			#"Drak (Hostile)", 
			#"Elenctic Commune", 
			#"Escort", "Escort (Betraying)", 
			#"Forest (Prey)", 
			"Free Worlds", 
			#"Free Worlds that won't enter wormhole", 
			"Gegno", 
			"Gegno Scin", 
			"Gegno Vi", 
			#"Gegno Scin (Neutral)", 
			#"Gegno Vi (Neutral)", 
			#"Gegno Vi (Duelist A)", 
			#"Gegno Vi (Duelist B)", 
			"Hai", 
			#"Hai (Wormhole Access)", 
			#"Hai Merchant", 
			"Hai Merchant (Sympathizers)", 
			#"Hai Merchant (Human)", 
			"Hai (Unfettered)", 
			#"Hai (Unfettered Wanderer Tribute)", 
			#"Hai (Friendly Unfettered)", 
			#"Hai (Unfettered Civilians)", 
			"Heliarch", 
			#"Heliarch Test Dummy", 
			"Independent", 
			#"Independent (Killable)", 
			#"Indigenous Lifeform", 
			#"Indigenous Lifeform (Acheron)", 
			#"Indigenous Lifeform (Astral)", 
			"Ka'het", 
			#"Ka'het (Infighting)", 
			#"Ka'sei", 
			"Korath", 
			"Korath (Civilian)", 
			#"Korath Nanobots", 
			"Kor Efret", 
			#"Kor Mereti", 
			#"Kor Mereti, (Hostile)", 
			#"Kor Sestor", 
			"Lunarium", 
			#"Lunarium (Hidden)", 
			#"Marauder", 
			"Merchant", 
			#"Merchant (Hijacked)", 
			"Militia", 
			"Navy Intelligence", 
			"Navy (Oathkeeper)", 
			#"Neutral", 
			#"Parrot", 
			"Pirate", 
			#"Pirate (Devil-Run Gang)", 
			#"Pirate (Rival)", 
			"Pug", 
			"Pug (Wanderer)", 
			"Quarg", 
			"Quarg (Hai)", 
			"Quarg (Kor Efret)", 
			"Quarg (Gegno)", 
			"Remnant", 
			#"Remnant (Research)", 
			"Republic", 
			"Republic Intelligence", 
			#"Republic that won't enter wormhole", 
			#"Republic (Friendly)", 
			#"Rulei", 
			#"Scar's Legion", 
			#"Scar's Legion (Killable)", 
			#"Sheragi", 
			#"Smuggler (Hai Trafficker)", 
			"Syndicate", 
			#"Syndicate (Extremist)", 
			#"Team Blue", 
			#"Team Red", 
			#"Test Dummy", 
			#"Unknown", 
			#"Uninhabited", 
			#"Ember Waste", 
			"Wanderer", 
			#"Wormhole Alpha", 
			#"Syndicate (Hostile)"
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
				if os.path.isfile(data_folder + folder + '/' + text_file) == False:
					continue
				if len(folder + text_file)  < 80: # just for displaying / max len = 44(currently)
					count = 80 - len(folder + text_file)
					spaces = ''
					for i in range(0, count):
						spaces += ' '
				print('\treading: ' + folder + '/' + text_file + spaces, end = '\r', flush= True)
				#time.sleep(.01)
				with open(data_folder + folder + '/' + text_file, 'r') as source_file:
					lines = source_file.readlines()
				for line in lines:
					if line[:1] == '#':
						continue
					elif line == '\n':
						continue
					elif line[:1] == '\t':
						continue
					elif line[:4] == 'gove':
						line = line.replace('government "', '').replace('"\n', '')
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
		targetfile.writelines('\ton complete\n')
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
		

# maybe add some day
# "visited system: <system>"
#"visited planet: <planet>"
# "person destroyed: <name>"

				
# run
set_globals()
read_everything()
create_txt()




