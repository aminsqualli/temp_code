from pulp import LpProblem, LpVariable, lpSum, LpMinimize

class Cube:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

# Sample data
box_volumes = [100, 250]
cubes_data = {"Cube1": 350, "Cube2": 250, "Cube3": 5, "Cube4": 7, "Cube5": 8, "Cube6": 10}

# Create cubes
cubes = [Cube(name, volume) for name, volume in cubes_data.items()]

# Create the ILP problem
prob = LpProblem("CubeCutting", LpMinimize)

# Create binary variables for each cube and each box
x = LpVariable.dicts("Cut", [(cube.name, i) for cube in cubes for i in range(1, len(box_volumes) + 1)], cat='Binary')

# Objective function: Minimize the total number of cuts
prob += lpSum(x[(cube.name, i)] for cube in cubes for i in range(1, len(box_volumes) + 1)), "Total Cuts"

# Constraints: Each cube can be cut at most once, and its cut pieces can fill the boxes
for cube in cubes:
    prob += lpSum(x[(cube.name, i)] for i in range(1, len(box_volumes) + 1)) <= 1, f"Cut Once Constraint for {cube.name}"

for i, box_volume in enumerate(box_volumes):
    # The total volume of cut pieces in each box is less than or equal to the box's volume
    prob += lpSum(x[(cube.name, i + 1)] * cube.volume for cube in cubes) <= box_volume, f"Volume Constraint for Box {i + 1}"

# Solve the problem
prob.solve()

# Extract the solution
selected_cuts = [(cube.name, i) for cube in cubes for i in range(1, len(box_volumes) + 1) if x[(cube.name, i)].value() == 1]

# Print the selected cuts
for cut_name, box_number in selected_cuts:
    print(f"Cut {cut_name} is selected for Box {box_number}")