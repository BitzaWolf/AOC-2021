codes = []

with open('day8.in.txt') as file:
	line = file.readline()
	while (line != ''):
		line = line.split('|')
		entry = {
			'signalPatterns': line[0].split(),
			'outputValues': line[1].split()
		}
		codes.append(entry)
		line = file.readline()
file.close()

"""
7 seg display to code and count

num		segments	not segments	seg count
0		abcefg		d				    6
1		cf			abdeg			2
2		acdeg		bf				   5
3		acdfg		be				   5
4		bcdf		aeg				  4
5		abdfg		ce				   5
6		abdefg		c				    6
7		acf			bdeg			 3
8		abcdefg		-				     7
9		abcdfg		e				    6
"""

def isPatternUnique(signalPattern):
	length = len(signalPattern)
	return (length == 2 or length == 3 or length == 4 or length == 7)

count = 0
for code in codes:
	for pattern in code['outputValues']:
		isUnique = isPatternUnique(pattern)
		if (isUnique):
			count += 1

print(count)

def lettersInCommon(patternA, patternB):
	count = 0
	for i in range(0, len(patternA)):
		for j in range(0, len(patternB)):
			if (patternA[i] == patternB[j]):
				count += 1
	return count

#print(lettersInCommon('abdefg', 'cf'))	 # 1 match, must be 6
#print(lettersInCommon('abcefg', 'cf'))
#print(lettersInCommon('abcdfg', 'cf'))
#print('----------------')
#print(lettersInCommon('abdefg', 'bcdf'))
#print(lettersInCommon('abcefg', 'bcdf'))
#print(lettersInCommon('abcdfg', 'bcdf')) # 4 match, must be 9
#print('----------------')# remaining 6 is a 0
#print(lettersInCommon('acdfg', 'cf')) # 2 match, must be 3
#print(lettersInCommon('acdeg', 'cf'))
#print(lettersInCommon('abdfg', 'cf'))
#print('----------------')
#print(lettersInCommon('acdfg', 'bcdf'))
#print(lettersInCommon('acdeg', 'bcdf')) # 2 match, must be 2
#print(lettersInCommon('abdfg', 'bcdf'))
# remaining is 5

def buildCodex(signalPatterns):
	codex = ['', '', '', '', '', '', '', '', '', '']
	for pattern in signalPatterns:
		if (len(pattern) == 2):
			codex[1] = pattern
		elif (len(pattern) == 3):
			codex[7] = pattern
		elif (len(pattern) == 4):
			codex[4] = pattern
		elif (len(pattern) == 7):
			codex[8] = pattern

	for pattern in signalPatterns:
		if (len(pattern) == 5):
			commonLetters = lettersInCommon(pattern, codex[1])
			if (commonLetters == 2):
				codex[3] = pattern
				continue
			commonLetters = lettersInCommon(pattern, codex[4])
			if (commonLetters == 2):
				codex[2] = pattern
			else:
				codex[5] = pattern
		elif (len(pattern) == 6):
			commonLetters = lettersInCommon(pattern, codex[1])
			if (commonLetters == 1):
				codex[6] = pattern
				continue
			commonLetters = lettersInCommon(pattern, codex[4])
			if (commonLetters == 4):
				codex[9] = pattern
			else:
				codex[0] = pattern
	return codex

def isAnagram(patternA, patternB):
	if (len(patternA) != len(patternB)):
		return False

	matches = lettersInCommon(patternA, patternB)
	return (matches == len(patternA))

def translateCode(codex, values):
	output = ''
	for val in values:
		for number in range(0, 10):
			if (isAnagram(codex[number], val)):
				output += str(number)
				continue
	return output

values = []
count = 0
for code in codes:
	codex = buildCodex(code['signalPatterns'])
	value = int(translateCode(codex, code['outputValues']))
	count += value
	values.append(value)
#print(values)
print(count)
		
"""
One solution is to run the data and calculate the correct spot for each diode, which is possible, but it might be unneccesary.
we know 1, 4, 7, 8
For example, '6' is just missing 'c', and 'c' is also in '1' which know.
So of all the 6-length patterns, we know '6' is the only digit that has only one letter also in '1'
	'0' and '9' (the other 6-digit numbers) have two letters in '1'
Now we know 1, 4, 6, 7, 8
'0' and '9' are remaining of the 6's. '4' has a 'd' and no 'e', so '9' will share all letters with '4' while '0' will only share two letters from '4'.
Now we know 0, 1, 4, 6, 7, 8, 9

Only left are the five-length patterns.
'3' is the only digit that has the two letters also in '1'
That leaves 2 and 5.
2 will have all but one of its letters represented in 
2 will have all but one of its letters represented in 9.
5 will have all but two of its letters represented in 9.

That's it! 0123456789

We could do this, but is this really better? We could also decode to get which diode each letter should represent then rebuild the correct digit.

Convert each pattern to a binary: 00abcdef

we can isolate 'a' from 7 XOR 1

We can can singles by NOTing the 6-length patterns
We can guarantee 'c', 'd', and 'e'

'f' is '1' NOT 'c'
'b' is '4' NOT 'cdf'
the last one is 'g'

Now we have a codex to map the input pattern to its proper number, then just display it.

Let's run through an example:
acedgfb cdfbe   gcdfa   fbcad   dab		cefabd  cdfgeb  eafb    cagedb  ab
1111011 0111110 1011011 1111010 1101000 1111110 0111111 1100110 1111101 1100000
8								7						4				1

a = 1101000 XOR 1100000  -->  0001000
"""