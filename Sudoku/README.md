# Sudoku Puzzle (CSP)

## Overview

This assignment focuses on solving a partially completed **Sudoku** puzzle using constraint satisfaction programming (CSP). The goal is to guide you through applying advanced problem-solving techniques to fill in the missing numbers in the grid, adhering to the standard Sudoku rules.

## Problem Description

Sudoku is a logic-based number puzzle consisting of a 9x9 grid, which is subdivided into nine 3x3 smaller grids. The task is to fill the grid with numbers from 1 to 9 under the following constraints:

- Each number must appear exactly once in each row.
- Each number must appear exactly once in each column.
- Each number must appear exactly once in each of the 3x3 subgrids.

The provided Sudoku puzzle has some pre-filled numbers, while other cells remain blank (denoted as `0`). Your task is to complete the puzzle by filling in the empty cells while respecting the above constraints.

### The Given Sudoku Grid

Here is the Sudoku grid you'll work with, where each `0` represents an empty cell to be filled:

```
[
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
```

## Objectives

1. **Develop a CSP-based solution:** You are expected to implement a **constraint satisfaction problem (CSP)** model to solve the Sudoku grid. The CSP model will:
   - Identify variables (i.e., unfilled cells).
   - Define domains (possible values for each variable).
   - Implement constraints that must be satisfied to ensure the solution follows Sudoku rules.

2. **Apply backtracking with forward-checking:** Use **backtracking search** along with **forward-checking** to efficiently explore and assign values to the grid, while pruning inconsistent options as early as possible.

3. **Heuristic approaches:** Incorporate heuristic techniques like:
   - **Minimum Remaining Values (MRV):** Select variables that have the fewest possible values first.
   - **Least Constraining Value (LCV):** Choose values that impose the least constraint on other variables.

4. **Inference:** Implement an inference mechanism that helps reduce the search space by propagating constraints after each assignment.

## Instructions

1. **Design the CSP Framework:**
   - Define variables as the cells that need to be filled (i.e., where the grid value is `0`).
   - Define the domain for each variable, which consists of the numbers 1 to 9.
   - Specify constraints that ensure the rules of Sudoku are respected (no duplicates in rows, columns, or 3x3 subgrids).

2. **Implement a Solution:**
   - Use backtracking search with forward-checking to explore the assignment of values to variables.
   - Use MRV to select which cell to fill next and LCV to determine the best value to assign to a cell.
   - Implement a method to check whether a value assignment is consistent with the constraints.

3. **Test Your Implementation:**
   - Apply your CSP solver to the provided Sudoku grid.
   - Ensure that the solution is correct by checking that all Sudoku rules are satisfied in the final grid.

## Deliverables

1. **CSP-based Solution:**
   - Write a Python program to solve the provided Sudoku puzzle using the CSP approach outlined above.
   - Ensure that your program outputs the completed Sudoku grid if a solution is found.

## Hints

- Think of each unfilled cell as a variable that needs a value.
- Use sets or lists to represent the domains (possible values) for each variable.
- A valid solution will meet all the constraints of the puzzle, meaning there are no repeated numbers in any row, column, or 3x3 subgrid.
