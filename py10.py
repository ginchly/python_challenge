
i = 0
freq = 1
prev = 0
newStr = []
seqList = []
lastEntry = '1'
while i < 30:
    b = lastEntry
    for num in b:
        if num == prev:
            freq = freq + 1
        else:
            if prev != 0:    #  not the first iteration
                newStr.append(str(freq) + str(prev))
            freq = 1
        prev = num
    newStr.append(str(freq) + str(prev))
    lastEntry = "".join(item for item in newStr)
    newStr = []
    freq = 1
    prev = 0
    #seqList.append(lastEntry)
    i = i + 1
    print i
print len(lastEntry)
