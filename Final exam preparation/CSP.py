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
