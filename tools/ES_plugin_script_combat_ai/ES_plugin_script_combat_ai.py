
def create_plugin():
	outfitlines, outfitnames, firststats, maxranks, displaynames = [], [], [], [], []
	outfittxt, outfittemplate, mission1template, mission2template, mission3template, xp = '', '', '', '', '', ''
	with open('data.txt', 'r') as source:
		data = source.readlines()
	for line in data:
		if line.startswith('#'):
			curPos = line
			continue
		elif line.startswith('\n'):
			continue
		if curPos.startswith('# outfits:'):
			outfitlines.append(line.strip())
		elif curPos.startswith('# xp:'):
			xp += line
		elif curPos.startswith('# outfit core:'):
			outfittxt += line
		elif curPos.startswith('# outfit template:'):
			outfittemplate += line
		elif curPos.startswith('# mission 1:'):
			mission1template += line
		elif curPos.startswith('# mission 2:'):
			mission2template += line
		elif curPos.startswith('# mission 3:'):
			mission3template += line
	# creating outfittxt
	outfittxt += '\n\n'
	for outfit in outfitlines:
		splitted = outfit.split('|')
		outfitname = splitted[0]
		displayname = splitted[1]
		maxranks.append(splitted[2])
		stats = ''
		for i in range(3,len(splitted)):
			stats += '\t' + splitted[i].strip() + '\n'
		displaynames.append(displayname)
		outfitnames.append(outfitname)
		firststats.append(splitted[3].replace('"', ''))
		if outfitname.startswith('basic'):
			index = '01101'
		elif outfitname.startswith('advanced'):
			index = '01102'
		elif outfitname.startswith('special'):
			index = '01103'
		replaced = outfittemplate\
			.replace('<outfitname>', outfitname)\
			.replace('<displayname>', displayname)\
			.replace('<stats>', stats[0:-1])\
			.replace('<index>', index)
		outfittxt += replaced + '\n\n'
	# reading xp
	splitted = xp.split('|')
	xp1 = splitted[0]
	xp2 = splitted[1]
	xp3 = splitted[2].strip()
	# create mission1txt
	outfitvar = ''
	for outfit in outfitnames:
		if outfit.startswith('basic'):
			outfitvar += '\t\t"installed ' + outfit  + '" = 0\n'
		elif outfit.startswith('advanced'):
			outfitvar += '\t\t"installed ' + outfit  + '" = 0\n'
		elif outfit.startswith('special'):
			outfitvar += '\t\t"installed ' + outfit  + '" = 0\n'
	mission1txt = mission1template\
		.replace('<outfitvar>', outfitvar[0:-1])
	# create mission2txt
	basic1, basic2, advanced1, advanced2, special1, special2 = '', '', '', '', '', ''
	for outfit in outfitnames:
		index = outfitnames.index(outfit)
		rankstr = ' max ' + maxranks[index] if maxranks[index] != '-' else ''
		if outfit.startswith('basic'):
			basic1 += '\t\t\t\t`\t' + displaynames[index] + ' (current rank: &[installed ' + outfit + ']' + rankstr + ')`\n'
			if maxranks[index] != '-':
				basic1 += '\t\t\t\t\tto display\n'
				basic1 += '\t\t\t\t\t\t"installed ' + outfit + '" < ' + maxranks[index] + '\n'
			basic1 += '\t\t\t\t\tgoto "' + outfit + '"\n'
			basic2 += '\t\t\tlabel "' + outfit + '"\n'
			basic2 += '\t\t\taction\n'
			basic2 += '\t\t\t\toutfit "combat_ai_' + outfit + '" 1\n'
			basic2 += '\t\t\t\t"installed ' + outfit + '" ++\n'
			basic2 += '\t\t\t\t"oldinstalled1" ++\n'
			basic2 += '\t\t\t\t"updates1" --\n'
			basic2 += '\t\t\t`\tInstalled ' + displaynames[index] + ' rank &[installed ' + outfit + ']...`\n'
			basic2 += '\t\t\t\tgoto "start1"\n'
		elif outfit.startswith('advanced'):
			advanced1 += '\t\t\t\t`\t' + displaynames[index] + ' (current rank: &[installed ' + outfit + ']' + rankstr + ')`\n'
			if maxranks[index] != '-':
				advanced1 += '\t\t\t\t\tto display\n'
				advanced1 += '\t\t\t\t\t\t"installed ' + outfit + '" < ' + maxranks[index] + '\n'
			advanced1 += '\t\t\t\t\tgoto "' + outfit + '"\n'
			advanced2 += '\t\t\tlabel "' + outfit + '"\n'
			advanced2 += '\t\t\taction\n'
			advanced2 += '\t\t\t\toutfit "combat_ai_' + outfit + '" 1\n'
			advanced2 += '\t\t\t\t"installed ' + outfit + '" ++\n'
			advanced2 += '\t\t\t\t"oldinstalled2" ++\n'
			advanced2 += '\t\t\t\t"updates2" --\n'
			advanced2 += '\t\t\t`\tInstalled ' + displaynames[index] + ' rank &[installed ' + outfit + ']...`\n'
			advanced2 += '\t\t\t\tgoto "start2"\n'
		elif outfit.startswith('special'):
			special1 += '\t\t\t\t`\t' + displaynames[index] + ' (current rank: &[installed ' + outfit + ']' + rankstr + ')`\n'
			if maxranks[index] != '-':
				special1 += '\t\t\t\t\tto display\n'
				special1 += '\t\t\t\t\t\t"installed ' + outfit + '" < ' + maxranks[index] + '\n'
			special1 += '\t\t\t\t\tgoto "' + outfit + '"\n'
			special2 += '\t\t\tlabel "' + outfit + '"\n'
			special2 += '\t\t\taction\n'
			special2 += '\t\t\t\toutfit "combat_ai_' + outfit + '" 1\n'
			special2 += '\t\t\t\t"installed ' + outfit + '" ++\n'
			special2 += '\t\t\t\t"oldinstalled3" ++\n'
			special2 += '\t\t\t\t"updates3" --\n'
			special2 += '\t\t\t`\tInstalled ' + displaynames[index] + ' rank &[installed ' + outfit + ']...`\n'
			special2 += '\t\t\t\tgoto "start3"\n'
	mission2txt = mission2template\
		.replace('<basic>', basic1 + basic2[0:-1])\
		.replace('<advanced>', advanced1 + advanced2[0:-1])\
		.replace('<special>', special1 + special2[0:-1])\
		.replace('<xp1>', xp1)\
		.replace('<xp2>', xp2)\
		.replace('<xp3>', xp3)
	#print(mission2txt)
	# create mission3txt
	conditions = ''
	cbasic, cadvanced, cspecial = 0, 0, 0
	for outfit in outfitnames:
		if outfit.startswith('basic'):
			cbasic += 1
			conditions += '\t\t\t"outfit (flagship installed): combat_ai_' + outfit + '" < "installed ' + outfit + '"\n'
		elif outfit.startswith('advanced'):
			cadvanced += 1
			conditions += '\t\t\t"outfit (flagship installed): combat_ai_' + outfit + '" < "installed ' + outfit + '"\n'
		elif outfit.startswith('special'):
			cspecial += 1
			conditions += '\t\t\t"outfit (flagship installed): combat_ai_' + outfit + '" < "installed ' + outfit + '"\n'
	#print(conditions)
	basic, advanced, special = '', '', ''
	for outfit in outfitnames:
		index = outfitnames.index(outfit)
		if outfit.startswith('basic'):
			cbasic += 1
			basic += '\t\t\tlabel "check ' + outfit + '"\n'
			basic += '\t\t\tbranch "check ' + outfitnames[index + 1] + '"\n'
			basic += '\t\t\t\t"outfit (flagship installed): combat_ai_' + outfit + '" == "installed ' + outfit + '"\n'
			basic += '\t\t\taction\n'
			basic += '\t\t\t\toutfit "combat_ai_' + outfit + '" 1\n'
			basic += '\t\t\t`\trestoring lost basic data: ' + displaynames[index] + '...`\n'
			basic += '\t\t\t\tgoto "check ' + outfit + '"\n'
		elif outfit.startswith('advanced'):
			cadvanced += 1
			advanced += '\t\t\tlabel "check ' + outfit + '"\n'
			advanced += '\t\t\tbranch "check ' + outfitnames[index + 1] + '"\n'
			advanced += '\t\t\t\t"outfit (flagship installed): combat_ai_' + outfit + '" == "installed ' + outfit + '"\n'
			advanced += '\t\t\taction\n'
			advanced += '\t\t\t\toutfit "combat_ai_' + outfit + '" 1\n'
			advanced += '\t\t\t`\trestoring lost advanced data: ' + displaynames[index] + '...`\n'
			advanced += '\t\t\t\tgoto "check ' + outfit + '"\n'
		elif outfit.startswith('special'):
			cspecial += 1
			special += '\t\t\tlabel "check ' + outfit + '"\n'
			if index != len(outfitnames) -1:
				special += '\t\t\tbranch "check ' + outfitnames[index + 1] + '"\n'
			else:
				special += '\t\t\tbranch "end"\n'
			special += '\t\t\t\t"outfit (flagship installed): combat_ai_' + outfit + '" == "installed ' + outfit + '"\n'
			special += '\t\t\taction\n'
			special += '\t\t\t\toutfit "combat_ai_' + outfit + '" 1\n'
			special += '\t\t\t`\trestoring lost special data: ' + displaynames[index] + '...`\n'
			special += '\t\t\t\tgoto "check ' + outfit + '"\n'
	mission3txt = mission3template\
		.replace('<conditions>', conditions[0:-1])\
		.replace('<basic>', basic[0:-1])\
		.replace('<advanced>', advanced[0:-1])\
		.replace('<special>', special[0:-1])
	# write to file
	with open('combatAI.txt', 'w') as target:
		target.writelines(outfittxt + mission1txt + '\n\n' + mission2txt + '\n\n' + mission3txt)


if __name__ == "__main__":
	create_plugin()