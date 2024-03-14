




def create_txt():
	targetfile = "show.reputation.mission.txt"
	with open(targetfile, "w") as targetfile:
		targetfile.writelines('mission "show reputation"\n')
		targetfile.writelines('\tjob\n')
		targetfile.writelines('\trepeat\n')
		targetfile.writelines('\tname "(Show Reputations)"\n')
		targetfile.writelines('\tdescription "Shows a list of reputations. Accept mission, start and land again. Its shows the values in steps of 10, from -1000 to +1000."\n')
		targetfile.writelines('\ton complete\n')
		targetfile.writelines('\t\tconversation\n')
		targetfile.writelines('\t\t\t`Reputation List`\n')
		targetfile.writelines('\t\t\t``\n')
		for gov in govs:
			targetfile.writelines('\t\t\t`<rep' + gov + '> ' + gov + '`\n')
		targetfile.writelines('\t\t\t``\n')
		targetfile.writelines('\t\t\t`Its shows the values in steps of 10, from -1000 to +1000.`\n')
		targetfile.writelines('substitutions\n')
		for gov in govs:
			#for i in range(-500000, -110000, 10000):
			#	targetfile.writelines('\t"<rep' + gov + '>" "' + str(i) + '"\n')
			#	targetfile.writelines('\t\t"reputation: ' + gov + '" >= '+ str(i) +'\n')
			#for i in range(-100000, -11000, 1000):
			#	targetfile.writelines('\t"<rep' + gov + '>" "' + str(i) + '"\n')
			#	targetfile.writelines('\t\t"reputation: ' + gov + '" >= '+ str(i) +'\n')
			#for i in range(-10000, -1100, 100):
			#	targetfile.writelines('\t"<rep' + gov + '>" "' + str(i) + '"\n')
			#	targetfile.writelines('\t\t"reputation: ' + gov + '" >= '+ str(i) +'\n')
			targetfile.writelines('\t"<rep' + gov + '>" "<-1000"\n')
			targetfile.writelines('\t\t"reputation: ' + gov + '" >= -1000000\n')
			for i in range(-1000, 1010, 10):
				number = ''
				if i > -1000 and i < - 90:
					number = '-0' + str(i * -1)
				elif i > -100 and i < 0:
					number = '-00' + str(i * -1)
				elif i == 0:
					number = '+000' + str(i)
				elif i < 100 and i > 0:
					number = '+00' + str(i)
				elif i < 1000 and i > 90:
					number = '+0' + str(i)
				print(number)	
				targetfile.writelines('\t"<rep' + gov + '>" "' + number + '"\n')
				targetfile.writelines('\t\t"reputation: ' + gov + '" >= '+ str(i) +'\n')
			targetfile.writelines('\t"<rep' + gov + '>" ">1000"\n')
			targetfile.writelines('\t\t"reputation: ' + gov + '" > 1000\n')
			
				
# run
govs = [
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
			#"Deep Security", 
			#"Derelict", 
			#"Drak", 
			#"Drak (Hostile)", 
			#"Elenctic Commune", 
			#"Escort", "Escort (Betraying)", 
			#"Forest (Prey)", "Free Worlds", 
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
			"Hai Merchant", 
			"Hai Merchant (Sympathizers)", 
			#"Hai Merchant (Human)", 
			"Hai (Unfettered)", 
			#"Hai (Unfettered Wanderer Tribute)", 
			#"Hai (Friendly Unfettered)", 
			#"Hai (Unfettered Civilians)", 
			"Heliarch", 
			#"Heliarch Test Dummy", 
			#"Independent", 
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
			#"Republic Intelligence", 
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
create_txt()



