from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpStatus

class Cube:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

# Sample data
box_volumes = [100, 250, 150]
cubes_data = {"Cube1": 350, "Cube2": 250, "Cube3": 5, "Cube4": 7, "Cube5": 8, "Cube6": 10}
tolerance = 10  # Tolerance for each box

# Create cubes
cubes = [Cube(name, volume) for name, volume in cubes_data.items()]

# Create continuous variables for each cube and each box
x = LpVariable.dicts("UseCube", [(cube.name, i) for cube in cubes for i in range(1, len(box_volumes) + 1)], lowBound=0, upBound=1, cat='Continuous')

# Objective function: Minimize the total volume of cubes used
prob = LpProblem("CubeCutting", LpMinimize)
prob += lpSum(x[(cube.name, i)] * cube.volume for cube in cubes for i in range(1, len(box_volumes) + 1)), "Total Volume Used"

# Constraints: The total volume of cubes in each box is within the box's volume ± tolerance
for i, box_volume in enumerate(box_volumes):
    prob += lpSum(x[(cube.name, i + 1)] * cube.volume for cube in cubes) <= box_volume + tolerance, f"Volume Constraint for Box {i + 1} Upper"
    prob += lpSum(x[(cube.name, i + 1)] * cube.volume for cube in cubes) >= box_volume - tolerance, f"Volume Constraint for Box {i + 1} Lower"

# Each cube can be used at most once in each box
for cube in cubes:
    prob += lpSum(x[(cube.name, i)] for i in range(1, len(box_volumes) + 1)) <= 1, f"Single Use Constraint for {cube.name}"

# The total usage of each cube across all boxes should not exceed its volume
for cube in cubes:
    prob += lpSum(x[(cube.name, i)] for i in range(1, len(box_volumes) + 1)) * cube.volume <= cube.volume, f"Volume Constraint for {cube.name}"

# Solve the problem
prob.solve()

# Check if the problem is feasible
if LpStatus[prob.status] == "Infeasible":
    print("The problem is infeasible. Adjust constraints or tolerance values.")
else:
    # Extract the solution
    selected_cubes = [(cube.name, i, x[(cube.name, i)].value()) for cube in cubes for i in range(1, len(box_volumes) + 1) if x[(cube.name, i)].value() > 0]

    # Print the selected cubes and their fractional use
    print("Selected Cubes and Their Fractional Use:")
    for cube_name, box_number, fractional_use in selected_cubes:
        print(f"Cube {cube_name} in Box {box_number} with fractional use {fractional_use}")