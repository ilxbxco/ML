import sys
import calc_entropy
argument = sys.argv
f = open(argument[1])
g = open(argument[2],'w')
attributes = f.readline()
attributes = attributes.split(',')
all_data = []
for i in f.readlines():
	j = i.split(',')[-1]
	k = j.rstrip('\r\n')
	all_data.append(k)
the_sum = len(all_data)
index = {}
for label in all_data:
    	index[label] = index.get(label,0) + 1
entropy = calc_entropy.entro(all_data)
error = 1.0 - float(max(index.values()))/float(the_sum)
g.write('entropy: ' + str(entropy) + '\n')
g.write('error: ' + str(error))
f.close()
g.close()
