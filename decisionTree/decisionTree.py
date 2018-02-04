# This is just partially finished
import sys,csv,numpy
import  evaluate_route as evr
argument = sys.argv

f = file(argument[1],'rb')
read = csv.reader(f)
data = []
for line in read:
   data.append(line)
data = numpy.transpose(data)
data = data.tolist()
index = {}
for i in range(0,len(data)):
	index[data[i][0]] = data[i][1:]
print evr.thePath(data[len(data)-1][0],index,2,{})