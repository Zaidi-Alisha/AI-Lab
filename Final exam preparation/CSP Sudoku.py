from ortools.sat.python import cp_model

def solve_sudoku(initial_grid):
    model = cp_model.CpModel()

    # Create variables: a 9x9 grid of integer variables with domain 1-9
    cell = [[model.new_int_var(1, 9, f'cell_{i}_{j}') for j in range(9)] for i in range(9)]

    # Add constraints for given cells (initial clues)
    for i in range(9):
        for j in range(9):
            if initial_grid[i][j] != 0:
                model.add(cell[i][j] == initial_grid[i][j])

    # AllDifferent constraints for rows
    for i in range(9):
        model.add_all_different([cell[i][j] for j in range(9)])

    # AllDifferent constraints for columns
    for j in range(9):
        model.add_all_different([cell[i][j] for i in range(9)])

    # AllDifferent constraints for 3x3 sub-grids
    for block_row in range(3):
        for block_col in range(3):
            block = [
                cell[i][j]
                for i in range(block_row * 3, (block_row + 1) * 3)
                for j in range(block_col * 3, (block_col + 1) * 3)
            ]
            model.add_all_different(block)

    # Create solver and solve
    solver = cp_model.CpSolver()
    status = solver.solve(model)

    # Print the solution
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print("Solved Sudoku:")
        for i in range(9):
            print([solver.value(cell[i][j]) for j in range(9)])
    else:
        print("No solution found.")

# Example partial Sudoku puzzle (0 = empty cell)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Run solver
solve_sudoku(sudoku_grid)
