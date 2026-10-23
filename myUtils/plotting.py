import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches

# n = 1000
# x_mean = np.array([1.0, 2.0])
# P = np.diag([2.0, 1.0])
# x = np.zeros([2, n])

# x[0, :] = x_mean[0] + np.sqrt(P[0, 0]) * np.random.randn(1, n)
# x[1, :] = x_mean[1] + np.sqrt(P[1, 1]) * np.random.randn(1, n)

# fig1 = plt.figure(1)
# plt.plot(x[0, :], x[1, :], "C0.", label="Sampled data")
# plt.plot(x_mean[0], x_mean[1], "C1o", label="Population mean")
# plt.xlabel(r"$x_1$")
# plt.ylabel(r"$x_2$")
# plt.legend(loc="upper left")
# plt.axis("equal")
# plt.show()

def plot_uncertainity_ellipse(ax, X_mean:np.array,  cov_matrix: np.array):
    # calculate eigen value and eigenv vector
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    max_i = 0
    max_val = 0
    for i, val in enumerate(eigenvalues):
        if val >= max_val:
            max_i = i
            max_val = val
    width = 2*np.sqrt(eigenvalues[max_i])
    height = 2*np.sqrt(eigenvalues[max_i-1])

    # eigen vector representing highest eigenvalue which represent high variance
    major_eigenvect = eigenvectors[:, max_i]
    angle = np.arctan2(float(major_eigenvect[1]), float(major_eigenvect[0]))
    # print(angle)

    ell = patches.Ellipse([X_mean[0], X_mean[1]], width=width, height=height, angle=angle*180/3.14, color="C2")

    ax.add_patch(ell)
    ax.set_xlim(-100, 100)
    ax.set_ylim(-1000, 1000)
    
    # print(eigenvalues)
    # print(eigenvectors)
    # print(major_eigenvect)

# if __name__:="__main__":
#     fig2, ax2 = plt.subplots()
#     plt.axis("equal")
#     plot_uncertainity_ellipse(ax2, np.array([0, 0]), np.array([[8.75, 4.5 ],[4.5,  3.  ]]))
#     plt.show()