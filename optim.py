from pulp import LpProblem, LpVariable, lpSum, LpMinimize

class Cube:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

# Sample data
box_volumes = [100, 250]
cubes_data = {"Cube1": 350, "Cube2": 250, "Cube3": 5, "Cube4": 7, "Cube5": 8, "Cube6": 10}
tolerance = 10  # Tolerance for each box

# Create cubes
cubes = [Cube(name, volume) for name, volume in cubes_data.items()]

# Create the ILP problem
prob = LpProblem("CubeCutting", LpMinimize)

# Create binary variables for each cube, whether it is used and whether it is cut
x = LpVariable.dicts("UseCube", [cube.name for cube in cubes], cat='Binary')
y = LpVariable.dicts("CutCube", [cube.name for cube in cubes], cat='Binary')

# Objective function: Minimize the total number of cubes used and cut
prob += lpSum(x[cube.name] + y[cube.name] for cube in cubes), "Total Cubes Used and Cut"

# Constraints: The total volume of cubes in each box is within the box's volume ± tolerance
for i, box_volume in enumerate(box_volumes):
    prob += lpSum((x[cube.name] + y[cube.name]) * cube.volume for cube in cubes) <= box_volume + tolerance, f"Volume Constraint for Box {i + 1} Upper"
    prob += lpSum((x[cube.name] + y[cube.name]) * cube.volume for cube in cubes) >= box_volume - tolerance, f"Volume Constraint for Box {i + 1} Lower"

# If a cube is cut (y[cube.name] == 1), it must be used (x[cube.name] == 1)
for cube in cubes:
    prob += y[cube.name] <= x[cube.name], f"Cut Implies Use for {cube.name}"

# Solve the problem
prob.solve()

# Extract the solution
selected_cubes = [cube.name for cube in cubes if x[cube.name].value() == 1]
cut_cubes = [cube.name for cube in cubes if y[cube.name].value() == 1]

# Print the selected and cut cubes
print("Selected Cubes:", selected_cubes)
print("Cut Cubes:", cut_cubes)