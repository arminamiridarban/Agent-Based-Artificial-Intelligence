from util import DFS , BFS, Node


roads_small= {
    'Andria': ['Corato', 'Trani'],
    'Corato': ['Ruvo', 'Trani', 'Andria', 'Altamura'],
    'Altamura': ['Corato', 'Ruvo', 'Modugno'],
    'Ruvo': ['Corato', 'Bisceglie', 'Terlizzi', 'Altamura'],
    'Terlizzi': ['Ruvo', 'Molfetta', 'Bitonto'],
    'Bisceglie': ['Trani', 'Ruvo', 'Molfetta'],
    'Trani': ['Andria', 'Corato', 'Bisceglie'],
    'Molfetta': ['Bisceglie', 'Giovinazzo', 'Terlizzi'],
    'Giovinazzo': ['Molfetta', 'Modugno', 'Bari', 'Bitonto'],
    'Bitonto': [ 'Modugno', 'Giovinazzo', 'Terlizzi'],
    'Modugno': ['Bitonto', 'Giovinazzo', 'Bari', 'Altamura'],
    'Bari': ['Modugno', 'Giovinazzo']
}
    

def main():
    start = "Andria"
    target = "Terlizzi"

    if start == target:
        return Exception("Target found")
    
    frontier = BFS()
    node = Node(state=start, parent=None, action=None, cost=None)
    frontier.add(node)
    action = []
    checked_states = []

    while True:
        if frontier.empty():
            raise Exception("There is no solution")
        
        node = frontier.remove()

        action.append(node.state)
        
        if node.state == target:
            print("Finished")
            action.reverse()
            return action
        
        checked_states.append(node.state)

        for state in roads_small[node.state]:
            if state not in checked_states:
                child = Node(state=state, action=None, parent=node, cost=None)
                frontier.add(child)

if __name__ == "__main__":
    result = main()
    if result:
        print(result)
        