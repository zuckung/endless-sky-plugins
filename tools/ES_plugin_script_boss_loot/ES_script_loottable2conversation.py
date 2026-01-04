
def write_loottable():
	text = ''
	tables = []
	conindex = []
	# putting tables into a list
	with open('loottables.txt', 'r') as s:
		lines = s.readlines()
	for line in lines:
		if line.startswith('conversation'):
			conindex.append(line)
			if text != '':
				tables.append(text)
				text = line
				continue
		text += line
	tables.append(text)
	# writing txt
	with open('dun.conversation.1.txt', 'w') as t:
		for each in conindex:
			t.writelines('# ' + each)
		t.writelines('\n\n\n')
		for each in tables:
			secondloot = []
			counter, top = 0, 100
			lines = each.split('\n')
			# writing comment
			for line in lines:
				if line != '':
					t.writelines('# ' + line + '\n')
			# writing branches
			for line in lines:
				if line.startswith('conversation'):
					t.writelines(line + '\n')
					t.writelines("\t`You've defeated the enemy! While scanning the debris field you've found " +\
						"an unstable data drive with the code frequency for the next wormhole. It will probably break when you enter human space.`\n")
					t.writelines("\t`You've also found: `\n")
					t.writelines('\taction\n')
					t.writelines('\t\t"dun_random2"  = "roll: 10" + 1\n')
					t.writelines('\t\t"dun_pay" = "dun_random2" * 200000\n')
					t.writelines('\tlabel "get payment"\n')
					t.writelines('\tbranch "continue loottable"\n')
					t.writelines('\t\t"dun_random2" < 1\n')
					t.writelines('\taction\n')
					t.writelines('\t\t"dun_random2" --\n')
					t.writelines('\t\tpayment 200000\n')
					t.writelines('\tbranch "get payment"\n')
					t.writelines('\tlabel "continue loottable"\n')
					t.writelines('\t`\tValuables worth &[dun_pay] credits, and`\n')
					t.writelines('\tlabel "loottable"\n')
				elif line == '':
					continue
				elif line.startswith('2ndloot'):
					secondloot.append(line.replace('2ndloot|', ''))
				else:
					counter += 1
					splitted = line.split('|')
					percent, display, name, image = splitted[0].replace('%', ''), splitted[1], splitted[2], splitted[3]
					t.writelines('\tbranch "' + str(counter) + '"\n')
					t.writelines('\t\t"dun_random" < ' + str(top) + '\n')
					t.writelines('\t\t"dun_random" >= ' + str(top - int(percent)) + '\n')
					top -= int(percent)
			# writing labels
			counter = 0
			for line in lines:
				if line.startswith('conversation'):
					continue
				elif line == '':
					continue
				elif line.startswith('2ndloot'):
					continue
				else:
					counter += 1
					splitted = line.split('|')
					percent, display, name, image = splitted[0].replace('%', ''), splitted[1], splitted[2], splitted[3]
					t.writelines('\tlabel "' + str(counter) + '"\n')
					t.writelines('\taction\n')
					t.writelines('\t\toutfit "' + name + '" 1\n')
					t.writelines('\t`\t' + display + '`\n')
					t.writelines('\tscene "' + image + '"\n')
					t.writelines('\tbranch "2ndloot"\n')
			# 2ndloot
			t.writelines('\tlabel "2ndloot"\n')
			t.writelines('\taction\n')
			t.writelines('\t\t"dun_random" = "roll: 100"\n')
			# writing branches for 2ndloot
			counter2, top = counter, 100
			for line in secondloot:
				counter2 += 1
				splitted = line.split('|')
				percent, display, name, image = splitted[0].replace('%', ''), splitted[1], splitted[2], splitted[3]
				t.writelines('\tbranch "' + str(counter2) + '"\n')
				t.writelines('\t\t"dun_random" < ' + str(top) + '\n')
				t.writelines('\t\t"dun_random" >= ' + str(top - int(percent)) + '\n')
				top -= int(percent)
			# writing labels for 2ndloot
			counter2 = counter
			for line in secondloot:
				counter2 += 1
				splitted = line.split('|')
				percent, display, name, image = splitted[0].replace('%', ''), splitted[1], splitted[2], splitted[3]
				t.writelines('\tlabel "' + str(counter2) + '"\n')
				t.writelines('\taction\n')
				t.writelines('\t\toutfit "' + name + '" 1\n')
				t.writelines('\t`\t' + display + '`\n')
				t.writelines('\tscene "' + image + '"\n')
				t.writelines('\tbranch "end"\n')
			t.writelines('\tlabel "end"\n')
			t.writelines('\n')
			counter, top = 0, 100		
			



def run():
	write_loottable()


if __name__ == "__main__":
	run()