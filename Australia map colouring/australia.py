# Australia Map Coloring using CSP (Backtracking)

states = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']

# Adjacency list: neighboring states must have different colors
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'Q': ['NT', 'SA', 'NSW'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []   # Tasmania has no land border
}

colors = ['Red', 'Green', 'Blue']

def is_safe(state, color, assignment):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def solve_csp(assignment):
    # If all states are assigned a color, solution found
    if len(assignment) == len(states):
        return assignment

    # Select next unassigned state
    for state in states:
        if state not in assignment:
            current_state = state
            break

    # Try each color
    for color in colors:
        if is_safe(current_state, color, assignment):
            assignment[current_state] = color

            result = solve_csp(assignment)
            if result is not None:
                return result

            # Backtrack
            del assignment[current_state]

    return None

# Solve the problem
solution = solve_csp({})

# Display result
if solution:
    print("Solution found:\n")
    for state in states:
        print(f"{state} -> {solution[state]}")
else:
    print("No solution exists.")