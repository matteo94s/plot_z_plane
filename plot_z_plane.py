# =============================================================================
# Matteo Saibene
# https://github.com/matteo94s
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches


def plot_z_plane(B, A, plot_title='Z-Plane', scaling_factor=0):
    """
    Plot the complex z-plane given a transfer function.    
    plots the zeros Z and poles P with the unit circle for reference.
    Each zero is represented with an 'O' and each pole with an 'X' on the plot.    

    plot_z_plane(B,A) where B and A are row vectors containing transfer function
    polynomial coefficients plots the poles and zeros of B(z)/A(z).

    Parameters
    ----------
    B : Vector of coefficients.

    A : Vector of coefficients.

    plot_title : String, optional
        DESCRIPTION. Assign title to the plot. The default is 'Z-Plane'.

    scaling_factor : Integer, optional
        DESCRIPTION. Scales the plot. The default is 0.

    Usage example
    -------

    B1 = np.array([0.0725, 0.2200, 0.4085, 0.4883, 0.4085,    0.2200, 0.0725])
    A1 = np.array([1.0000,  -0.5835,  1.7021, -0.8477, 0.8401, -0.2823,   0.0924])


    B2 = np.array([1.0000,  1.3000,   0.4900,  -0.0130,  -0.0290])
    A2 = np.array([1.0000,   -0.4326,  -1.6656,   0.1253,  0.2877])

    B3 = np.array([1.0000, -1.4000,   0.2400,  0.3340,  -0.1305])
    A3 = np.array([1.0000,   0.5913,  -0.6436,  0.3803,  -1.0091])

    plt.figure(constrained_layout=True, figsize=(10, 8))
    plt, ax = plot_z_plane(B1, A1, plot_title='Filter1')

    plt.figure(constrained_layout=True, figsize=(10, 8))
    plt, ax = plot_z_plane(B2, A2, plot_title='Filter2', scaling_factor=1)

    plt.figure(constrained_layout=True, figsize=(10, 8))
    plt, ax = plot_z_plane(B3, A3, plot_title='Filter3', scaling_factor=1)

    """

    # Set proprietes of inner plot
    color_code = '#4DBEEE'  # Matlab Blue
    alfa = 0.8
    line_type = 'dotted'  # Check matplotlib documentation
    color_code_dots = '#0072BD'  # color code of circles and crosses

    # get a figure/plot
    ax = plt.subplot(1, 1, 1)

    # create the unit circle
    uc = patches.Circle((0, 0), radius=1, fill=False,
                        color=color_code, ls=line_type, alpha=alfa)
    ax.add_patch(uc)
    ax.set_xlim(-1, 1)
    ax.set_box_aspect(1)

    # Normalize coeficients if they are <1
    max_B = np.max(B)
    kn = max_B if max_B > 1 else 1
    B /= float(kn)

    max_A = np.max(A)
    kd = max_A if max_A > 1 else 1
    B /= float(kd)

    # Get the poles and zeros
    poles = np.roots(A)
    zeros = np.roots(B)

    # Plot the zeros and set marker properties
    t1 = plt.plot(zeros.real, zeros.imag, 'go', ms=10)
    plt.setp(t1, markersize=10.0, markeredgewidth=1.0,
             markeredgecolor=color_code_dots, markerfacecolor='white')

    # Plot the poles and set marker properties
    t2 = plt.plot(poles.real, poles.imag, 'rx', ms=10)
    plt.setp(t2, markersize=10.0, markeredgewidth=1.0,
             markeredgecolor=color_code_dots, markerfacecolor='white')

    # Horizontal line
    plt.plot([-scaling_factor-2, scaling_factor+2], [0, 0],
             linestyle=line_type, color=color_code,  alpha=alfa)
    # Vertical line
    plt.plot([0, 0], [-scaling_factor-2, scaling_factor+2],
             linestyle=line_type, color=color_code,  alpha=alfa)

    # set the ticks
    r = 1.5
    plt.axis('scaled')
    plt.axis([-r, r, -r, r])

    scaling_factor = int(scaling_factor)
    ticks = np.concatenate(
        (np.arange(-1+(-scaling_factor), 0, 0.5),
         np.array([0, 0.5]),
         np.arange(1, 1.5+scaling_factor, 0.5)
         ))

    # Show ticks
    plt.xticks(ticks)
    plt.yticks(ticks)
    plt.grid(linestyle='--', linewidth=0.2, color=color_code)
    plt.xlabel('Real Part')
    plt.ylabel('Imaginary Part')
    plt.title(plot_title)

    return plt, ax
