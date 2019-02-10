#recursive backtrack algo
def backTrack(puzzle):
    #current working location
    freeSpace = [0,0]
    if not findEmpty(puzzle,freeSpace):
        return True

    for number in range(1,10):
        # print(number)
        if checkLocation(puzzle,freeSpace[0],freeSpace[1],str(number)):
            puzzle[freeSpace[0]][freeSpace[1]] = str(number)
            if backTrack(puzzle):
                return True
            puzzle[freeSpace[0]][freeSpace[1]] = '0'
    return False

#forward checking algorithm
def forwardCheck(puzzle):
    # current working location
    freeSpace = [0, 0]
    if not findEmpty(puzzle, freeSpace):
        return True

    #check here for the domain
    domain = getAllowedValues(puzzle,freeSpace)

    #check if the domain is empty
    if not domain:
        return False

    for number in domain:
        if checkLocation(puzzle,freeSpace[0],freeSpace[1],str(number)):
            puzzle[freeSpace[0]][freeSpace[1]] = str(number)
            if forwardCheck(puzzle):
                return True
            puzzle[freeSpace[0]][freeSpace[1]] = '0'
    return False

#checks the allowed values for the current position
def getAllowedValues(puzzle,freeSpace):
    domain = []

    for num in range(1,10):
        if not used(puzzle,freeSpace[0],freeSpace[1],str(num)):
            domain.append(num)
    return domain


#find a empty position in the puzzle
def findEmpty(puzzle,freeSpace):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == '0':
                freeSpace[0],freeSpace[1] = row, col
                return True
    return False

#finds all the empty spaces in the puzzle
#including the location
def findAllEmpty(puzzle,freeSpaces):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == '0':
                freeSpaces.append([row,col])


#check to see if it is ok to put the number at location
def checkLocation(puzzle,row,col,number):
    return not used(puzzle,row,col,number) and not usedBox(puzzle,row-row%3,col-col%3,number)


#see if the number your trying to use has been used in current row or col.
#might have to split this up?
def used(puzzle,row,col,number):
    for i in range(0,9):
        if puzzle[row][i] == number or puzzle[i][col] == number:
            return True
    return False

#see if the number has been used in the 3x3 box
def usedBox(puzzle,row,col,number):
    for i in range(3):
        for j in range(3):
            if puzzle[i+row][j+col] == number:
                return True
    return False


