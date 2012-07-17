import zipfile
import re

fileNo = ['90052']
commentsDict = {}
comment = ''

z = zipfile.ZipFile("channel.zip", "r")

for i in z.infolist():
    commentsDict[i.filename] = i.comment


while True:
    fileName = fileNo[0] + '.txt'
    data = z.read(fileName)
    fileNo = re.findall(r'nothing is \d+', data)
    if fileNo:
        fileNo = re.findall(r'\d+', fileNo[0])
        comment = comment + commentsDict[fileName]
        #info = z.infolist(fileName[0])
        #print info
        #comments = comments + info.comment
        #print data
    else:
        #print data
        break

print comment

