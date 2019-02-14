# Sudoku Solver #

Assignment for CPSC 371 that will solve sudoku puzzles

# Puzzle notes #
All the puzzles are stored in the "puzzles.txt" file and are read from there. That means that 
you can add your own puzzles to solve.

There were some student puzzles that needed to be changed to be solved. 
- Puzzle 2 has an issue where there were two 9's in one row. Fixed by changing them both to 0
- Puzzle 3 line 8 had a 9 that looks like a 4
- Puzzle 4 has an unknown issue, so currently is unsolvable. 

All the output including times, puzzles and solutions, will be in the file "hillerSudokuOutput.txt"

# Complexity Analysis #
Im going to do this by a rough method by method basis
#### Methods ####
```
getAllowedValues = n
findEmpty = n^2
findAllEmpty = n^2
checkLocation = used + usedBox = n + n^2
used = n
usedBox = n^2
```
* BackTracking
    * findEmpty
    * checkLocation 
    * Total = 2n^2 + n 

* ForwardChecking
    * findEmpty 
    * checkLocation
    * Total = 2n^2 + n


Although the two methods have the same Complexity Forward checking will be faster since It
only goes through the domain which will be equal or smaller to the domain of the backtracking method