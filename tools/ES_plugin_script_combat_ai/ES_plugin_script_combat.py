
def read_templates():
	outfitlines = []
	xp, outfittxt, outfittemplate, mission1template, mission2template, mission3template, mission4template, substitutions = '', '', '', '', '', '', '', ''
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
		elif curPos.startswith('# mission 4:'):
			mission4template += line
		elif curPos.startswith('# substitutions'):
			substitutions += line
	outfittxt += '\n\n'
	return outfitlines, xp, outfittxt, outfittemplate, mission1template, mission2template, mission3template, mission4template, substitutions


def create_outfits(outfitlines, outfittxt, outfittemplate):
	outfitnames, displaynames, maxranks = [], [], []
	outfits = ''
	for outfit in outfitlines:
		stattxt = ''
		splitted = outfit.split('|')
		outfitname = splitted[0]
		outfitnames.append(outfitname)
		displayname = splitted[1]
		displaynames.append(displayname)
		maxranks.append(splitted[2])
		for i in range(3,len(splitted)):
			stattxt += '\t' + splitted[i].strip() + '\n'
		replaced = outfittemplate\
			.replace('<outfitname>', outfitname)\
			.replace('<displayname>', displayname)\
			.replace('<stats>', stattxt[0:-1])
		outfits += replaced + '\n\n'
	outfittxt += outfits
	return outfittxt, outfitnames, displaynames, maxranks


def create_mission1(outfitnames, mission1template):
	outfitvar = ''
	for outfit in outfitnames:
		if outfit.startswith('basic'):
			outfitvar += '\t\t"combat_ai_installed_' + outfit  + '" = 0\n'
		elif outfit.startswith('advanced'):
			outfitvar += '\t\t"combat_ai_installed_' + outfit  + '" = 0\n'
		elif outfit.startswith('special'):
			outfitvar += '\t\t"combat_ai_installed_' + outfit  + '" = 0\n'
	mission1txt = mission1template\
		.replace('<outfitvar>', outfitvar[0:-1])
	return mission1txt


def create_mission2(xp, outfitnames, maxranks, displaynames, mission2template):
	# reading xp
	splitted = xp.split('|')
	xp1 = splitted[0]
	xp2 = splitted[1]
	xp3 = splitted[2].strip()
	# create mission2txt
	basic1, basic2, advanced1, advanced2, special1, special2 = '', '', '', '', '', ''
	for outfit in outfitnames:
		index = outfitnames.index(outfit)
		rankstr = ' max ' + maxranks[index] if maxranks[index] != '-' else ''
		if outfit.startswith('basic'):
			basic1 += '\t\t\t\t`\t' + displaynames[index] + ' (current rank: &[combat_ai_installed_' + outfit + ']' + rankstr + ')`\n'
			if maxranks[index] != '-':
				basic1 += '\t\t\t\t\tto display\n'
				basic1 += '\t\t\t\t\t\t"combat_ai_installed_' + outfit + '" < ' + maxranks[index] + '\n'
			basic1 += '\t\t\t\t\tgoto "' + outfit + '"\n'
			basic2 += '\t\t\tlabel "' + outfit + '"\n'
			basic2 += '\t\t\taction\n'
			basic2 += '\t\t\t\toutfit "combat_ai_' + outfit + '" 1\n'
			basic2 += '\t\t\t\t"combat_ai_installed_' + outfit + '" ++\n'
			basic2 += '\t\t\t`\tInstalled ' + displaynames[index] + ' rank &[combat_ai_installed_' + outfit + ']...`\n'
			basic2 += '\t\t\t\tgoto "start1"\n'
		elif outfit.startswith('advanced'):
			advanced1 += '\t\t\t\t`\t' + displaynames[index] + ' (current rank: &[combat_ai_installed_' + outfit + ']' + rankstr + ')`\n'
			if maxranks[index] != '-':
				advanced1 += '\t\t\t\t\tto display\n'
				advanced1 += '\t\t\t\t\t\t"combat_ai_installed_' + outfit + '" < ' + maxranks[index] + '\n'
			advanced1 += '\t\t\t\t\tgoto "' + outfit + '"\n'
			advanced2 += '\t\t\tlabel "' + outfit + '"\n'
			advanced2 += '\t\t\taction\n'
			advanced2 += '\t\t\t\toutfit "combat_ai_' + outfit + '" 1\n'
			advanced2 += '\t\t\t\t"combat_ai_installed_' + outfit + '" ++\n'
			advanced2 += '\t\t\t`\tInstalled ' + displaynames[index] + ' rank &[combat_ai_installed_' + outfit + ']...`\n'
			advanced2 += '\t\t\t\tgoto "start2"\n'
		elif outfit.startswith('special'):
			special1 += '\t\t\t\t`\t' + displaynames[index] + ' (current rank: &[combat_ai_installed_' + outfit + ']' + rankstr + ')`\n'
			if maxranks[index] != '-':
				special1 += '\t\t\t\t\tto display\n'
				special1 += '\t\t\t\t\t\t"combat_ai_installed_' + outfit + '" < ' + maxranks[index] + '\n'
			special1 += '\t\t\t\t\tgoto "' + outfit + '"\n'
			special2 += '\t\t\tlabel "' + outfit + '"\n'
			special2 += '\t\t\taction\n'
			special2 += '\t\t\t\toutfit "combat_ai_' + outfit + '" 1\n'
			special2 += '\t\t\t\t"combat_ai_installed_' + outfit + '" ++\n'
			special2 += '\t\t\t`\tInstalled ' + displaynames[index] + ' rank &[combat_ai_installed_' + outfit + ']...`\n'
			special2 += '\t\t\t\tgoto "start3"\n'
	exitmission = \
		'				`	Enough updates for today! (continue on next day)`\n'
	exitmission1 = \
		'					goto "delay1"\n'
	exitmission2 = \
		'					goto "delay2"\n'
	exitmission3 = \
		'					goto "delay3"\n'
	mission2txt = mission2template\
		.replace('<basic>', basic1 + exitmission + exitmission1 + basic2[0:-1])\
		.replace('<advanced>', advanced1 + exitmission + exitmission2 + advanced2[0:-1])\
		.replace('<special>', special1 + exitmission + exitmission3 + special2[0:-1])\
		.replace('<xp1>', xp1)\
		.replace('<xp2>', xp2)\
		.replace('<xp3>', xp3)
	return mission2txt



def create_mission3(outfitnames, displaynames, mission3template):
	# create mission3txt
	conditions = ''
	cbasic, cadvanced, cspecial = 0, 0, 0
	for outfit in outfitnames:
		if outfit.startswith('basic'):
			cbasic += 1
			conditions += '\t\t\t"outfit (flagship installed): combat_ai_' + outfit + '" < "combat_ai_installed_' + outfit + '"\n'
		elif outfit.startswith('advanced'):
			cadvanced += 1
			conditions += '\t\t\t"outfit (flagship installed): combat_ai_' + outfit + '" < "combat_ai_installed_' + outfit + '"\n'
		elif outfit.startswith('special'):
			cspecial += 1
			conditions += '\t\t\t"outfit (flagship installed): combat_ai_' + outfit + '" < "combat_ai_installed_' + outfit + '"\n'
	#print(conditions)
	basic, advanced, special = '', '', ''
	for outfit in outfitnames:
		index = outfitnames.index(outfit)
		if outfit.startswith('basic'):
			cbasic += 1
			basic += '\t\t\tlabel "precheck ' + outfit + '"\n'
			if index != 0:
				basic += '\t\t\tbranch "check ' + outfitnames[index] + '"\n'
				basic += '\t\t\t\t"combat_ai_counter" == 0\n'
				basic += '\t\t\t`\trestored &[combat_ai_counter] x ' + displaynames[index-1] + '`\n'
			basic += '\t\t\taction\n'
			basic += '\t\t\t\t"combat_ai_counter" = 0\n'
			basic += '\t\t\tlabel "check ' + outfit + '"\n'
			basic += '\t\t\tbranch "precheck ' + outfitnames[index + 1] + '"\n'
			basic += '\t\t\t\t"outfit (flagship installed): combat_ai_' + outfit + '" == "combat_ai_installed_' + outfit + '"\n'
			basic += '\t\t\taction\n'
			basic += '\t\t\t\toutfit "combat_ai_' + outfit + '" 1\n'
			basic += '\t\t\t\t"combat_ai_counter" ++\n'
			basic += '\t\t\tbranch "check ' + outfit + '"\n'
		elif outfit.startswith('advanced'):
			cadvanced += 1
			advanced += '\t\t\tlabel "precheck ' + outfit + '"\n'
			advanced += '\t\t\tbranch "check ' + outfitnames[index] + '"\n'
			advanced += '\t\t\t\t"combat_ai_counter" == 0\n'
			advanced += '\t\t\t`\trestored &[combat_ai_counter] x ' + displaynames[index-1] + '`\n'
			advanced += '\t\t\taction\n'
			advanced += '\t\t\t\t"combat_ai_counter" = 0\n'
			advanced += '\t\t\tlabel "check ' + outfit + '"\n'
			advanced += '\t\t\tbranch "precheck ' + outfitnames[index + 1] + '"\n'
			advanced += '\t\t\t\t"outfit (flagship installed): combat_ai_' + outfit + '" == "combat_ai_installed_' + outfit + '"\n'
			advanced += '\t\t\taction\n'
			advanced += '\t\t\t\toutfit "combat_ai_' + outfit + '" 1\n'
			advanced += '\t\t\t\t"combat_ai_counter" ++\n'
			advanced += '\t\t\tbranch "check ' + outfit + '"\n'
		elif outfit.startswith('special'):
			cspecial += 1
			special += '\t\t\tlabel "precheck ' + outfit + '"\n'
			special += '\t\t\tbranch "check ' + outfitnames[index] + '"\n'
			special += '\t\t\t\t"combat_ai_counter" == 0\n'
			special += '\t\t\t`\trestored  &[combat_ai_counter] x  ' + displaynames[index-1] + '`\n'
			special += '\t\t\taction\n'
			special += '\t\t\t\t"combat_ai_counter" = 0\n'
			special += '\t\t\tlabel "check ' + outfit + '"\n'
			if index != len(outfitnames) -1:
				special += '\t\t\tbranch "precheck ' + outfitnames[index + 1] + '"\n'
			else:
				special += '\t\t\tbranch "preend"\n'
			special += '\t\t\t\t"outfit (flagship installed): combat_ai_' + outfit + '" == "combat_ai_installed_' + outfit + '"\n'
			special += '\t\t\taction\n'
			special += '\t\t\t\toutfit "combat_ai_' + outfit + '" 1\n'
			special += '\t\t\t\t"combat_ai_counter" ++\n'
			special += '\t\t\tbranch "check ' + outfit + '"\n'
	mission3txt = mission3template\
		.replace('<conditions>', conditions[0:-1])\
		.replace('<basic>', basic[0:-1])\
		.replace('<advanced>', advanced[0:-1])\
		.replace('<special>', special[0:-1])
	return mission3txt


def create_mission4(outfitnames, mission4template):
	# create mission4txt
	basic, advanced, special = '', '', ''
	for outfit in outfitnames:
		index = outfitnames.index(outfit)
		if outfit.startswith('basic'):
			basic += '\t\t\tlabel "check ' + outfit + '"\n'
			basic += '\t\t\tbranch "check ' + outfitnames[index + 1] + '"\n'
			basic += '\t\t\t\t"outfit (flagship installed): combat_ai_' + outfit + '" == 0\n'
			basic += '\t\t\taction\n'
			basic += '\t\t\t\toutfit "combat_ai_' + outfit + '" -1\n'
			basic += '\t\t\tbranch "check ' + outfit + '"\n'
		elif outfit.startswith('advanced'):
			advanced += '\t\t\tlabel "check ' + outfit + '"\n'
			advanced += '\t\t\tbranch "check ' + outfitnames[index + 1] + '"\n'
			advanced += '\t\t\t\t"outfit (flagship installed): combat_ai_' + outfit + '" == 0\n'
			advanced += '\t\t\taction\n'
			advanced += '\t\t\t\toutfit "combat_ai_' + outfit + '" -1\n'
			advanced += '\t\t\tbranch "check ' + outfit + '"\n'
		elif outfit.startswith('special'):
			special += '\t\t\tlabel "check ' + outfit + '"\n'
			if index != len(outfitnames) -1:
				special += '\t\t\tbranch "check ' + outfitnames[index + 1] + '"\n'
			else:
				special += '\t\t\tbranch "end"\n'
			special += '\t\t\t\t"outfit (flagship installed): combat_ai_' + outfit + '" == 0\n'
			special += '\t\t\taction\n'
			special += '\t\t\t\toutfit "combat_ai_' + outfit + '" -1\n'
			special += '\t\t\tbranch "check ' + outfit + '"\n'
	mission4txt = mission4template\
		.replace('<basic>', basic[0:-1])\
		.replace('<advanced>', advanced[0:-1])\
		.replace('<special>', special[0:-1])		
	return mission4txt


def write_file(outfittxt, mission1txt, mission2txt, mission3txt, mission4txt, substitutions):
	# write to file
	with open('combatAI.txt', 'w') as target:
		target.writelines(substitutions + '\n\n' + outfittxt + '\n\n' + mission1txt + '\n\n' + mission2txt + '\n\n' + mission3txt + '\n\n' + mission4txt)


def run():
	outfitlines, xp, outfittxt, outfittemplate, mission1template, mission2template, mission3template, mission4template, substitutions = read_templates()
	outfittxt, outfitnames, displaynames, maxranks = create_outfits(outfitlines, outfittxt, outfittemplate)
	mission1txt = create_mission1(outfitnames, mission1template)
	mission2txt = create_mission2(xp, outfitnames, maxranks, displaynames, mission2template)
	mission3txt = create_mission3(outfitnames, displaynames, mission3template)
	mission4txt = create_mission4(outfitnames, mission4template)
	write_file(outfittxt, mission1txt, mission2txt, mission3txt, mission4txt, substitutions)


if __name__ == "__main__":
	run()