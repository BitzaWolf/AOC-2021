boards = []

with open('day4.in.txt') as file:
	draws = file.readline()
	draws = draws.split(',')
	draws[len(draws) - 1] = draws[len(draws) - 1].split()[0] # Remove the \n at the end of the line... Not pretty but works
	file.readline() # Eat empty line

	while 1:
		str_row = file.readline()
		if (str_row == ""):
			break

		board = []
		for r in range(0, 5):
			row = str_row.split()
			board.append(row)
			str_row = file.readline()

		boards.append(board)

file.close()

def markBoards(drawnNumber):
	for board in boards:
		for row in board:
			for index in range(0, len(row)):
				number = row[index]
				if (number == drawnNumber):
					row[index] = "" # Mark the number

def isRowWon(row):
	for number in row:
		if (number != ""):
			return False
	return True

def isBoardWon(board):
	for row in board:
		if (isRowWon(row)):
			return True

	for columnIndex in range(0, 5):
		column = [
			board[0][columnIndex],
			board[1][columnIndex],
			board[2][columnIndex],
			board[3][columnIndex],
			board[4][columnIndex]
		]
		if (isRowWon(column)):
			return True

	return False

def checkWinners():
	winningBoards = []

	for index in range(0, len(boards)):
		board = boards[index]
		if (isBoardWon(board)):
			winningBoards.append(index)

	return winningBoards
		
def getBoardSum(board):
	sum = 0
	for row in board:
		for number in row:
			if (number != ""):
				sum += int(number)
	return sum

winningNumber = -1
print("num of boards: " + str(len(boards)))
for draw in draws:
	markBoards(draw)

	# We want the last board, so we're gonna remove winning boards
	# since we're removing boards via index, we have to remove later indices first
	winningBoardIndicies = checkWinners()
	winningBoardIndicies.sort(reverse=True)
	for winningBoardIndex in winningBoardIndicies:
		lastWinner = boards[winningBoardIndex]
		del boards[winningBoardIndex]

	if (len(boards) == 0):
		winningNumber = int(draw)
		break

print("-------------------------")
print(str(getBoardSum(lastWinner)) + " x " + str(winningNumber))
print(getBoardSum(lastWinner) * winningNumber)
