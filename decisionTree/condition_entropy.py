# attri and label should be two corresbonding lists with the same length
# attri is the value of attributes, label is the value of labels
# This function returns the entropy of 'label' given the condition of 'attri'
def condi_H(attri,label):
	import calc_entropy as cale
	total = len(attri)
	index = {}
	for feature in attri:
		index[feature] = index.get(feature,0) + 1
	pack = zip(attri,label)
	count = {}
	for catag in index.keys():
		li = [item[1] for item in pack if item[0] == catag]
		count[catag] = li
	H = 0.0
	for title in index.keys():
		H = H + cale.entro(count[title])*(float(index[title])/float(total))
	return H