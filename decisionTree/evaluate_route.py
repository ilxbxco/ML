# This function takes in four arguments
# 'subject' is the final label that we should anticipate
# 'train' is the training set, stored as a notebook. Each attribute has a corresbonding value list
# 'depth' is depth
# 'route' is the final generated decision tree. It is a dic of a dic of a dic...
def thePath(subject,train,depth,route):
	import condition_entropy
	import calc_entropy
	import divide

    # base case of the recursion, if all features have been tested or depth is max, then stop.
	if len(train) == 1 or depth == 0:
		return route

	else:
		H = (0,'') # H[0] stores the mutual information, H[1] stores the attribute that we should split on
		for attributes in train:
			if attributes == subject: # don't test the label
				continue
			else:
				entr = calc_entropy.entro(train[subject]) - condition_entropy.condi_H(train[attributes],train[subject]) # calculate mutual information
				if entr < 0: # mutual information should not be less than 0
					continue 
				elif entr >= H[0]:
					H = (entr,attributes)
		if H[1] == '':
			return route # if no mutual information is greater than 0, don't split
		new_set = divide.attridivide(H[1],train) # new_set stores the training set of each corresbonding value of the picked attribute, please refer to 'divide.py'
		for deeper_books in new_set:
			route[deeper_books] = thePath(subject,new_set[deeper_books],depth-1,{})
		return route