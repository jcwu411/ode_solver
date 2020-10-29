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
    dt = 0.01
    steps = 6000
    # which scheme you wanna use
    """
    forward:  Forward
    leapfrog: Leapfrog
    ab2:      Adams-Bashforth-2nd-order
    rk4:      Runge-Kutta-4th-order
    """
    scheme = "rk4"

    if scheme == "forward":
        scheme_fullname = "Forward"
    elif scheme == "leapfrog":
        scheme_fullname = "Leapfrog"
    elif scheme == "ab2":
        scheme_fullname = "Adams-Bashforth-2nd-order"
    elif scheme == "rk4":
        scheme_fullname = "Runge-Kutta-4th-order"

    save = False  # save = True means to save the figure

    homework = 2
    if homework == 1:
        x0 = [0.1, 0.1, 0.1]
        result = ode_solver.Ode(iv=x0, function=lorenz63, dt=dt, steps=steps, debug=0)
        result.integrate(scheme)

        title = 'Lorenz63 Model ( ' + scheme_fullname + ' )\nInitial value: ' + str(x0)
        filename = "plot_" + scheme + "_iv" + str(x0) + ".pdf"
        plot_data.plot3d(result.trajectory, ti=title, style='r-', lw=0.5, fn=filename, sa=save)
    else:
        x10 = [50.0, 50.0, 50.0]
        x20 = [50.01, 50.01, 50.01]
        x30 = [50.1, 50.1, 50.1]
        x40 = [51.0, 51.0, 51.0]
        result1 = ode_solver.Ode(iv=x10, function=lorenz63, dt=dt, steps=steps, debug=0)
        result2 = ode_solver.Ode(iv=x20, function=lorenz63, dt=dt, steps=steps, debug=0)
        result3 = ode_solver.Ode(iv=x30, function=lorenz63, dt=dt, steps=steps, debug=0)
        result4 = ode_solver.Ode(iv=x40, function=lorenz63, dt=dt, steps=steps, debug=0)
        result1.integrate(scheme)
        result2.integrate(scheme)
        result3.integrate(scheme)
        result4.integrate(scheme)

        title = 'Lorenz63 Model ( ' + scheme_fullname + ' )\n'
        var = 4
        if var == 2:
            filename = "plot_" + scheme + "_2diff_iv.pdf"
            plot_data.plot2dcomp2(result1.trajectory, result4.trajectory, x10, x40,
                                  dt=dt, steps=steps+1, ti=title, lw=1.0, fn=filename, sa=save)
        elif var == 4:
            filename = "plot_" + scheme + "_4diff_iv.pdf"
            plot_data.plot2dcomp4(result1.trajectory, result2.trajectory, result3.trajectory, result4.trajectory,
                                  x10, x20, x30, x40, dt=dt, steps=steps + 1, ti=title, lw=1.0, fn=filename, sa=save)

