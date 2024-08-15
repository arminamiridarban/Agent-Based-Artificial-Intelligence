# Problem: Optimal Pathfinding with A* Algorithm

### Scenario
You are tasked with implementing an emergency response system to guide a rescue team through a hazardous environment to save a civilian trapped in a burning building. The building's floor plan is represented by a 2D grid, where each cell can either be clear, on fire, or marked as the start or civilian’s location.

```python
grid = [
    ['S',  0,  1,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  1,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  1,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  1,  1,  1,  1,  1,  1,  1,  1 ],
    [  0,  0,  1,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  1,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  1,  0,  0,  0,  0,  0,  0, 'C'],
]
```

- 'S' marks the start point of the rescue team.
- 'C' marks the civilian's location.
- Cells marked with '1' represent flames. Moving through these cells incurs a higher cost.
- Cells marked with '0' are safe to move through, with a standard movement cost.

### Task

Using the A* search algorithm, your goal is to determine the most cost-effective path for the rescue team to reach the civilian.

## Requirements:

1. Algorithm Implementation:
- Implement the A* search algorithm to navigate the grid.
- Use the Manhattan Distance as the heuristic to estimate the cost from any node to the civilian.
- Accurately calculate and update the total cost (F = G + H) for each node, where:
   - G is the cost from the start node to the current node.
   - H is the heuristic estimate from the current node to the civilian's location.

2. Cost Considerations:
- Moving through a clear cell ('0') has a cost of 1.
- Moving through a cell on fire ('1') has a cost of 5.
- The algorithm must account for these costs when determining the optimal path.

3. Deliverables:
- A list of coordinates representing the optimal path from 'S' to 'C'.
- The total cost associated with this path.

### Sample Output
Assuming the optimal path was found, your program should output something like:

- Path: [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (6,8), (6,9)]
- Total Cost: X (Where X represents the sum of costs along the path)

### Additional Guidelines
- Ensure that your algorithm handles edge cases, such as when no viable path exists.
- Remember to handle obstacles (fire) properly in your implementation, considering the higher movement cost associated with fire.