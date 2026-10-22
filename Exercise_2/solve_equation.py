import sympy as sp

# Define the matrix using exact rationals (e.g., -0.2 = -1/5)
M = sp.Matrix([
    [sp.Rational('-1/5'), sp.Rational('2/5'), sp.Rational('1/5')],
    [sp.Rational('1/5'),  sp.Rational('-3/5'), sp.Rational('3/5')],
    [0,                   sp.Rational('1/5'),  sp.Rational('-4/5')]
])

# Find the null space (the solution to M * v = 0)
null_space = M.nullspace()

# print("Base vector:")
# print(null_space[0])



A = sp.Matrix([
    [sp.Rational('4/5'), sp.Rational('2/5'), sp.Rational('1/5')],
    [sp.Rational('1/5'), sp.Rational('2/5'), sp.Rational('3/5')],
    [0,                  sp.Rational('1/5'), sp.Rational('1/5')]
])

# Construct the exact symbolic eigenvalue
lam_1 = (1 + sp.sqrt(2)) / 5

# Compute the null space for A - lambda*I
M_1 = A - lam_1 * sp.eye(3)
vector_1 = M_1.nullspace()[0]

# Use simplify() to clean up the algebraic fractions
print(sp.simplify(vector_1))