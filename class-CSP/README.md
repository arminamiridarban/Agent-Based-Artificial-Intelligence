### Class Scheduling

#### Problem Overview

You are tasked with scheduling classes in a university. The goal is to assign rooms to classes in a way that no two classes that share students are scheduled in the same room at the same time. You will use Constraint Satisfaction Problem (CSP) techniques to solve this problem.

#### Problem Details

- **Variables:** Each class is a variable.
- **Domains:** Each variable can be assigned to one of several available rooms (e.g., Room1, Room2, Room3).
- **Constraints:** 
  - No two classes that share students can be scheduled in the same room at the same time.
  - Each class must be assigned to exactly one room.

#### Example Scenario

Let's consider a small example with 4 classes and 3 rooms:

- **Classes:** `C1`, `C2`, `C3`, `C4`
- **Rooms:** `Room1`, `Room2`, `Room3`
- **Student Enrollment:**
  - `C1` and `C2` have some common students.
  - `C1` and `C3` have some common students.
  - `C2` and `C4` have some common students.
  - `C3` and `C4` have no common students.


#### Goal

The goal is to assign each class to a room such that no two classes with common students are scheduled in the same room.

### Steps to Solve the Problem

1. **Model the Problem:**
   - Define the variables, domains, and constraints in your CSP representation.

2. **Implement the CSP Solver:**
   - Use techniques such as Backtracking, MRV, LCV, and Forward Checking to solve the problem.

3. **Test the Solution:**
   - Ensure that your solution satisfies all the constraints.


### Your Task

- **Understand the Problem:** Review the problem description and the provided template.
- **Implement the Solution:** Modify and complete the template to solve the CSP problem.
- **Test and Verify:** Run the code and verify that it produces a valid schedule that satisfies all constraints.

This exercise will help you solidify your understanding of CSPs and the techniques used to solve them.