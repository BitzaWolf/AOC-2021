heightmap = []

with open('day9.in.txt') as file:
	line = file.readline()
	while (line != ''):
		line = line.strip()
		row = []
		for i in range(0, len(line)):
			row.append(int(line[i]))
		heightmap.append(row)
		line = file.readline()
file.close()

width = len(heightmap[0])
height = len(heightmap)

def isLowPoint(x, y):
	global width, height

	me = heightmap[y][x]
	top = 99
	right = 99
	bottom = 99
	left = 99

	if (x > 0):
		left = heightmap[y][x - 1]
	if (x < width - 1):
		right = heightmap[y][x + 1]
	if (y > 0):
		top = heightmap[y - 1][x]
	if (y < height - 1):
		bottom = heightmap[y + 1][x]

	return (me < top and me < right and me < bottom and me < left)

def getRiskLevel(x, y):
	return heightmap[y][x] + 1

totalRisk = 0
lowPointLocations = []
for y in range(0, height):
	for x in range(0, width):
		if (isLowPoint(x, y)):
			totalRisk += getRiskLevel(x, y)
			lowPointLocations.append([x, y])

print(totalRisk)

def findBasin(coordinatesChecked, x, y):
	#print("\tChecking (%d, %d)" % (x, y))

	global width, height

	coordsAsString = str(x) + str(y)
	#print("\tRisk Level: %d" % getRiskLevel(x, y))
	#print("\tChecked: " + str(coordinatesChecked.get(coordsAsString)))
	if (getRiskLevel(x, y) == 10 or coordinatesChecked.get(coordsAsString) != None):
		#print("\t\tSkipping!")
		return

	coordinatesChecked[coordsAsString] = 1
	if (x > 0):
		findBasin(coordinatesChecked, x - 1, y)
	if (x < width - 1):
		findBasin(coordinatesChecked, x + 1, y)
	if (y > 0):
		findBasin(coordinatesChecked, x, y - 1)
	if (y < height - 1):
		findBasin(coordinatesChecked, x, y + 1)

def calculateBasinSize(x, y):
	#print("Searching point (%d, %d)..." % (x, y))

	coordinatesChecked = {}
	findBasin(coordinatesChecked, x, y)

	#print("Size: %d" % len(coordinatesChecked))
	return len(coordinatesChecked)

basinSizes = []	
for location in lowPointLocations:
	size = calculateBasinSize(location[0], location[1])
	basinSizes.append(size)

basinSizes = sorted(basinSizes)
puzzleAnswer = basinSizes[-1] * basinSizes[-2] * basinSizes[-3]
print(puzzleAnswer)
#print(basinSizes)