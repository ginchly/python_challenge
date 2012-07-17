#!/usr/bin/python
from string import maketrans
str = "map"

normal = "abcdefghijklmnopqrstuvwxyz"
coded = "cdefghijklmnopqrstuvwxyzab"

trantab = maketrans(normal, coded)
print str.translate(trantab)

