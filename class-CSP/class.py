variables = ["C1","C2","C3","C4"]
domains = {var: ["R1","R2","R3"] for var in variables}
constraints = {
    "C1": ["C2", "C3"],
    "C2": ["C1", "C4"],
    "C3": ["C1"],
    "C4": ["C2"]
}


class CSP():
    def __init__(self, variables, domains, constrains):
        self.variables = variables
        self.domains = domains
        self.constrains = constrains
        self.assignment = {}

    def is_consistant(self, var, value):
        x = self.constrains.get(var)
        if x:
            for neighbor in x:
                if neighbor in self.assignment and self.assignment[neighbor] == value:
                    return False
                
        return True
    
    def select_unassigned_variable(self):
        select = [v for v in self.variables if v not in self.assignment]

        return min(select, key=lambda v:len(self.domains[v]))
    
    def order_domain_values(self, var):
        if var not in self.constrains:
            return self.domains[var]
        
        unsort_list = []
        for val in self.domains[var]:
            conflict = 0
            for neighbor in self.constrains[var]:
                if val in self.domains[neighbor]:
                    conflict += 1
            unsort_list.append((val, conflict))
        
        unsort_list.sort(key=lambda x:x[1])
        return [domain for domain,_ in unsort_list]
    
    def forward_checking(self, var, value):
        inferences = {}
        for neighbor in self.constrains[var]:
            if neighbor not in self.assignment:
                inferences[neighbor] = []
                for neighbor_value in self.domains[neighbor]:
                    if not self.is_consistant(neighbor, neighbor_value):
                        inferences[neighbor].append(neighbor_value)
        
        for neighbor in inferences:
            if len(inferences[neighbor]) == 0:
                return False, inferences
        
        return True, inferences

    def undo_inferences(self, inferences):
        for neighbor in inferences:
            self.domains[neighbor].extend(inferences[neighbor])


    def backtracking(self):
        if len(self.assignment) == len(self.variables):
            return self.assignment

        var = self.select_unassigned_variable()
        for value in self.domains[var]:
            if self.is_consistant(var, value):
                self.assignment[var] = value
                success, inferences = self.forward_checking(var, value)

                if success:
                    result = self.backtracking()
                    if result is not None:
                        return result
                
                del self.assignment[var]
                self.undo_inferences(inferences)
    
        return None



csp = CSP(variables,domains,constraints)

solution = csp.backtracking()

if solution:
    print("Solution is:")
    for cls, room in solution.items():
        print(f"{cls}:{room}")

else:
    print("There is no solution")
    