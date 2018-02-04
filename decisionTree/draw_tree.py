# draw the final decision tree
def drawTree(subject,dataset,path,verti):
	import divide
	if path == {}:
		return 0
	else:
		for p in path:
			new_set = divide.attridivide(p[0],dataset)[p]
			count = {}
			for g in new_set[subject]:
				count[g] = count.get(g,0) + 1
			print verti*'| ' + p[0].lstrip(' ') + '=' + p[1] + ':' + ' ' + str(count)
			drawTree(subject,new_set,path[p],verti+1)