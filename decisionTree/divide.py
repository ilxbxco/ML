# this function returns the training set of each corresbonding value of the picked attribute, 'attri', given the original training set 'train'
# 'attri' is a string of the attribute that you want to split on
# 'train' is a dictionary that should contrain 'attri'
def attridivide(attri,train):
	import numpy as np
	the_set = {}
	master = train.pop(attri) # get the values of 'attri', and new set should contain train[attri]
	keys = train.keys()
	val_mat = np.array(train.values())
	number = len(train)

	# give each different values in 'attri' their own training set
	# this is stored in the form of {(attribute name, attribute value): its training set}
	for i in range(0,len(master)):
		matrix = the_set.get((attri,master[i]),np.empty([number,0]))
		the_column = val_mat[:,i]
		the_set[(attri,master[i])] = np.column_stack((matrix,the_column)) 

	# the generated training sets are in the same form as 'train'
	for index in the_set:
		temp = the_set[index]
		the_set[index] = dict(zip(keys,temp.tolist())) 
	return the_set