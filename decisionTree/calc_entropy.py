# 'index' is a list that saves the labels, this function will return the entropy of 'index'
def entro(all_data):
    import math
    total = len(all_data)
    index = {}
    for label in all_data:
    	index[label] = index.get(label,0) + 1
    entropy = 0.0
    for i in index:
    	p = float(index[i])/float(total)
	entropy = entropy - (p*math.log(p,2.0))
    return entropy
