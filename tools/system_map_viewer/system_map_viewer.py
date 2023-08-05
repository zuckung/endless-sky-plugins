import matplotlib.pyplot as plt


def check_exclude():
	if exclude == True:
		exclude_list = exclude_systems
	else:
		exclude_list = ["void"]
	return exclude_list

def read_file():
	systems, positions_x, positions_y = [], [], []
	gotsys = 0
	with open (systemsfile)as file1:
		all_lines = file1.readlines()
	for line in all_lines:
		if gotsys == 0:
			if line[:6] == "system":
				line = line.replace("system", "").replace('"', '').strip()
				for check in exclude_list:
					if line != check:
						do_it = 1
					else:
						do_it = 0
						break
				if do_it == 1:
					systems.append(line)
					gotsys = 1
		else:
			if line[:5] == "\tpos ":
				line = (line.replace("\tpos ", "").strip())
				positions_x.append(float(line.split(" ")[0]))
				positions_y.append(float(line.split(" ")[1]))
				gotsys = 0
	return systems, positions_x, positions_y
		
def sort_axis(positions):
	pos_x = []
	for x in positions:
		num = float(x)
		pos_x.append(num)
	pos_x = sorted(pos_x)
	for x in pos_x:
		print(x)
		
def plot_map(pos_x, pos_y, sys):
	fig, ax = plt.subplots()
	ax.set_title('Full Endless Sky Map', fontsize=20)
	#plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
	#plt.margins(0,0)
	ax.scatter(pos_x, pos_y)
	for i, txt in enumerate(sys):
   	 ax.annotate(txt, (pos_x[i], pos_y[i]))   
	plt.gca().invert_yaxis()
	plt.autoscale(tight=True)
	plt.show()	

#setting variables
systemsfile = "map systems.txt"
exclude = True # exclude exclude_systems from showing in map? True or False
exclude_systems = ["World's End", "Over the Rainbow", "Terra Incognita"] # pug galaxy systems. would scale the map too much. Won't get listed if exlude is True.

# running
exclude_list = check_exclude() # check if systems are excluded
systems, positions_x, positions_y = read_file()  # create
plot_map(positions_x, positions_y, systems)

#sort_axis(positions_x) # show all sorted coordinates x
#sort_axis(positions_y) # show all sorted coordinates y
# × = -1436.63 to 1206.6 (3 x 9966.5) | y = 994.955 to 772.051 (3 x 7176.0)