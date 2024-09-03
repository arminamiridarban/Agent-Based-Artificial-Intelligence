class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables 
        self.domains = domains  
        self.constraints = constraints
        self.assignment = {} 
    
    def is_consistent(self, var, value):
        """Check if assigning 'value' to 'var' is consistent with current assignment."""
        for neighbor in self.constraints[var]:
            if neighbor in self.assignment and self.assignment[neighbor] == value:
                return False
        return True
    
    def select_unassigned_variable(self):
        """Select the next variable to assign using MRV heuristic."""
        unassigned = [v for v in self.variables if v not in self.assignment]
        # Minimum Remaining Values (MRV) heuristic
        return min(unassigned, key=lambda var: len(self.domains[var]))
    
    def order_domain_values(self, var):
        """Order the domain values using LCV heuristic."""
        if var not in self.constraints:
            return self.domains[var]
        # Least Constraining Value (LCV) heuristic
        def count_conflicts(value):
            conflicts = 0
            for neighbor in self.constraints[var]:
                if value in self.domains[neighbor]:
                    conflicts += 1
            return conflicts
        return sorted(self.domains[var], key=count_conflicts)
    
    def forward_checking(self, var, value):
        """Perform forward checking after assigning 'value' to 'var'."""
        inferences = {}
        for neighbor in self.constraints[var]:
            if neighbor not in self.assignment:
                inferences[neighbor] = []
                for neighbor_value in self.domains[neighbor]:
                    if not self.is_consistent(neighbor, neighbor_value):
                        inferences[neighbor].append(neighbor_value)
        # If any variable has an empty domain, return failure
        for neighbor in inferences:
            for value_to_remove in inferences[neighbor]:
                self.domains[neighbor].remove(value_to_remove)
                if len(self.domains[neighbor]) == 0:
                    return False, inferences
        return True, inferences
    
    def undo_inferences(self, inferences):
        """Undo the inferences made by forward checking."""
        for neighbor in inferences:
            self.domains[neighbor].extend(inferences[neighbor])
    
    def backtrack(self):
        """Backtracking search to solve the CSP."""
        if len(self.assignment) == len(self.variables):
            return self.assignment
        
        var = self.select_unassigned_variable()
        for value in self.order_domain_values(var):
            if self.is_consistent(var, value):
                self.assignment[var] = value
                success, inferences = self.forward_checking(var, value)
                
                if success:
                    result = self.backtrack()
                    if result is not None:
                        return result
                
                # Backtrack
                del self.assignment[var]
                self.undo_inferences(inferences)
        
        return None

# Define the regions and their constraints
variables = ['A', 'B', 'C', 'D', 'E']
domains = {var: ['Red', 'Green', 'Blue'] for var in variables}
constraints = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

# Initialize the CSP
csp = CSP(variables, domains, constraints)

# Find the solution using backtracking
solution = csp.backtrack()

# Output the solution
if solution:
    print("Solution found:")
    for region, color in solution.items():
        print(f"{region}: {color}")
else:
    print("No solution exists.")
