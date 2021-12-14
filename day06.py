fishes = []
newFishes = []
for x in range(0, 9):
	fishes.append(0)
	newFishes.append(0)

DAYS_TO_SIMULATE = 256

with open('day6.in.txt') as file:
	ages = file.readline().split(',')
	for age in ages:
		age = int(age)
		fishes[age] += 1
file.close()

def resetNewFishes():
	global newFishes
	for x in range(0, 9):
		newFishes[x] = 0

for dayNumber in range(1, DAYS_TO_SIMULATE + 1):
	resetNewFishes()
	newFishes[8] = fishes[0]
	newFishes[6] = fishes[0]
	for index in range(1, 9):
		fishes[index - 1] = fishes[index]
	fishes[8] = newFishes[8]
	fishes[6] += newFishes[6]
	#print("Day " + str(dayNumber) + " | " + str(len(fishes)))
	#print(fishes)

count = 0
for fishCount in fishes:
	count += fishCount
print(count)