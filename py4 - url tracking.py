import urllib2
import re

urlNo = ['8022']
data = "the next nothing is"
while ("next nothing" in data):	
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' \
    + str(urlNo[0])
    print url
    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close()
    urlNo = re.findall(r'next nothing is \d+', data)
    urlNo = re.findall(r'\d+', urlNo[0])
    print urlNo
    print data
