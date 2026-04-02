"""
Map Coloring Problem for 33 Districts of Telangana using CSP (Constraint Satisfaction Problem)
Solved using Backtracking with Forward Checking and MRV (Minimum Remaining Values) heuristic.
"""

# ─────────────────────────────────────────────────────────────────────────────
# 1. DEFINE THE 33 DISTRICTS OF TELANGANA
# ─────────────────────────────────────────────────────────────────────────────
DISTRICTS = [
    "Adilabad", "Kumuram Bheem", "Mancherial", "Nirmal", "Nizamabad",
    "Jagitial", "Peddapalli", "Jayashankar Bhupalpally", "Rajanna Sircilla",
    "Karimnagar", "Kamareddy", "Medak", "Sangareddy", "Siddipet",
    "Jangaon", "Hanamkonda", "Warangal", "Mahabubabad", "Bhadradri Kothagudem",
    "Khammam", "Suryapet", "Nalgonda", "Yadadri Bhuvanagiri", "Medchal-Malkajgiri",
    "Hyderabad", "Rangareddy", "Vikarabad", "Narayanpet", "Mahbubnagar",
    "Jogulamba Gadwal", "Wanaparthy", "Nagarkurnool", "Nagar Kurnool Rural"
]

# ─────────────────────────────────────────────────────────────────────────────
# 2. ADJACENCY LIST (Neighbours share a border)
# ─────────────────────────────────────────────────────────────────────────────
ADJACENCY = {
    "Adilabad":                    ["Kumuram Bheem", "Mancherial", "Nirmal"],
    "Kumuram Bheem":               ["Adilabad", "Mancherial", "Jayashankar Bhupalpally"],
    "Mancherial":                  ["Adilabad", "Kumuram Bheem", "Peddapalli", "Nirmal", "Jagitial"],
    "Nirmal":                      ["Adilabad", "Mancherial", "Jagitial", "Nizamabad", "Kamareddy"],
    "Nizamabad":                   ["Nirmal", "Kamareddy", "Medak"],
    "Jagitial":                    ["Mancherial", "Nirmal", "Rajanna Sircilla", "Karimnagar", "Peddapalli"],
    "Peddapalli":                  ["Mancherial", "Jagitial", "Karimnagar", "Jayashankar Bhupalpally"],
    "Jayashankar Bhupalpally":     ["Kumuram Bheem", "Peddapalli", "Karimnagar", "Warangal", "Mahabubabad", "Bhadradri Kothagudem"],
    "Rajanna Sircilla":            ["Jagitial", "Karimnagar", "Siddipet"],
    "Karimnagar":                  ["Jagitial", "Peddapalli", "Jayashankar Bhupalpally", "Rajanna Sircilla", "Siddipet", "Jangaon"],
    "Kamareddy":                   ["Nirmal", "Nizamabad", "Medak", "Sangareddy"],
    "Medak":                       ["Nizamabad", "Kamareddy", "Sangareddy", "Siddipet", "Medchal-Malkajgiri", "Yadadri Bhuvanagiri"],
    "Sangareddy":                  ["Kamareddy", "Medak", "Siddipet", "Medchal-Malkajgiri", "Hyderabad", "Rangareddy", "Vikarabad"],
    "Siddipet":                    ["Rajanna Sircilla", "Karimnagar", "Medak", "Sangareddy", "Yadadri Bhuvanagiri", "Jangaon"],
    "Jangaon":                     ["Karimnagar", "Siddipet", "Yadadri Bhuvanagiri", "Hanamkonda", "Warangal"],
    "Hanamkonda":                  ["Jangaon", "Warangal", "Mahabubabad", "Suryapet", "Nalgonda", "Yadadri Bhuvanagiri"],
    "Warangal":                    ["Jayashankar Bhupalpally", "Jangaon", "Hanamkonda", "Mahabubabad"],
    "Mahabubabad":                 ["Jayashankar Bhupalpally", "Warangal", "Hanamkonda", "Suryapet", "Khammam", "Bhadradri Kothagudem"],
    "Bhadradri Kothagudem":        ["Jayashankar Bhupalpally", "Mahabubabad", "Khammam"],
    "Khammam":                     ["Bhadradri Kothagudem", "Mahabubabad", "Suryapet"],
    "Suryapet":                    ["Hanamkonda", "Mahabubabad", "Khammam", "Nalgonda", "Yadadri Bhuvanagiri"],
    "Nalgonda":                    ["Hanamkonda", "Suryapet", "Yadadri Bhuvanagiri", "Medchal-Malkajgiri", "Rangareddy", "Mahbubnagar"],
    "Yadadri Bhuvanagiri":         ["Medak", "Siddipet", "Jangaon", "Hanamkonda", "Suryapet", "Nalgonda", "Medchal-Malkajgiri"],
    "Medchal-Malkajgiri":          ["Medak", "Sangareddy", "Yadadri Bhuvanagiri", "Nalgonda", "Hyderabad", "Rangareddy"],
    "Hyderabad":                   ["Sangareddy", "Medchal-Malkajgiri", "Rangareddy"],
    "Rangareddy":                  ["Sangareddy", "Nalgonda", "Medchal-Malkajgiri", "Hyderabad", "Vikarabad", "Mahbubnagar"],
    "Vikarabad":                   ["Sangareddy", "Rangareddy", "Mahbubnagar", "Narayanpet"],
    "Narayanpet":                  ["Vikarabad", "Mahbubnagar", "Wanaparthy"],
    "Mahbubnagar":                 ["Nalgonda", "Rangareddy", "Vikarabad", "Narayanpet", "Wanaparthy", "Nagarkurnool"],
    "Jogulamba Gadwal":            ["Nagarkurnool", "Wanaparthy", "Nagar Kurnool Rural"],
    "Wanaparthy":                  ["Narayanpet", "Mahbubnagar", "Nagarkurnool", "Jogulamba Gadwal"],
    "Nagarkurnool":                ["Mahbubnagar", "Wanaparthy", "Jogulamba Gadwal", "Nagar Kurnool Rural"],
    "Nagar Kurnool Rural":         ["Nagarkurnool", "Jogulamba Gadwal"],
}

# ─────────────────────────────────────────────────────────────────────────────
# 3. COLORS
# ─────────────────────────────────────────────────────────────────────────────
COLORS = ["Red", "Green", "Blue", "Yellow"]

# ─────────────────────────────────────────────────────────────────────────────
# 4. CSP SOLVER — Backtracking + Forward Checking + MRV
# ─────────────────────────────────────────────────────────────────────────────

def is_consistent(district, color, assignment):
    """Return True if assigning `color` to `district` violates no constraints."""
    for neighbor in ADJACENCY.get(district, []):
        if assignment.get(neighbor) == color:
            return False
    return True


def forward_check(district, color, assignment, domains):
    """
    Remove `color` from neighbors' domains.
    Returns False if any neighbor's domain becomes empty (dead end).
    """
    removed = {}
    for neighbor in ADJACENCY.get(district, []):
        if neighbor not in assignment:
            if color in domains[neighbor]:
                domains[neighbor].remove(color)
                removed.setdefault(neighbor, []).append(color)
                if not domains[neighbor]:
                    # Restore and signal failure
                    for n, colors in removed.items():
                        domains[n].extend(colors)
                    return False, removed
    return True, removed


def restore_domains(removed, domains):
    """Undo forward-checking removals."""
    for district, colors in removed.items():
        domains[district].extend(colors)


def select_unassigned_variable(assignment, domains):
    """MRV heuristic: pick the unassigned district with the fewest remaining colors."""
    unassigned = [d for d in DISTRICTS if d not in assignment]
    return min(unassigned, key=lambda d: len(domains[d]))


def backtrack(assignment, domains):
    if len(assignment) == len(DISTRICTS):
        return assignment  # Solution found

    district = select_unassigned_variable(assignment, domains)

    for color in list(domains[district]):
        if is_consistent(district, color, assignment):
            assignment[district] = color
            ok, removed = forward_check(district, color, assignment, domains)

            if ok:
                result = backtrack(assignment, domains)
                if result is not None:
                    return result

            restore_domains(removed, domains)
            del assignment[district]

    return None  # Trigger backtrack


def solve():
    domains = {d: list(COLORS) for d in DISTRICTS}
    assignment = {}
    return backtrack(assignment, domains)


# ─────────────────────────────────────────────────────────────────────────────
# 5. VISUALISE THE RESULT
# ─────────────────────────────────────────────────────────────────────────────

def display_result(solution):
    if solution is None:
        print("No solution found.")
        return

    COLOR_CODES = {
        "Red":    "\033[41m",
        "Green":  "\033[42m",
        "Blue":   "\033[44m",
        "Yellow": "\033[43m",
    }
    RESET = "\033[0m"
    BOLD  = "\033[1m"

    print(f"\n{BOLD}{'═'*55}")
    print("  Map Coloring — 33 Districts of Telangana (CSP)")
    print(f"{'═'*55}{RESET}\n")

    print(f"  {'District':<35} {'Color'}")
    print(f"  {'-'*50}")
    for district in DISTRICTS:
        color = solution[district]
        bar = f"{COLOR_CODES[color]}   {RESET}"
        print(f"  {bar} {district:<33} {color}")

    # Verify no two neighbours share the same color
    violations = 0
    for d, neighbors in ADJACENCY.items():
        for n in neighbors:
            if solution.get(d) == solution.get(n):
                print(f"  !! Conflict: {d} and {n} both {solution[d]}")
                violations += 1
    if violations == 0:
        print(f"\n  {BOLD}✓ Valid coloring — no adjacent districts share a color!{RESET}")
    print()


def draw_matplotlib(solution):
    """Optional: draw a geographic-ish layout using matplotlib patches."""
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
        import random, math

        COLOR_MAP = {
            "Red":    "#E74C3C",
            "Green":  "#2ECC71",
            "Blue":   "#3498DB",
            "Yellow": "#F1C40F",
        }

        # Simple circular layout — positions for 33 nodes
        n = len(DISTRICTS)
        positions = {}
        for i, d in enumerate(DISTRICTS):
            angle = 2 * math.pi * i / n
            r = 4 + (i % 3) * 1.2
            positions[d] = (r * math.cos(angle), r * math.sin(angle))

        fig, ax = plt.subplots(figsize=(16, 14))
        ax.set_facecolor("#1a1a2e")
        fig.patch.set_facecolor("#1a1a2e")

        # Draw edges
        drawn = set()
        for d, neighbors in ADJACENCY.items():
            x1, y1 = positions[d]
            for n in neighbors:
                key = tuple(sorted([d, n]))
                if key not in drawn:
                    x2, y2 = positions[n]
                    ax.plot([x1, x2], [y1, y2], color="#555577", lw=0.8, zorder=1)
                    drawn.add(key)

        # Draw nodes
        for d in DISTRICTS:
            x, y = positions[d]
            color = COLOR_MAP[solution[d]]
            circle = plt.Circle((x, y), 0.55, color=color, zorder=3, ec="white", lw=1.2)
            ax.add_patch(circle)
            ax.text(x, y, d[:8], ha="center", va="center",
                    fontsize=5.5, color="white", fontweight="bold", zorder=4)

        # Legend
        legend_patches = [mpatches.Patch(color=c, label=name)
                          for name, c in COLOR_MAP.items()]
        ax.legend(handles=legend_patches, loc="lower right",
                  facecolor="#2c2c54", edgecolor="white", labelcolor="white",
                  fontsize=11, title="Colors", title_fontsize=12)

        ax.set_xlim(-8, 8); ax.set_ylim(-8, 8)
        ax.set_aspect("equal"); ax.axis("off")
        ax.set_title("Telangana District Map Coloring (CSP – 4 Colors)",
                     color="white", fontsize=16, fontweight="bold", pad=14)

        plt.tight_layout()
        plt.savefig("telangana_map_coloring.png", dpi=150,
                    bbox_inches="tight", facecolor=fig.get_facecolor())
        print("  Graph saved to telangana_map_coloring.png")
        plt.show()

    except ImportError:
        print("  (matplotlib not available — skipping graph visualisation)")


# ─────────────────────────────────────────────────────────────────────────────
# 6. ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Solving CSP Map Coloring for 33 districts of Telangana …")
    solution = solve()
    display_result(solution)
    draw_matplotlib(solution)
