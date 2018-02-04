def error(set1,set2):
	count = 0
	length = len(set1)
	for i in range(0,length):
		if set1[i] != set2[i]:
			count = count + 1
	return float(count)/float(length)