### Advanced A* Search Example:

#### **Scenario:**
You are tasked with navigating a robot through a complex 8x8 grid to reach a goal. The grid contains different types of terrain, each with a different movement cost, as well as blocked cells. The robot can move in four directions (up, down, left, right).

#### **Grid Layout:**
- **S** = Start
- **G** = Goal
- **#** = Blocked (Impassable)
- **.** = Normal terrain (cost = 1)
- **~** = Water terrain (cost = 3)
- **^** = Mountain terrain (cost = 5)

The movement cost is based on the type of terrain you move into. You need to implement A* to find the shortest path considering both terrain costs and heuristic estimates.

**Grid:**
```
S  .  .  .  #  .  .  G
.  #  .  ~  .  .  #  .
.  .  ~  ^  .  .  ~  .
.  #  .  .  .  #  .  .
~  .  ^  #  .  .  .  .
.  .  .  .  .  ~  .  .
.  .  #  .  #  .  #  .
.  .  .  .  .  .  .  .
```

#### **Start Position:** (0, 0)
#### **Goal Position:** (0, 7)
#### **Blocked Cells:** Represented by `#`, impassable
#### **Movement Costs:**
- Normal terrain (`.`): 1
- Water (`~`): 3
- Mountain (`^`): 5

#### **Task:**
1. Implement the A* algorithm to find the shortest path from `S` to `G`.
2. Use the Manhattan distance as the heuristic, but factor in the terrain costs for `g(n)` during the search.
3. Output the final path as a list of coordinates and the total movement cost.