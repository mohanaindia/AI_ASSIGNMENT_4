# Australia Map Coloring using CSP

## Description
This project solves the Australia Map Coloring problem using a Constraint Satisfaction Problem (CSP) approach. The aim is to assign colors to the states and territories of Australia so that no two neighboring regions have the same color. The states used are WA, NT, Q, SA, NSW, V, and T, and the available colors are Red, Green, and Blue. This is a common Artificial Intelligence problem because it shows how a real problem can be represented using variables, domains, and constraints.

## What the Program Does
The program assigns a color to each state one by one and checks whether that color is valid. A color is valid only if none of the neighboring states already has the same color. If a conflict happens, the program tries another color. If no color works, it goes back to the previous state and changes its color. This process is called backtracking. Once all states are colored without any conflict, the program prints the solution.

## How It Works
The program first stores all the states and their neighboring states. Then it stores the list of possible colors. A function checks whether a color can safely be assigned to a state. Another function uses backtracking to try all possible valid assignments step by step until a complete solution is found. Tasmania has no land border with the mainland states, so it can take any color.

## Requirements
- Python 3.x
- No external libraries required

## How to Run
Save the code in a file named `australia.py` and run it using:

`python australia.py`

or

`python3 australia.py`

## Sample Output
```text
Solution found:

WA -> Red
NT -> Green
Q -> Red
SA -> Blue
NSW -> Green
V -> Red
T -> Red
