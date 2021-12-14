BYTE_SIZE = 12 #8043063 too high

def byteToDec(byte):
	val = 0
	for index in range(0, BYTE_SIZE):
		val += int(byte[index]) * pow(2, BYTE_SIZE - index - 1)
	return val

with open('day3.in.txt') as file:
	report = file.readlines()

#report = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

counts = []
for x in range(0, BYTE_SIZE):
	counts.append([0, 0])
mostCommon = ""
leastCommon = ""
equal = ""

def calcCounts(report):
	global counts, mostCommon, leastCommon, equal
	mostCommon = ""
	leastCommon = ""
	equal = ""
	for x in range(0, BYTE_SIZE):
		counts[x][0] = 0
		counts[x][1] = 0

	for byte in report:
		for index in range(0, BYTE_SIZE):
			bitVal = int(byte[index])
			counts[index][bitVal] += 1

	for count in counts:
		mostCommon = mostCommon + str(int(count[1] > count[0]))
		leastCommon = leastCommon + str(int(count[1] < count[0]))
		equal = equal + str(int(count[1] == count[0]))

calcCounts(report)
power = byteToDec(mostCommon) * byteToDec(leastCommon)
print("power:" + str(power))

reportCopy = report[:]
log = ""

for bitPosition in range(0, BYTE_SIZE):
	if (len(reportCopy) == 1):
		break
	calcCounts(reportCopy)
	isEqual = bool(int(equal[bitPosition]))
	number = mostCommon[bitPosition]
	if (isEqual):
		number = "1"

	log += "		Bit Position " + str(bitPosition) + " | equal? " + str(isEqual) + " | number: " + number + "(" + str(counts[bitPosition][0]) + "/" + str(counts[bitPosition][1]) + ") | len:" + str(len(reportCopy)) + "\n"
	reportCopy = sorted(reportCopy, key=lambda byte: byte[bitPosition])
	found = -1
	for index in range(0, len(reportCopy)):
		log += reportCopy[index]
		if (found == -1 and reportCopy[index][bitPosition] == "1"):
			found = index
			break
	log += "			index: " + str(found) + "\n"
	if (number == "0"):
		reportCopy = reportCopy[:found]
	else:
		reportCopy = reportCopy[found:len(reportCopy)]

		
oxy = byteToDec(reportCopy[0])
print("oxy:" + str(oxy) + "(" + reportCopy[0][0:BYTE_SIZE] + ") | " + str(len(reportCopy)))
reportCopy = report[:]

for bitPosition in range(0, BYTE_SIZE):
	if (len(reportCopy) == 1):
		break
	calcCounts(reportCopy)
	isEqual = bool(int(equal[bitPosition]))
	number = leastCommon[bitPosition]
	if (isEqual):
		number = "0"

	log += "		Bit Position " + str(bitPosition) + " | equal? " + str(isEqual) + " | number: " + number + "(" + str(counts[bitPosition][0]) + "/" + str(counts[bitPosition][1]) + ") | len:" + str(len(reportCopy)) + "\n"
	reportCopy = sorted(reportCopy, key=lambda byte: byte[bitPosition])
	found = -1
	for index in range(0, len(reportCopy)):
		log += reportCopy[index]
		if (found == -1 and reportCopy[index][bitPosition] == "1"):
			found = index
			break
	log += "			index: " + str(found) + "\n"
	if (number == "0"):
		reportCopy = reportCopy[:found]
	else:
		reportCopy = reportCopy[found:len(reportCopy)]

	
	
co2 = byteToDec(reportCopy[0])
print("CO2:" + str(co2) + "(" + reportCopy[0][0:BYTE_SIZE] + ") | " + str(len(reportCopy)))

with open('day3.log.txt', 'w') as file:
	file.write(log)

print("Life support:" + str(co2 * oxy))