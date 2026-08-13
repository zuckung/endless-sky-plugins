import os

       
def write():
	# get folder/colors
	folder = os.listdir('label/')
	folders = []
	for f in folder:
		if os.path.isdir('label/' + f) and not f == 'borders':
			folders.append(f)
	# check folder order and save if changed
	with open('folder_order.cfg', 'r') as source:
		lines = source.readlines()
	folder_order = []
	changed = False
	for line in lines:
		folder_order.append(line.strip())
	for folder in folders:
		if folder in folder_order:
			continue
		else:
			changed = True
			folder_order.append(folder)
	if changed == True:
		with open('folder_order.cfg', 'w') as target:
			for folder in folder_order:
				target.writelines(folder + '\n')
	print('writing missions and events for the following label folder:')
	for folder in folders:
		print('	' + folder)
	# create events
	events = ''
	event_header = ''
	event_borders = '' +\
		'# human borders\n' +\
		'event "activate borders"\n' +\
		'	galaxy "border deep"\n' +\
		'		pos -670 -270\n' +\
		'		sprite label/borders/border_deep\n' +\
		'	galaxy "border dirt belt"\n' +\
		'		pos -515 145\n' +\
		'		sprite "label/borders/border_dirt belt"\n' +\
		'	galaxy "border rim"\n' +\
		'		pos -778 228\n' +\
		'		sprite label/borders/border_rim\n' +\
		'	galaxy "border south"\n' +\
		'		pos -566 370\n' +\
		'		sprite label/borders/border_south\n' +\
		'	galaxy "border earth"\n' +\
		'		pos -400 115\n' +\
		'		sprite label/borders/border_earth\n' +\
		'	galaxy "border core"\n' +\
		'		pos -145 107\n' +\
		'		sprite label/borders/border_core\n' +\
		'	galaxy "border paradise"\n' +\
		'		pos -418 -95\n' +\
		'		sprite label/borders/border_paradise\n' +\
		'	galaxy "border north"\n' +\
		'		pos -350 -400\n' +\
		'		sprite label/borders/border_north\n' +\
		'event "deactivate borders"\n' +\
		'	galaxy "border deep"\n' +\
		'		pos -670 -270\n' +\
		'		sprite label/empty\n' +\
		'	galaxy "border dirt belt"\n' +\
		'		pos -515 145\n' +\
		'		sprite "label/empty"\n' +\
		'	galaxy "border rim"\n' +\
		'		pos -778 228\n' +\
		'		sprite label/empty\n' +\
		'	galaxy "border south"\n' +\
		'		pos -566 370\n' +\
		'		sprite label/empty\n' +\
		'	galaxy "border earth"\n' +\
		'		pos -400 115\n' +\
		'		sprite label/empty\n' +\
		'	galaxy "border core"\n' +\
		'		pos -145 107\n' +\
		'		sprite label/empty\n' +\
		'	galaxy "border paradise"\n' +\
		'		pos -418 -95\n' +\
		'		sprite label/empty\n' +\
		'	galaxy "border north"\n' +\
		'		pos -350 -400\n' +\
		'		sprite label/empty\n'
	event_original = '' +\
		'event "change original"\n' +\
		'	galaxy "label deep"\n' +\
		'		pos -658 -300\n' +\
		'		sprite label/deep\n' +\
		'	galaxy "label dirt belt"\n' +\
		'		pos -515 260\n' +\
  		'		sprite "label/dirt belt"\n' +\
		'	galaxy "label rim"\n' +\
		'		pos -778 265\n' +\
		'		sprite label/rim\n' +\
		'	galaxy "label south"\n' +\
		'		pos -566 501\n' +\
  		'		sprite label/south\n' +\
		'	galaxy "label earth"\n' +\
		'		pos -420 94\n' +\
		'		sprite label/earth\n' +\
  		'	galaxy "label core"\n' +\
		'		pos -136 130\n' +\
		'		sprite label/core\n' +\
		'	galaxy "label paradise"\n' +\
		'		pos -345 -136\n' +\
		'		sprite label/paradise\n' +\
		'	galaxy "label north"\n' +\
		'		pos -324 -332\n' +\
		'		sprite label/north\n' +\
		'event "change original hai"\n' +\
		'	galaxy "label hai"\n' +\
		'		pos -74 -497\n' +\
		'		sprite label/hai\n' +\
		'event "change original waste"\n' +\
		'	galaxy "label waste"\n' +\
		'		pos 160 380\n' +\
		'		sprite label/waste\n' +\
		'event "change original graveyard"\n' +\
		'	galaxy "label graveyard"\n' +\
		'		pos 100 630\n' +\
		'		sprite label/graveyard\n' +\
		'event "change original korath"\n' +\
  		'	galaxy "label korath"\n' +\
		'		pos 165 -347\n' +\
		'		sprite label/korath\n' +\
		'event "change original bunrodea"\n' +\
		'	galaxy "label bunrodea"\n' +\
		'		pos 328 -210\n' +\
		'		sprite label/empty\n' +\
		'event "change original gegno"\n' +\
		'	galaxy "label gegno"\n' +\
		'		pos 854 -544\n' +\
		'		sprite label/gegno\n' +\
		'event "change original umbral"\n' +\
		'	galaxy "label umbral"\n' +\
		'		pos 1150 -500n' +\
		'		sprite label/umbral\n' +\
		'event "change original wanderers"\n' +\
		'	galaxy "label wanderers"\n' +\
		'		pos -145 -753\n' +\
		'		sprite label/wanderers\n' +\
		'event "change original incipias"\n' +\
		'	galaxy "label incipias"\n' +\
		'		pos 300 -870\n' +\
		'		sprite label/incipias\n' +\
		'event "change original coalition"\n' +\
		'	galaxy "label arachi"\n' +\
		'		pos -750 615\n' +\
		'		sprite label/arachi\n' +\
		'	galaxy "label kimek"\n' +\
		'		pos -1250 215\n' +\
		'		sprite label/kimek\n' +\
		'	galaxy "label saryds"\n' +\
		'		pos -1080 678\n' +\
		'		sprite label/saryds\n' +\
		'event "change original avgi"\n' +\
		'	galaxy "label outer limits"\n' +\
		'		pos -540 1260\n' +\
		'		sprite "label/outer limits"\n' +\
		'	galaxy "label tangled shroud"\n' +\
		'		pos -300 1080\n' +\
		'		sprite "label/tangled shroud"\n' +\
		'	galaxy "label twilight"\n' +\
		'		pos -420 750\n' +\
		'		sprite label/twilight\n' +\
		'event "change original successors"\n' +\
		'	galaxy "label successors"\n' +\
		'		pos -122 1385\n' +\
		'		sprite label/successors\n'
	event_template = '' +\
		'# color folder "COLOR"\n' +\
		'event "change COLOR"\n' +\
		'	galaxy "label deep"\n' +\
		'		pos -590 -260\n' +\
		'		sprite label/COLOR/thedeep\n' +\
		'	galaxy "label dirt belt"\n' +\
		'		pos -480 247\n' +\
		'		sprite "label/COLOR/thedirtbelt"\n' +\
		'	galaxy "label rim"\n' +\
		'		pos -850 235\n' +\
		'		sprite label/COLOR/therim\n' +\
		'	galaxy "label south"\n' +\
		'		pos -600 470\n' +\
		'		sprite label/COLOR/thesouth\n' +\
		'	galaxy "label earth"\n' +\
		'		pos -350 70\n' +\
		'		sprite label/COLOR/nearearth\n' +\
		'	galaxy "label core"\n' +\
		'		pos -136 -10\n' +\
		'		sprite label/COLOR/thecore\n' +\
		'	galaxy "label paradise"\n' +\
		'		pos -420 -110\n' +\
		'		sprite label/COLOR/paradiseworlds\n' +\
		'	galaxy "label north"\n' +\
		'		pos -385 -460\n' +\
		'		sprite label/COLOR/thenorth\n' +\
		'event "change COLOR hai"\n' +\
		'	galaxy "label hai"\n' +\
		'		pos 12 -538\n' +\
		'		sprite label/COLOR/haispace\n' +\
		'event "change COLOR waste"\n' +\
		'	galaxy "label waste"\n' +\
		'		pos 137 250\n' +\
		'		sprite label/COLOR/theemberwaste\n' +\
		'event "change COLOR graveyard"\n' +\
		'	galaxy "label graveyard"\n' +\
		'		pos 132 589\n' +\
		'		sprite label/COLOR/thegraveyard\n' +\
		'event "change COLOR korath"\n' +\
		'	galaxy "label korath"\n' +\
		'		pos 97 -370\n' +\
		'		sprite label/COLOR/korathspace\n' +\
		'event "change COLOR bunrodea"\n' +\
		'	galaxy "label bunrodea"\n' +\
		'		pos 328 -210\n' +\
		'		sprite label/COLOR/bunrodeaspace\n' +\
		'event "change COLOR gegno"\n' +\
		'	galaxy "label gegno"\n' +\
		'		pos 797 -492\n' +\
		'		sprite label/COLOR/gegnospace\n' +\
		'event "change COLOR umbral"\n' +\
		'	galaxy "label umbral"\n' +\
		'		pos 1187 -564\n' +\
		'		sprite label/COLOR/umbralreach\n' +\
		'event "change COLOR wanderers"\n' +\
		'	galaxy "label wanderers"\n' +\
		'		pos -165 -738\n' +\
		'		sprite label/COLOR/wandererspace\n' +\
		'event "change COLOR incipias"\n' +\
		'	galaxy "label incipias"\n' +\
		'		pos 342 -911\n' +\
		'		sprite label/COLOR/incipiasspace\n' +\
		'event "change COLOR coalition"\n' +\
		'	galaxy "label arachi"\n' +\
		'		pos -739 600\n' +\
		'		sprite label/COLOR/arachi\n' +\
		'	galaxy "label kimek"\n' +\
		'		pos -1225 352\n' +\
		'		sprite label/COLOR/kimek\n' +\
		'	galaxy "label saryds"\n' +\
		'		pos -976 625\n' +\
		'		sprite label/COLOR/saryds\n' +\
		'event "change COLOR avgi"\n' +\
		'	galaxy "label outer limits"\n' +\
		'		pos -416 1283\n' +\
		'		sprite label/COLOR/outerlimits\n' +\
		'	galaxy "label tangled shroud"\n' +\
		'		pos -203 1051\n' +\
		'		sprite label/COLOR/tangledshroud\n' +\
		'	galaxy "label twilight"\n' +\
		'		pos -521 850\n' +\
		'		sprite label/COLOR/thetwilight\n' +\
		'event "change COLOR successors"\n' +\
		'	galaxy "label successors"\n' +\
		'		pos -210 1404\n' +\
		'		sprite label/COLOR/successorspace\n' +\
		'\n' +\
		'\n'
	event_header += '# 2 events for activating/deactivating human borders\n' +\
		'# 13 events for back to vanilla labels\n'
	for folder in folder_order:
		event_header += '# 13 events for "' + folder + '"\n'
		events += event_template.replace('COLOR', folder)
	# write events.txt
	with open('events.txt', 'w') as target:
		target.writelines(event_header + '\n\n\n' + event_borders + '\n\n' + event_original + '\n\n' + events)
	# create missions
	mission_change = ''
	mission_change_template = '' +\
		'mission "Map Labels and Borders"\n' +\
		'	name "(Map Labels and Borders)"\n' +\
		'	color selected "human.labels job: selected"\n' +\
		'	color unselected "human.labels job: unselected"\n' +\
		'	job\n' +\
		'	repeat\n' +\
		'	description "Changes the color and style of the map area labels."\n' +\
		'	source "Earth"\n' +\
		'	to offer\n' +\
		'		not "installed plugin: control.station"\n' +\
		'	on accept\n' +\
		'		conversation\n' +\
		'			label "start"' +\
		'			scene "scene/colors"\n' +\
		'			`Choose a style for the map area labels:`\n' +\
		'			choice\n' +\
		'%choices%' +\
		'				`	revert back to original labels`\n' +\
		'					goto "original"\n' +\
		'				`	activate the human area borders`\n' +\
		'					to display\n' +\
		'						"borders" == 0\n' +\
		'					goto "activate borders"\n' +\
		'				`	deactivate the human area borders`\n' +\
		'					to display\n' +\
		'						"borders" == 1\n' +\
		'					goto "deactivate borders"\n' +\
		'				`	done`\n' +\
		'					goto end\n' +\
		'%labels%' +\
		'			label "activate borders"\n' +\
		'			action\n' +\
		'				"borders" = 1\n' +\
		'				event "activate borders" 0\n' +\
		'			`Area borders are visible now!`\n' +\
		'				goto "start"\n' +\
		'			label "deactivate borders"\n' +\
		'			action\n' +\
		'				"borders" = 0\n' +\
		'				event "deactivate borders" 0\n' +\
		'			`Area borders are visible now!`\n' +\
		'				goto "start"\n' +\
		'			# original\n' +\
		'			label "original"\n' +\
		'			action\n' +\
		'				"label color" = 0\n' +\
		'				event "change original" 0\n' +\
		'			label "original Avgi"\n' +\
		'			branch "original Coalition"\n' +\
		'				not "Avgi: First Contact: offered"\n' +\
		'			action\n' +\
		'				event "change original avgi" 0\n' +\
		'			label "original Coalition"\n' +\
		'			branch "original Gegno"\n' +\
		'				not "Discovered Coalition Space: offered"\n' +\
		'			action\n' +\
		'				event "change original coalition" 0\n' +\
		'			label "original Gegno"\n' +\
		'			branch "original Hai"\n' +\
		'				not "Giaru Gegno: Quarg Contact: offered"\n' +\
		'			action\n' +\
		'				event "change original gegno" 0\n' +\
		'			label "original Hai"\n' +\
		'			branch "original Incipias"\n' +\
		'				not "Discovered Hai Space: offered"\n' +\
		'			action\n' +\
		'				event "change original hai" 0\n' +\
		'			label "original Incipias"\n' +\
		'			branch "original Graveyard"\n' +\
		'				not "Incipias: Warning of the Guardian: offered"\n' +\
		'			action\n' +\
		'				event "change original incipias" 0\n' +\
		'			label "original Graveyard"\n' +\
		'			branch "original Korath"\n' +\
		'				not "Graveyard Label: offered"\n' +\
		'			action\n' +\
		'				event "change original graveyard" 0\n' +\
		'			label "original Korath"\n' +\
		'			branch "original Remnant"\n' +\
		'				not "Discovered Korath Space: offered"\n' +\
		'			action\n' +\
		'				event "change original korath" 0\n' +\
		'			label "original Remnant"\n' +\
		'			branch "original Umbral"\n' +\
		'				not "First Contact: Remnant: offered"\n' +\
		'			action\n' +\
		'				event "change original waste" 0\n' +\
		'			label "original Umbral"\n' +\
		'			branch "original Successors"\n' +\
		'				not "Rulei: Umbral Reach: offered"\n' +\
		'			action\n' +\
		'				event "change original umbral" 0\n' +\
		'			label "original Successors"\n' +\
		'			branch "original Wanderer"\n' +\
		'				not "Successors: First Contact 1: offered"\n' +\
		'			action\n' +\
		'				event "change original successors" 0\n' +\
		'			label "original Wanderer"\n' +\
		'			branch "original Bunrodea"\n' +\
		'				not "Discovered Wanderer Space: offered"\n' +\
		'			action\n' +\
		'				event "change original wanderers" 0\n' +\
		'			label "original Bunrodea"\n' +\
		'			branch "original finish"\n' +\
		'				not "First Contact: Bunrodea (Hostile): offered"\n' +\
		'			action\n' +\
		'				event "change original bunrodea" 0\n' +\
		'			label "original finish"\n' +\
		'			`Label color and style changed back to original!`\n' +\
		'				goto start\n' +\
		'			label end\n' +\
		'			`Thanks for using this plugin :)`\n' +\
		'		fail\n'
	mission_change_choices_template = '' +\
		'				`	COLOR`\n' +\
		'					goto "COLOR"\n'
	mission_change_label_template = '' +\
		'			# COLOR\n' +\
		'			label "COLOR"\n' +\
		'			action\n' +\
		'				"label color" = %colornumber%\n' +\
		'%clearcolor%' +\
		'				event "change COLOR" 0\n' +\
		'			label "COLOR Avgi"\n' +\
		'			branch "COLOR Coalition"\n' +\
		'				not "Avgi: First Contact: offered"\n' +\
		'			action\n' +\
		'				event "change COLOR avgi" 0\n' +\
		'			label "COLOR Coalition"\n' +\
		'			branch "COLOR Gegno"\n' +\
		'				not "Discovered Coalition Space: offered"\n' +\
		'			action\n' +\
		'				event "change COLOR coalition" 0\n' +\
		'			label "COLOR Gegno"\n' +\
		'			branch "COLOR Hai"\n' +\
		'				not "Giaru Gegno: Quarg Contact: offered"\n' +\
		'			action\n' +\
		'				event "change COLOR gegno" 0\n' +\
		'			label "COLOR Hai"\n' +\
		'			branch "COLOR Incipias"\n' +\
		'				not "Discovered Hai Space: offered"\n' +\
		'			action\n' +\
		'				event "change COLOR hai" 0\n' +\
		'			label "COLOR Incipias"\n' +\
		'			branch "COLOR Graveyard"\n' +\
		'				not "Incipias: Warning of the Guardian: offered"\n' +\
		'			action\n' +\
		'				event "change COLOR incipias" 0\n' +\
		'			label "COLOR Graveyard"\n' +\
		'			branch "COLOR Korath"\n' +\
		'				not "Graveyard Label: offered"\n' +\
		'			action\n' +\
		'				event "change COLOR graveyard" 0\n' +\
		'			label "COLOR Korath"\n' +\
		'			branch "COLOR Remnant"\n' +\
		'				not "Discovered Korath Space: offered"\n' +\
		'			action\n' +\
		'				event "change COLOR korath" 0\n' +\
		'			label "COLOR Remnant"\n' +\
		'			branch "COLOR Umbral"\n' +\
		'				not "First Contact: Remnant: offered"\n' +\
		'			action\n' +\
		'				event "change COLOR waste" 0\n' +\
		'			label "COLOR Umbral"\n' +\
		'			branch "COLOR Successors"\n' +\
		'				not "Rulei: Umbral Reach: offered"\n' +\
		'			action\n' +\
		'				event "change COLOR umbral" 0\n' +\
		'			label "COLOR Successors"\n' +\
		'			branch "COLOR Wanderer"\n' +\
		'				not "Successors: First Contact 1: offered"\n' +\
		'			action\n' +\
		'				event "change COLOR successors" 0\n' +\
		'			label "COLOR Wanderer"\n' +\
		'			branch "COLOR Bunrodea"\n' +\
		'				not "Discovered Wanderer Space: offered"\n' +\
		'			action\n' +\
		'				event "change COLOR wanderers" 0\n' +\
		'			label "COLOR Bunrodea"\n' +\
		'			branch "COLOR finish"\n' +\
		'				not "First Contact: Bunrodea (Hostile): offered"\n' +\
		'			action\n' +\
		'				event "change COLOR bunrodea" 0\n' +\
		'			label "COLOR finish"\n' +\
		'			`Label color and style changed to "COLOR"!`\n' +\
		'				goto start\n'
	mission_header = '' +\
		'# colors\n' +\
		'# mission "Map Labels and Borders"\n' +\
		'# mission "Map Labels and Borders Control Station"\n' +\
		'# ' + str(11 * len(folder_order)) + ' recolor-on-area-discovery missions\n'
	mission_color = '' +\
		'color "human.labels job: selected" 0. .7 1. 0.\n' +\
		'color "human.labels job: unselected" .3 .5 .8 0.\n\n\n'
	mission_change_choices = ''
	mission_change_labels = ''
	clearcolor = ''
	for folder in folder_order:
		clearcolor += '				clear "event: change ' + folder + '"\n'
	for folder in folder_order:
		mission_change_choices += mission_change_choices_template.replace('COLOR', folder)
		mission_change_labels += mission_change_label_template.replace('COLOR', folder).replace('%colornumber%', str(folder_order.index(folder) + 1)).replace('%clearcolor%', clearcolor)
	mission_change += mission_change_template.replace('%choices%', mission_change_choices).replace('%labels%', mission_change_labels)
	# write missions.txt & controlstation.txt
	with open('missions.txt', 'w') as target:
		target.writelines(mission_header + '\n\n\n' + mission_color + mission_change + '\n\n')
		target.writelines( mission_change \
			.replace('mission "Map Labels and Borders"', 'mission "Map Labels and Borders Control Station"') \
			.replace('name "(Map Labels and Borders)"', 'name "[4] plugin: human.labels"')
			.replace('source "Earth"', 'source "Control Station"') \
			.replace('not "installed plugin: control.station"', 'has "installed plugin: control.station"') + '\n\n')
	# write space discovery missions
	discovery_template = '\n\n' +\
			'mission "label COLOR discovery avgi"\n' +\
			'	entering\n' +\
			'	invisible\n' +\
			'	destination "Earth"\n' +\
			'	to offer\n' +\
			'		has "Avgi: First Contact: offered"\n' +\
			'		not "event: change COLOR avgi"\n' +\
			'		"label color" == %colornumber%\n' +\
			'	on offer\n' +\
			'		event "change COLOR avgi" 0\n' +\
			'		fail\n' +\
			'\n\n' +\
			'mission "label COLOR discovery coalition"\n' +\
			'	entering\n' +\
			'	invisible\n' +\
			'	destination "Earth"\n' +\
			'	to offer\n' +\
			'		has "Discovered Coalition Space: offered"\n' +\
			'		not "event: change COLOR coalition"\n' +\
			'		"label color" == %colornumber%\n' +\
			'	on offer\n' +\
			'		event "change COLOR coalition" 0\n' +\
			'		fail\n' +\
			'\n\n' +\
			'mission "label COLOR discovery gegno"\n' +\
			'	entering\n' +\
			'	invisible\n' +\
			'	destination "Earth"\n' +\
			'	to offer\n' +\
			'		has "Giaru Gegno: Quarg Contact: offered"\n' +\
			'		not "event: change COLOR gegno"\n' +\
			'		"label color" == %colornumber%\n' +\
			'	on offer\n' +\
			'		event "change COLOR gegno" 0\n' +\
			'		fail\n' +\
			'\n\n' +\
			'mission "label COLOR discovery hai"\n' +\
			'	entering\n' +\
			'	invisible\n' +\
			'	destination "Earth"\n' +\
			'	to offer\n' +\
			'		has "Discovered Hai Space: offered"\n' +\
			'		not "event: change COLOR hai"\n' +\
			'		"label color" == %colornumber%\n' +\
			'	on offer\n' +\
			'		event "change COLOR hai" 0\n' +\
			'		fail\n' +\
			'\n\n' +\
			'mission "label COLOR discovery incipias"\n' +\
			'	entering\n' +\
			'	invisible\n' +\
			'	destination "Earth"\n' +\
			'	to offer\n' +\
			'		has "Incipias: Warning of the Guardian: offered"\n' +\
			'		not "event: change COLOR incipias"\n' +\
			'		"label color" == %colornumber%\n' +\
			'	on offer\n' +\
			'		event "change COLOR incipias" 0\n' +\
			'		fail\n' +\
			'\n\n' +\
			'mission "label COLOR discovery graveyard"\n' +\
			'	entering\n' +\
			'	invisible\n' +\
			'	destination "Earth"\n' +\
			'	to offer\n' +\
			'		has "Graveyard Label: offered"\n' +\
			'		not "event: change COLOR graveyard"\n' +\
			'		"label color" == %colornumber%\n' +\
			'	on offer\n' +\
			'		event "change COLOR graveyard" 0\n' +\
			'		fail\n' +\
			'\n\n' +\
			'mission "label COLOR discovery remnant"\n' +\
			'	entering\n' +\
			'	invisible\n' +\
			'	destination "Earth"\n' +\
			'	to offer\n' +\
			'		has "First Contact: Remnant: offered"\n' +\
			'		not "event: change COLOR waste"\n' +\
			'		"label color" == %colornumber%\n' +\
			'	on offer\n' +\
			'		event "change COLOR waste" 0\n' +\
			'		fail\n' +\
			'\n\n' +\
			'mission "label COLOR discovery korath"\n' +\
			'	entering\n' +\
			'	invisible\n' +\
			'	destination "Earth"\n' +\
			'	to offer\n' +\
			'		has "Discovered Korath Space: offered"\n' +\
			'		not "event: change COLOR korath"\n' +\
			'		"label color" == %colornumber%\n' +\
			'	on offer\n' +\
			'		event "change COLOR korath" 0\n' +\
			'		fail\n' +\
			'\n\n' +\
			'mission "label COLOR discovery umbral"\n' +\
			'	entering\n' +\
			'	invisible\n' +\
			'	destination "Earth"\n' +\
			'	to offer\n' +\
			'		has "Rulei: Umbral Reach: offered"\n' +\
			'		not "event: change COLOR umbral"\n' +\
			'		"label color" == %colornumber%\n' +\
			'	on offer\n' +\
			'		event "change COLOR umbral" 0\n' +\
			'		fail\n' +\
			'\n\n' +\
			'mission "label COLOR discovery successors"\n' +\
			'	entering\n' +\
			'	invisible\n' +\
			'	destination "Earth"\n' +\
			'	to offer\n' +\
			'		has "Successors: First Contact 1: offered"\n' +\
			'		not "event: change COLOR successors"\n' +\
			'		"label color" == %colornumber%\n' +\
			'	on offer\n' +\
			'		event "change COLOR successors" 0\n' +\
			'		fail\n' +\
			'\n\n' +\
			'mission "label COLOR discovery wanderer"\n' +\
			'	entering\n' +\
			'	invisible\n' +\
			'	destination "Earth"\n' +\
			'	to offer\n' +\
			'		has "Discovered Wanderer Space: offered"\n' +\
			'		not "event: change COLOR wanderers"\n' +\
			'		"label color" == %colornumber%\n' +\
			'	on offer\n' +\
			'		event "change COLOR wanderers" 0\n' +\
			'		fail\n' +\
			'\n\n' +\
			'mission "label COLOR discovery bunrodea"\n' +\
			'	entering\n' +\
			'	invisible\n' +\
			'	destination "Earth"\n' +\
			'	to offer\n' +\
			'		has "First Contact: Bunrodea (Hostile): offered"\n' +\
			'		not "event: change COLOR bunrodea"\n' +\
			'		"label color" == %colornumber%\n' +\
			'	on offer\n' +\
			'		event "change COLOR bunrodea" 0\n' +\
			'		fail\n'
	with open('missions.txt', 'a') as target:
		for folder in folder_order:
			target.writelines(discovery_template.replace('COLOR', folder).replace('%colornumber%', str(folder_order.index(folder) + 1)))


if __name__ == "__main__":
    write()