import matplotlib.pyplot as plt
# Define the map of Australia as a dictionary with state names as keys and neighbors as values
australia = {
    "WA": ["SA", "NT"],
    "NT": ["WA", "SA", "QL"],
    "SA": ["WA", "NT", "QL", "NSW", "VI"],
    "QL": ["NT", "SA", "NSW"],
    "NSW": ["QL", "SA", "VI"],
    "VI": ["NSW", "SA"],
}

# Define the domain of colors
colors = ["red", "green", "blue"]

# Define a function to check if the current state assignment is consistent with the constraints
def is_consistent(state, color, assignment):
    for neighbor in australia[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Define a recursive function to search for a solution
def backtrack_search(assignment):
    # If all states are assigned, return the solution
    if len(assignment) == len(australia):
        return assignment
    
    # Select an unassigned state
    unassigned_states = [state for state in australia.keys() if state not in assignment]
    state = unassigned_states[0]
    
    # Try each possible value for the selected state
    for color in colors:
        # Check if the current state assignment is consistent with the constraints
        if is_consistent(state, color, assignment):
            # Add the current state assignment to the partial solution
            assignment[state] = color
            # Recursively search for a solution with the updated partial solution
            result = backtrack_search(assignment)
            # If a solution is found, return it
            if result is not None:
                return result
            # Otherwise, backtrack and try the next possible value for the selected state
            del assignment[state]
    
    # If no solution is found, return None
    return None

# Solve the problem and print the solution
solution = backtrack_search({})
print(solution)

# Define the coordinates of the nodes for plotting
coordinates = {
    "WA": (0, 2),
    "NT": (1, 1),
    "SA": (2, 2),
    "QL": (1, 0),
    "NSW": (3, 1),
    "VI": (4, 2),
}

# Plot the graph
fig, ax = plt.subplots()
for state, neighbors in australia.items():
    for neighbor in neighbors:
        x1, y1 = coordinates[state]
        x2, y2 = coordinates[neighbor]
        ax.plot([x1, x2], [y1, y2], color="gray")
    x, y = coordinates[state]
    circle = plt.Circle((x, y), radius=0.4, color=solution[state])
    ax.add_patch(circle)
    ax.text(x, y, state, ha="center", va="center")
ax.set_aspect("equal")
ax.set_xlim([-0.5, 4.5])
ax.set_ylim([-0.5, 2.5])
plt.show()
