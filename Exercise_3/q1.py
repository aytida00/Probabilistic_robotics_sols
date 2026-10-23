import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# plotting uncertainity ellipse as time passes.
import numpy as np
from myUtils import posterior_covariance
from myUtils import plot_uncertainity_ellipse
import matplotlib.pyplot as plt

# initial state(t = 0)
X0 = np.zeros([2,1])
mean_0 = np.zeros([2, 1])
cov_0 = np.zeros([2, 2])

# transisition function [X_t+1 = A*X_t + B*U_t + e_t]
# here e_t is prediction noise in Gaussian form with 0 mean and covariance R.
A = np.array([[1, 1], 
              [0, 1]])
B = np.zeros([2,2])
R = np.array([[0.25, 0.5], [0.5, 1]])

# number of timesteps
n = 110
# for storing predition step covariance of differnt timesteps
pred_cov_prev = cov_0


#for plotting
fig1, ax1 = plt.subplots()
plt.axis("equal")

for i in range(1, n+1):
    pred_cov_new = posterior_covariance(A, pred_cov_prev, R)
    print(f"Posterior covariance at time t = {i},")
    print(pred_cov_new)

    if i == 110:
        plot_uncertainity_ellipse(ax1, np.array([0, 0]), pred_cov_new)
        plt.show()
    pred_cov_prev = pred_cov_new