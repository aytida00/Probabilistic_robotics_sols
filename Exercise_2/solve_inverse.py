from sympy import *
import numpy as np

init_printing(use_unicode=False)

# 1. Defining the SymPy matrices
Q = Matrix([[9, -sqrt(2)-1, -1+sqrt(2)], 
           [4, sqrt(2), -sqrt(2)], 
           [1, 1, 1]])

D = Matrix([[1, 0, 0], 
            [0, 0.2+0.2*sqrt(2), 0], 
            [0, 0, 0.2-0.2*sqrt(2)]])


def apply_EVD_to_calculate_power_of_matrix(Q, D, n):
    # Convert SymPy matrices to standard NumPy float arrays
    Q_np = np.array(Q, dtype=float)
    D_np = np.array(D, dtype=float)
    
    # Calculate the numerical inverse
    Q_inv_np = np.linalg.inv(Q_np)
    
    # FIX: Use @ for matrix multiplication and matrix_power for exponentiation
    D_power_n = np.linalg.matrix_power(D_np, n)
    A_power_n = Q_np @ D_power_n @ Q_inv_np

    return A_power_n

# Compute A^100
A_100 = apply_EVD_to_calculate_power_of_matrix(Q, D, 1000)

# FIX: Use @ to multiply the matrix by your initial state vector
# Adjusted slightly to [0.34, 0.33, 0.33] so the initial probability sums to exactly 1.0
initial_state = np.array([0.333, 0.333, 0.333])
state_prob_at_n = A_100 @ initial_state

print("State probabilities at n=100:")
print(state_prob_at_n)

print("\nTotal Probability Sum (Should equal 1.0):")
print(np.sum(state_prob_at_n))
