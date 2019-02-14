#to meet all the requirements of the assignment
import time
#output information to file
def outputToFile(toFile):
    fileName = "hillierSudokuOutput.txt"
    f = open(fileName,'a')
    f.write(toFile)

#pass it a function and it will time it
def timeFunction(func):
    timeStart = time.time()
    func()
    timeEnd = time.time()
    total = timeStart - timeEnd
    outputToFile("time to finish:",total)


def puzzleToOutput(puzzle):
    outputToFile('|-----------------------|')#,end='')
    a = 0
    for sublist in puzzle:
        i = 0
        outputToFile("\n| ")#,end="")
        for item in sublist:
            i += 1
            a += 1
            outputToFile(item+" ")#,end='')
            if i % 3 == 0:
                outputToFile("| ")#,end='')

            if a % 27 == 0:
                outputToFile('\n|-------+-------+-------|')#,end='')
        outputToFile("")
