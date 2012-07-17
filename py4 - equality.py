#!/usr/bin/python
import re
#p = re.compile('[A-Z]{3}[a-z][A-Z]{3}')
p = re.compile('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]')

with open('py4.txt', 'r') as f:
    read_data = f.read()
#print read_data
#read_data = "ABCaGFDljalkjdlandlalaldksnnadlGFHuGDT"
print p.findall(read_data)

