# My Python Sodoku Solver

```python
def isLegal(puzzle, i, j, k):
    # Test row
    for a in range(9):
        if puzzle[i][a] == k:
            return False
    for a in range(9):
        if puzzle[a][j] == k:
            return False
    group_i = i//3
    group_j = j//3
    base_i = group_i * 3
    base_j = group_j *3
    for a in range(3):
        for b in range(3):
            if puzzle[base_i + a][base_j + b] == k:
                return False
    return True
            

def findFirstEmpty(puzzle):
    i = 0
    j = 0
    for i in range(9):
        row = puzzle[i]
        for j in range(9):
            if row[j] == 0:
                return (i, j)
    
    # If everythign is filled, return (-1, -1)
    return (-1,-1)



def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    

    i, j = findFirstEmpty(puzzle)
    
    
    # if full, we found the answer
    if i == -1:
        return puzzle

    for k in range(1, 10):
        if isLegal(puzzle, i, j, k):
            tmp = [x[:] for x in puzzle]
            tmp[i][j] = k
            tmp = sudoku(tmp)
            if tmp is not None:
                return tmp
        
    return None
```

Test cases:
```
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]

puzzle2 = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,0]]
```
