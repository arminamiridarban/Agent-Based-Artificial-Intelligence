class Frontier():
    def __init__(self):
        self.frontier = []
    
    def add(self, node):
        self.frontier.append(node)
        
    def empty(self):
        return len(self.frontier) == 0

    def contain_state(self, state):
        return any(node.state == state for node in self.frontier)


class BFS(Frontier):
    def remove(self):
        if self.empty():
            raise Exception("Frontier empty")
        else:
            node = self.frontier.pop(0)
            return node

class DFS(Frontier):
    def remove(self):
        if self.empty:
            raise Exception ("Frontier is empty")
        else:
            self.frontier.pop(-1)


class Node:
    def __init__(self, state, parent, action, cost):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.action = action
    
    def __str__(self):
        return self.state
    
