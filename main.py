import solver
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
            # solver.backTrack(puzzle)
            solver.forwardCheck(puzzle.copy())
            print("end  ",puzzle)
            content = f.readline()

main()
