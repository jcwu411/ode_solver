#!/usr/bin/env python3.8
"""
Created on 28/10/2020
@author: Jiacheng Wu, jcwu@pku.edu.cn
"""

import ode_solver
import plot_data
import numpy as np


def lorenz63(x_0):
    x, y, z = x_0
    a, b, c = 10, 28, 8/3
    fx = [a * (y - x), x * (b - z) - y, x * y - c * z]
    return np.array(fx)


if __name__ == "__main__":
    #  initialization
    x0 = [50.0, 50.0, 50.0]
    dt = 0.01
    steps = 6000

    result = ode_solver.Ode(iv=x0, function=lorenz63, dt=dt, steps=steps, debug=1)
    # which scheme you wanna use
    """
    forward:  Forward
    leapfrog: Leapfrog
    ab2:      Adams-Bashforth-2nd-order
    rk4:      Runge-Kutta-4th-order
    """
    scheme = "rk4"
    result.integrate(scheme)

    if scheme == "forward":
        scheme_fullname = "Forward"
    elif scheme == "leapfrog":
        scheme_fullname = "Leapfrog"
    elif scheme == "ab2":
        scheme_fullname = "Adams-Bashforth-2nd-order"
    elif scheme == "rk4":
        scheme_fullname = "Runge-Kutta-4th-order"

    title = 'Lorenz63 Model ( ' + scheme_fullname + ' )\nInitial value: ' + str(x0)
    save = False  # save = True means to save the figure
    filename = "plot_" + scheme + "_iv" + str(x0) + ".pdf"

    plot_data.plot2d(result.trajectory, dt=dt, steps=steps+1, ti=title, lw=1.0, fn=filename, sa=save)

    # plot_data.plot3d(result.trajectory, ti=title, style='r-', lw=0.5, fn=filename, sa=save)
