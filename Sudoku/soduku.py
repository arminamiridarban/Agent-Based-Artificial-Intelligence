sudoku_grid = [
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

class CSP():
    def __init__(self, grid):
        self.domains = self.init_domain(grid)
        self.constrains = self.init_constrains()
        self.variables = [(r, c) for r in range(9) for c in range(9)]
        self.assignment = self.init_assignment(grid)

    # Defining the domains
    def init_domain(self, grid):
        domains = {}
        for r in range(9):
            for c in range(9):
                if grid[r][c] == 0:
                    domains[(r, c)] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
                else:
                    domains[(r, c)] = {grid[r][c]}
        
        return domains

    # Defining the constrains
    def init_constrains(self):
        constrains = {}
        for r in range(9):
            for c in range(9):
                constrains[(r, c)] = set()

                for col in range(9):
                    if col != c:
                        constrains[(r, c)].add((r, col))

                for row in range(9):
                    if row != r:
                        constrains[(r, c)].add((row, c))

                start_row, start_col = 3 * (r // 3), 3 * (c // 3)
                for row in range(start_row, start_row+3):
                    for col in range(start_col, start_col + 3):
                        if row != r or col != c:
                            constrains[(r, c)].add((row, col))

        return constrains
        
    # Defining the assignment
    def init_assignment(self, grid):
        assignment = {}
        for r in range(9):
            for c in range(9):
                if grid[r][c] != 0:
                    assignment[(r, c)] = grid[r][c]
        
        return assignment
                
    # Select a variable if its not assigned
    def select_unsigned_var(self):
        x = [var for var in self.domains if var not in self.assignment]
        return min(x, key=lambda x:len(self.domains[x]))

    # Check assignment for all constraints of var if there is already an items assigned with value
    def is_consistant(self, var, val):
        for v in self.constrains[var]:
            if v in self.assignment and self.assignment[v] == val:
                return False
        return True

    # Returns a list of values which affect less if we assign something to a variable
    def order_domain_values(self, var):
        ODV = []
        for value in self.domains[var]:
            conflict = 0
            for neighbor in self.constrains[var]:
                if value in self.domains[neighbor]:
                    conflict += 1
            ODV.append((value, conflict))
        
        ODV.sort(key=lambda x:x[1])

        return [val for val,_ in ODV]

    # Checks all of the constrains of var if we assign value to var, their domain is empty
    def forward_checking(self, var, value):
        inferences = {}
        for neighbor in self.constrains[var]:
            if value in self.domains[neighbor]:
                if neighbor not in inferences:
                    inferences[neighbor] = set()
                inferences[neighbor].add(value)
                self.domains[neighbor].remove(value)
                
                if len(self.domains[neighbor]) == 0:
                    return False

        return inferences
        
    # Re-assign the values which is removed from all items domain
    def undo_inference(self, inferences):
        for var, removed_values in inferences.items():
            self.domains[var].update(removed_values)

    # Main function to solve the problem
    def backtracking(self):
        if len(self.assignment) == len(self.variables):
            return self.assignment
        
        var = self.select_unsigned_var()

        for value in self.order_domain_values(var):
            if self.is_consistant(var, value):
                self.assignment[var] = value

                inferences = self.forward_checking(var, value)

                if inferences != False:
                    result = self.backtracking()
                    if result is not None:
                        return result

                self.undo_inference(inferences)
                del self.assignment[var]

        return None


csp = CSP(sudoku_grid)

solution = csp.backtracking()

if solution:
    print("Solution is:")
    for (row, col), value in solution.items():
        sudoku_grid[row][col] = value

    for row in sudoku_grid:
        print(row)

else:
    print("No solution")