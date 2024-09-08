### Map Coloring Problem with Arc Consistency (CSP)

You are tasked with solving a **Map Coloring Problem** for seven regions in Australia. The regions are:
- Western Australia (WA)
- Northern Territory (NT)
- Queensland (Q)
- New South Wales (NSW)
- Victoria (V)
- South Australia (SA)
- Tasmania (T)

Each region must be colored using one of the three colors: **red**, **green**, or **blue**, and adjacent regions cannot share the same color. 

#### Constraints:
- WA ≠ NT
- NT ≠ Q
- NT ≠ SA
- SA ≠ Q
- SA ≠ NSW
- NSW ≠ V

### Task:
1. **Implement a CSP solver** using **arc consistency** and **backtracking** to solve the map-coloring problem.
2. Your solution should first enforce arc consistency before attempting any assignments.
3. Your solution should return an assignment of colors to each region such that all constraints are satisfied.

### Example Solution:
An example of a valid solution might be:
```
{WA: red, NT: green, Q: red, NSW: green, V: red, SA: blue, T: green}
```