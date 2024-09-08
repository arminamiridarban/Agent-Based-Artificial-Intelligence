variables = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']

domains = {var : {'red', 'green', 'blue'} for var in variables}

constraints = {
    'WA': {'NT'},
    'NT': {'Q', 'SA', 'WA'},
    'SA': {'Q', 'NSW', 'NT'},
    'NSW': {'V', 'SA'},
    'V': {'NSW'},
    'Q': {'NT', 'SA'},
    'T': set()  # Tasmania has no constraints
}

class CSP():
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.assignment = {}

    def is_consistant(self, var, value):
        for neighbor in self.constraints.get(var, []):
            if neighbor in self.assignment and self.assignment[neighbor] == value:
                return False
            
        return True
    
    def select_unassigned_variable(self):
        unassigned = [var for var in self.domains if var not in self.assignment]
        
        return min(unassigned, key=lambda var: len(self.domains[var]))
    
    def order_domain_values(self, var):
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
    
    def revise(self, var1, var2):
        revised = False
        for val1 in set(self.domains[var1]):
            if all(val1 == val2 for val2 in self.domains[var2]):
                self.domains[var1].remove(val1)
                revised = True

        return revised
    
    def ac3(self):
        queue = [(X, Y) for X in self.constraints for Y in self.constraints[X]]

        while queue:
            (X, Y) = queue.pop(0)
            if self.revise(X, Y):
                if not self.domains[X]:
                    return False
                for Z in self.constraints.get(X, []):
                    if Z != Y:
                        queue.append((Z, X))
        return True
    
    def backtracking_search(self):
        if not self.ac3():
            return None
        return self.backtracking()
    
    def backtracking(self):
        if len(self.assignment) == len(self.variables):
            return self.assignment
        
        var = self.select_unassigned_variable()
        for value in self.order_domain_values(var):
            if self.is_consistant(var, value):
                self.assignment[var] = value
                result = self.backtracking()
                if result:
                    return result
                del self.assignment[var]
        return None

csp = CSP(variables, domains, constraints)
print(csp.backtracking())