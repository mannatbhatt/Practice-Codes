# Python Code for Solving 3-Loop Circuit (KVL Equations)

# You can run this code directly in any Python IDE or notebook

import sympy as sp

# Define variables for loop currents

I1, I2, I3 = sp.symbols('I1 I2 I3')

# Given circuit parameters (Ω and V)

R12 = 5   # shared between loop1 and loop2
R23 = 5   # shared between loop2 and loop3
R_left = 5  # bottom left resistor
R_mid = 6   # center vertical resistor
R_right1 = 3  # top right
R_right2 = 7  # upper right series
R_bottom_mid = 5
R_bottom_right = 5

V1 = 10  # left battery (V)
V2 = 5   # middle battery (V)
V3 = 5   # right battery (V)

# Write KVL equations based on assumed clockwise currents

# Equation 1: Left loop (Loop 1)

eq1 = V1 - R12*(I1 - I2) - R_left*I1 - R_left*I1

eq1 = V1 - R12*(I1 - I2) - 2*R_left*I1

# Equation 2: Middle loop (Loop 2)

eq2 = -R12*(I2 - I1) - R_mid*I2 - R23*(I2 - I3) - V2 - R_bottom_mid*I2

# Equation 3: Right loop (Loop 3)

eq3 = -R23*(I3 - I2) - R_right1*I3 - R_right2*I3 - V3 - R_bottom_right*I3

# Simplify each equation to standard form eq = 0

eq1_s = sp.simplify(eq1)
eq2_s = sp.simplify(eq2)
eq3_s = sp.simplify(eq3)

# Solve the 3 equations simultaneously

solution = sp.solve([eq1_s, eq2_s, eq3_s], (I1, I2, I3))

print("Currents in each loop (A):")
for var, val in solution.items():
    print(f"{var} = {float(val):.3f} A")
