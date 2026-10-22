import numpy as np

# R  is defined as convariance of noise of prediction 
def posterior_covariance(A:np.array, prior_cov:np.array, R:np.array):
    return A@prior_cov@(A.T) + R