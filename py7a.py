import Image, urllib, StringIO
img = urllib.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read()
i = Image.open(StringIO.StringIO(img))
# Extract every 7th pixel from row 45.
row = [i.getpixel((x, 45)) for x in range(0, i.size[0], 7)]
print row
# Take the R value from all with equal R, G, and B values.
ords = [r for r, g, b, a in row if r == g == b]
# And convert to characters.
print "".join(map(chr, ords))
