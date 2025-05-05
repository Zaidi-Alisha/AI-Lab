from ortools.sat.python import cp_model

def solve_csp():
    # Step 1: Create the model
    model = cp_model.CpModel()

    # Step 2: Create the variables with finite domains
    num_vals = 3  # domain: 0, 1, 2
    x = model.new_int_var(0, num_vals - 1, "x")
    y = model.new_int_var(0, num_vals - 1, "y")
    z = model.new_int_var(0, num_vals - 1, "z")

    # Step 3: Add constraints
    model.add(x != y)
    model.add(y != z)
    model.add(x != z)

    # Step 4: Create a solver and solve the model
    solver = cp_model.CpSolver()
    status = solver.solve(model)

    # Step 5: Output the results
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print("Solution Found:")
        print(f"x = {solver.value(x)}")
        print(f"y = {solver.value(y)}")
        print(f"z = {solver.value(z)}")
    else:
        print("No solution found.")

# Run the function
solve_csp()


#map coloring problem 
# Define map coloring using backtracking

# Regions and their adjacent neighbors
adjacency = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

# Available colors
colors = ['Red', 'Green', 'Blue']

def is_valid(region, color, assignment):
    for neighbor in adjacency[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    # If all regions are assigned
    if len(assignment) == len(adjacency):
        return assignment

    # Select an unassigned region
    unassigned = [r for r in adjacency if r not in assignment][0]

    for color in colors:
        if is_valid(unassigned, color, assignment):
            assignment[unassigned] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[unassigned]

    return None

# Run CSP solver
solution = backtrack({})
if solution:
    print("Map Coloring Solution:")
    for region, color in solution.items():
        print(f"{region}: {color}")
else:
    print("No solution found.")


#n queen problem

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(n):
    def backtrack(row, board):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1, board)

    solutions = []
    board = [-1] * n
    backtrack(0, board)
    return solutions

# Input
n = 4
result = solve_n_queens(n)

print(f"\nSolutions for {n}-Queens:")
for sol in result:
    for i in sol:
        row = ['.'] * n
        row[i] = 'Q'
        print(' '.join(row))
    print()

#schedule timetable 
# Courses and their conflicts
conflicts = {
    'C1': ['C2', 'C3'],
    'C2': ['C1', 'C4'],
    'C3': ['C1'],
    'C4': ['C2']
}

# Available timeslots
timeslots = ['T1', 'T2', 'T3']

def is_valid(course, timeslot, schedule):
    for conflict_course in conflicts.get(course, []):
        if schedule.get(conflict_course) == timeslot:
            return False
    return True

def backtrack(schedule):
    # All courses scheduled
    if len(schedule) == len(conflicts):
        return schedule

    # Pick an unscheduled course
    unassigned = [c for c in conflicts if c not in schedule][0]

    for timeslot in timeslots:
        if is_valid(unassigned, timeslot, schedule):
            schedule[unassigned] = timeslot
            result = backtrack(schedule)
            if result:
                return result
            del schedule[unassigned]

    return None

# Run CSP solver
solution = backtrack({})
if solution:
    print("Timetable Schedule:")
    for course, slot in solution.items():
        print(f"{course}: {slot}")
else:
    print("No valid schedule found.")
