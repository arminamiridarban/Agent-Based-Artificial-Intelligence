### Map Coloring Problem

#### Project Overview

You are tasked with solving a Map Coloring Problem using techniques for Constraint Satisfaction Problems (CSP). The goal is to assign colors to a set of regions on a map such that no two adjacent regions have the same color. You will implement a solution using the Backtracking algorithm, incorporating constraint propagation techniques (e.g., Forward Checking or Arc Consistency) and heuristics (e.g., Minimum Remaining Values and Least Constraining Value).

#### Problem Description

Consider a map with the following five regions:
- **Region A**
- **Region B**
- **Region C**
- **Region D**
- **Region E**

These regions are connected as follows:
- **Region A** is adjacent to **Region B** and **Region C**.
- **Region B** is adjacent to **Region A**, **Region C**, and **Region D**.
- **Region C** is adjacent to **Region A**, **Region B**, **Region D**, and **Region E**.
- **Region D** is adjacent to **Region B**, **Region C**, and **Region E**.
- **Region E** is adjacent to **Region C** and **Region D**.

#### Variables

- **Variables:** The regions A, B, C, D, and E are the variables.
- **Domains:** The set of colors available for each region. Use the following colors:
  - Red
  - Green
  - Blue

#### Constraints

The constraints of the problem are that no two adjacent regions can have the same color. The adjacency relationships are as described above.

#### Requirements

1. **Backtracking Implementation:**
   - Implement the basic Backtracking algorithm to assign colors to the regions.
   - Ensure that your solution checks for consistency with the constraints at each step.

2. **Constraint Propagation:**
   - Enhance your Backtracking algorithm with Forward Checking to keep track of remaining legal values for unassigned variables.

3. **Heuristics:**
   - Implement the **Minimum Remaining Values (MRV)** heuristic to choose the next variable to assign.
   - Implement the **Least Constraining Value (LCV)** heuristic to order the domain values when making assignments.

4. **Output:**
   - Your program should output the color assigned to each region, ensuring that all constraints are satisfied.
   - If no solution exists, the program should indicate that the problem is unsolvable with the given constraints and domains.

5. **Code Structure:**
   - Use object-oriented programming principles. Define classes such as `CSP`, `Variable`, `Domain`, and `Constraint`.
   - Your code should be modular and well-documented, with comments explaining key steps and decisions.

#### Deliverables

1. **Source Code:** Submit your fully implemented Python program. Ensure that your code is clean, well-documented, and follows best practices.
