import pickle, pprint
import sys

with open('banner.p', 'rb') as f:
    data1 = pickle.load(f)
    with open('output', 'wb') as output:
        for line in data1:
            for elem in line:
                output.write(elem[0]*elem[1])
            output.write('\n')
    #pprint.pprint(data1)
    #read_data = f.read()
    
    #pickle.dump(read_data, output)
    #output.close()
