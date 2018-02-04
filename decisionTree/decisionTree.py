# Instruction:
# python <trainingData>.csv <testData>.csv searchDepth <trainingLabels>.labels <testingLabels>.labels <errorRate>.txt
import sys,csv,numpy,anticipate,error_rate
import  evaluate_route as evr
import draw_tree as dt
argument = sys.argv

f = file(argument[1],'rb')
g = file(argument[2],'rb')
the_depth = int(argument[3])
writeTrain = open(argument[4],'w')
writeTest = open(argument[5],'w')
writeErr = open(argument[6],'w')

# initialize the training data, store them in a dictionary, each attribute has its own list of values
read = csv.reader(f)
data = []
for line in read:
   data.append(line)
data2 = numpy.transpose(data)
data2 = data2.tolist()
subject = data2[len(data2)-1][0]
index = {}
for i in range(0,len(data2)):
	index[data2[i][0]] = data2[i][1:]

# generate the decision tree
path = evr.thePath(subject,index,the_depth,{})

# evaluate the test values, saved in 'results'
read_test = csv.reader(g)
data_test = []
test_real_value = []
results = []
for line2 in read_test:
	data_test.append(line2)
header = data_test[0]
for line3 in data_test[1:]:
	results.append(anticipate.get_label(subject,index,zip(header,line3),path))
	test_real_value.append(line3[-1])

# evaluate the train values, saved in 'results_train'
results_train = []
header_train = data[0]
for line5 in data[1:]:
	results_train.append(anticipate.get_label(subject,index,zip(header_train,line5),path))

# calculate the error rates
err_train = error_rate.error(index[subject],results_train)
err_test = error_rate.error(test_real_value,results)

# print out the results
for final in results_train:
	writeTrain.write(str(final) + '\n')
for final in results:
	writeTest.write(str(final) + '\n')
writeErr.write(str(err_train) + '\n')
writeErr.write(str(err_test) + '\n')

# print out how I made the decision tree
final_data = index[subject]
final_count = {}
for final_search in final_data:
	final_count[final_search] = final_count.get(final_search,0) + 1
print str(final_count)
dt.drawTree(subject,index,path,1)

writeTrain.close()
writeTest.close()
writeErr.close()
