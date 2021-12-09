
average = 0

with open('day7.in.example.txt') as file:
	positions = file.readline().split(',')
	crabsAtThisPosition = {}
	highestPosition = 0
	for index in range(0, len(positions)):
		pos = int(positions[index])
		positions[index] = pos
		average += pos

		if (crabsAtThisPosition.get(pos) == None):
			crabsAtThisPosition[pos] = 1
		else:
			crabsAtThisPosition[pos] += 1

		highestPosition = max(highestPosition, pos)
file.close()

average = average / len(crabsAtThisPosition)
print("Average: %f" % average)

def printCrabsAtThisPosition(crabsAtThisPosition):
	for pos in range(0, highestPosition + 1):
		count = crabsAtThisPosition.get(pos)
		if (count == None):
			count = 0
		print("pos %d: %d" % (pos, count))

def calcMedian(crabsAtThisPosition):
	lowPosition = 0
	highPosition = highestPosition

	while (lowPosition < highPosition):
		while (lowPosition < highPosition and crabsAtThisPosition.get(lowPosition) == None):
			lowPosition += 1
		if (lowPosition < highPosition):
			crabsAtThisPosition[lowPosition] -= 1
			if (crabsAtThisPosition[lowPosition] == 0):
				del crabsAtThisPosition[lowPosition]
		while (lowPosition < highPosition and crabsAtThisPosition.get(highPosition) == None):
			highPosition -= 1
		if (lowPosition < highPosition):
			crabsAtThisPosition[highPosition] -= 1
			if (crabsAtThisPosition[highPosition] == 0):
				del crabsAtThisPosition[highPosition]
	#printCrabsAtThisPosition(crabsAtThisPosition)
	for key in crabsAtThisPosition.keys():
		median = key
	return median
		

median = calcMedian(crabsAtThisPosition.copy())
#print(median)
#printCrabsAtThisPosition(crabsAtThisPosition)

def calcFuelToMoveToPosition(crabsAtThisPosition, position, newFuelCost = False):
	fuel = 0
	for pos in range(0, highestPosition + 1):
		numberOfCrabs = crabsAtThisPosition.get(pos)
		if (numberOfCrabs == None):
			continue

		if (newFuelCost):
			distance = abs(pos - position)
			distanceCost = (pow(distance, 2) + distance) / 2 # "nth triangle number". Does 1 + 2 + 3 + 4 + ... + n
			fuel += distanceCost * numberOfCrabs
		else:
			fuel += numberOfCrabs * abs(pos - position)

	return fuel

print("Median: %f" % median)
print("Fuel cost to move to %d: %d" % (median, calcFuelToMoveToPosition(crabsAtThisPosition, median)))
# 332 357353 (average is 761.276827)



# This weighting system is a stab in the dark.
# Searching for the median is good.
# What we need is a way to re-visualize the distribution of crabs to account for the new fuel costs.
# Median works assuming 1 away is the same. What if the distribution was such that 
# Can we just naively check each position? Lol... I think this is honestly the best way to go about it.
# Yes it's slow, but trying to transform the data to account for such odd moving costs and then find the median of that is very difficult.

"""
middlePosition = (highestPosition + 1) / 2
print(middlePosition)
crabsAtThisPositionWeightedByCost = {}

for pos in crabsAtThisPosition.keys():
	distanceFromMiddlePosition = abs(middlePosition - pos)
	weight = (pow(distanceFromMiddlePosition, 2) + distanceFromMiddlePosition) / 2
	crabsAtThisPositionWeightedByCost[pos] = crabsAtThisPosition[pos] * weight
	print("pos(%d) | Distance from middle: %d | weight: %d" % (pos, distanceFromMiddlePosition, weight))
	
median = calcMedian(crabsAtThisPositionWeightedByCost.copy())
print(median)
printCrabsAtThisPosition(crabsAtThisPositionWeightedByCost)

print("Fuel cost to move to %d: %d" % (median, calcFuelToMoveToPosition(crabsAtThisPosition, median, True)))
print("Fuel cost to move to %d: %d" % (5, calcFuelToMoveToPosition(crabsAtThisPosition, 5, True)))
"""



cheapestFuel = 999999999999999999
cheapestFuelPosition = -1
for pos in range(0, highestPosition + 1):
	cost = calcFuelToMoveToPosition(crabsAtThisPosition, pos, True)
	#print("%d --> %d" % (pos, cost))
	if (cost < cheapestFuel):
		cheapestFuel = cost
		cheapestFuelPosition = pos

print("Fuel cost to move to %d: %d" % (cheapestFuelPosition, cheapestFuel))
# Correct answer is position 489 and fuel 104822130
# Still slow to process, but it does work. There must be a better way! The median was a cool trick.