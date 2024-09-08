### Problem: Sudoku Puzzle (CSP)

**Description**:
A Sudoku puzzle is a 9x9 grid where each cell must be filled with a digit from 1 to 9. The grid is divided into 9 smaller 3x3 subgrids. The goal is to fill the grid in such a way that:

- Each row contains the digits 1 to 9 without repetition.
- Each column contains the digits 1 to 9 without repetition.
- Each 3x3 subgrid contains the digits 1 to 9 without repetition.

### Constraints:
- Each cell in the grid is a variable.
- The domain of each cell is the set of values `{1, 2, 3, 4, 5, 6, 7, 8, 9}`.
- The constraints are:
  1. No row contains the same number more than once.
  2. No column contains the same number more than once.
  3. No 3x3 subgrid contains the same number more than once.

### Example:
Here is an example of a partially filled Sudoku puzzle:

```
5 3 _  _ 7 _  _ _ _
6 _ _  1 9 5  _ _ _
_ 9 8  _ _ _  _ 6 _
8 _ _  _ 6 _  _ _ 3
4 _ _  8 _ 3  _ _ 1
7 _ _  _ 2 _  _ _ 6
_ 6 _  _ _ _  2 8 _
_ _ _  4 1 9  _ _ 5
_ _ _  _ 8 _  _ 7 9
```

In this grid:
- Empty cells are represented by `_` (these are variables).
- Your task is to fill these empty cells while respecting the constraints.

### Task:
1. **Model the Sudoku puzzle as a CSP problem**.
2. Implement the backtracking search to solve the puzzle.
3. Use appropriate constraint propagation methods (like AC-3) to reduce the search space.
4. Return the solution (a completely filled 9x9 grid) that satisfies all the constraints.
