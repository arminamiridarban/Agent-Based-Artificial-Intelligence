sudoku_puzzle = [
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
        self.variables = self.gen_vars()
        self.domains = self.gen_domains()
        self.constraints = self.gen_const()
        self.assignment = {}


    def gen_vars(self):
        var_dict = {}
        for row_index, row in enumerate(sudoku_puzzle):
            for col_index, col in enumerate(row):
                if col == 0:
                    var_dict[(row_index, col_index)] = None
                else:
                    var_dict[(row_index, col_index)] = col
        
        return var_dict
    
    def gen_const(self):
        consts = {}
        for row_index, row in enumerate(sudoku_puzzle):
            for col_index, col in enumerate(row):
                consts[(row_index, col_index)] = set()
                for c in range(9):
                    if col_index != c:
                        consts[(row_index, col_index)].add((row_index, c))
                
                for r in range(9):
                    if row_index != r:
                        consts[(row_index, col_index)].add((r, col_index))

                start_row, start_col = 3 * (row_index // 3), 3 * (col_index // 3)
                for r in range(start_row, start_row + 3):
                    for c in range(start_col, start_col + 3):
                        if r != row_index or c != col_index:
                            consts[(row_index, col_index)].add((r, c))
        return consts
    
    def gen_domains(self):
        domains = {}
        for row_index, row in enumerate(sudoku_puzzle):
            for col_index, col in enumerate(row):
                if col == 0:
                    domains[(row_index, col_index)] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
                else:
                    domains[(row_index, col_index)] = {col}
        return domains
    
    def select_unassigned_variable(self):
        unassigned = [var for var in self.domains if var not in self.assignment]

        return min(unassigned, key=lambda x:len(self.domains[x]))
    
    def is_consistent(self, var, val):
        for neighbor in self.constraints[var]:
            if neighbor in self.assignment and self.assignment[neighbor] == val:
                return False
        return True
    
    def order_domains_value(self, var):
        ODV = []
        for val in self.domains[var]:
            conflicts = 0
            for neighbor in self.constraints[var]:
                if val in self.domains[neighbor]:
                    conflicts +=1
            
            ODV.append((val, conflicts))
        
        ODV = [val for val, _ in sorted(ODV, key=lambda x:x[1])]
        
        return ODV
    
    def revise(self, var1, var2):
        revised = False
        for val1 in set(self.domains[var1]):
            if not any(val2 != val1 for val2 in self.domains[var2]):
                self.domains[var1].remove(val1)
                revised = True
        return revised


    def ac3(self):
        queue = [(var1, var2) for var1 in self.constraints for var2 in self.constraints[var1]]
        while queue:
            var1, var2 = queue.pop(0)
            if self.revise(var1, var2):
                if not self.domains[var1]:
                    return False
                for var3 in self.constraints[var1]:
                    if var3 != var2:
                        queue.append((var3, var1))
        return True
                
            
    def backtrack(self):
        if len(self.assignment) == len(self.variables):
            return self.assignment
        var = self.select_unassigned_variable()
        for val in self.order_domains_value(var):
            if self.is_consistent(var, val):
                self.assignment[var] = val
                result = self.backtrack()
                if result:
                    return result
                del self.assignment[var]
        return None


    def backtracksearch(self):
        if not self.ac3():
            return None
        return self.backtrack()


csp = CSP(sudoku_puzzle)

solution = csp.backtracksearch()
mat = sudoku_puzzle 
if solution:
    for i, j in solution.items():
        mat[i[0]][i[1]] = j

    for row in mat:
        print(row)
else:
    print("There is no solution")
