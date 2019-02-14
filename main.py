import solver,output,copy,time
def main():
    getPuzzle("./puzzles.txt")
    # solver.backTrack(thisPuzzle)

def getPuzzle(fileName):
    with open(fileName) as f:
        content = f.readline()
        while content:
            temp = list(content)
            puzzle = []
            i = 0
            while i < len(temp):
                puzzle.append(temp[i:i+9])
                i += 9
            #create 2 copies of the puzzle
            copy1 = copy.deepcopy(puzzle)
            copy2 = copy.deepcopy(puzzle)
            #time the function
            output.outputToFile("Starting Puzzle\n")
            output.puzzleToOutput(copy1)

            timeStart1 = time.time()
            solver.backTrack(copy1)
            timeEnd1 = time.time()
            total1 = timeEnd1 - timeStart1

            timeStart2 = time.time()
            solver.forwardCheck(copy2)
            timeEnd2 = time.time()
            total2 = timeEnd2 - timeStart2
            output.outputToFile("Ending Puzzle\n")
            output.puzzleToOutput(copy1)
            output.outputToFile("BackTrack-Time to finish:" + str(total1) + "\n")
            output.outputToFile("ForwardCheck-Time to finish:" + str(total2) + "\n")





            #
            # output.timeFunction(solver.backTrack(copy1))
            # print(output.puzzleToOutput(copy1))
            # # print("bt start",copy1)
            # # # output.outputToFile(copy1)
            # # solver.backTrack(copy1)
            # # print("bt end",copy1)
            # # print("fc start",copy2)
            # # solver.forwardCheck(copy2)
            # # print("fc end",copy2)
            # # # print("end  ",puzzle)
            content = f.readline()

main()
