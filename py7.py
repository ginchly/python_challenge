import Image
import png
import numpy
import itertools

levelStr = ''

reader = png.Reader(filename='oxygen.png')  # streams are also accepted
w, h, pixels, metadata = reader.read()
pixel_byte_width = 4 if metadata['alpha'] else 3
image_2d = numpy.vstack(itertools.imap(numpy.uint16, pixels))
for elem in image_2d:
    if elem[0] == 115:
        everyFifth = elem[::4]
        print everyFifth
        for pix in everyFifth:
            levelStr = levelStr + chr(pix) + ' '
        break
#print levelStr
with open('output7', 'wb') as output:
    levelStr = levelStr[::6]
    output.write(levelStr)


newStr = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join(map(chr,newStr))
#for asc in newStr:
#    print chr(asc)
#  105 110 116 101 103 114 105 116 121
