lines = []

def coordInToPoint(coordinate):
	point = coordinate.split(',')
	point[0] = int(point[0])
	point[1] = int(point[1])
	return point

fieldWidth = 0
fieldHeight = 0

with open('day5.in.txt') as file:
	while True:
		line = file.readline()
		if (line == ""):
			break

		line = line.split()
		pointA = coordInToPoint(line[0])
		pointB = coordInToPoint(line[2])
		dx = pointB[0] - pointA[0]
		dy = pointB[1] - pointA[1]

		if (dx < 0):
			dx = -1
		elif (dx > 0):
			dx = 1

		if (dy < 0):
			dy = -1
		elif (dy > 0):
			dy = 1
		
		line = {
			'pointA': pointA,
			'pointB': pointB,
			'dx': dx,
			'dy': dy
		}

		lines.append(line)

		if (max(pointA[0], pointB[0]) > fieldWidth):
			fieldWidth = max(pointA[0], pointB[0])

		if (max(pointA[1], pointB[1]) > fieldHeight):
			fieldHeight = max(pointA[1], pointB[1])
file.close()

# Points are 0-based, but wdth and height are 1-based (screw you this makes sense)
fieldWidth += 1
fieldHeight += 1

field = []
for row in range(0, fieldHeight):
	field.append([])
	for column in range(0, fieldWidth):
		field[row].append(0)

def printField():
	global field, fieldWidth, fieldHeight
	display = ""
	for x in range(0, fieldWidth):
		display += str(x)
	print(display)
	for row in field:
		display = ""
		for val in row:
			if (val == 0):
				display += "."
			else:
				display += str(val)
		print(display)

def getLineDirection(line):
	dx = line['dx']
	dy = line['dy']

	if (dx == 0 and dy == 0):
		return "point"
	elif (dx == 0):
		return "vertical"
	elif (dy == 0):
		return "horizontal"
	return "diagonal"

def samePoint(pointA, pointB):
	return (pointA[0] == pointB[0] and pointA[1] == pointB[1])

def fillLine(line):
	global field
	path = [
		line['pointA'][0],
		line['pointA'][1]
	]

	while (not samePoint(path, line['pointB'])):
		field[path[1]][path[0]] += 1
		path[0] += line['dx']
		path[1] += line['dy']

	field[path[1]][path[0]] += 1 # Don't forget to fill pointB (fencepost issue)

for line in lines:
	lineDirection = getLineDirection(line)
	#if (lineDirection == "vertical" or lineDirection == "horizontal"):
	fillLine(line)
		
print(str(fieldWidth) + " x " + str(fieldHeight))
#printField()

# sum number of locations in field with val >=2
def countDangers(dangerTarget):
	global field
	count = 0
	for row in field:
		for value in row:
			if (value >= dangerTarget):
				count += 1
	return count

print("Dangers: " + str(countDangers(2)))