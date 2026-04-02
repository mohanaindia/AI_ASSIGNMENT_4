# Cryptarithmetic CSP Solver

This program solves the cryptarithmetic puzzle **TWO + TWO = FOUR** using a Constraint Satisfaction Problem (CSP) with backtracking search. Each letter is assigned a unique digit, leading letters cannot be zero, carry values are used for column-wise addition, and the solver finds a valid assignment that satisfies the full equation.

## Requirements
Python 3 and a `csp.py` file in the same folder containing `CSP` and `backtracking_search`.

## File
`crypto.py`

## How to Run
Run the program from the terminal using:
```bash
python3 crypto.py
```

--- Task 4: Cryptarithmetic Solution (TWO + TWO = FOUR) ---
T = 7
W = 3
O = 4
F = 1
U = 6
R = 8
C10 = 0
C100 = 0
C1000 = 1

Equation Check:
  734
+ 734
-----
 1468