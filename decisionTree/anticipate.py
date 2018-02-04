def get_label(subject,train,test,route):
	import divide
	if route == {}:
		index = {}
		for label in train[subject]:
			index[label] = index.get(label,0) + 1
		theKeys = index.keys()
		theValues = index.values()
		return theKeys[theValues.index(max(theValues))]
	else:
		for kvpair in route:
			if kvpair in test:
				feature = divide.attridivide(kvpair[0],train)
				test.remove(kvpair)
				return get_label(subject,feature[kvpair],test,route[kvpair])