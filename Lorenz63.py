#!/usr/bin/env python3.8
"""
Created on 28/10/2020
@author: Jiacheng Wu, jcwu@pku.edu.cn
"""

import ode_solver
import numpy as np


def lorenz63(x_0):
    x, y, z = x_0
    fx = [10 * (y - x), x * (28 - z) - y, x * y - 8/3*z]
    return np.array(fx)


if __name__ == "__main__":
    x0 = [0.1, 0.1, 0.1]
    result = ode_solver.Ode(iv=x0, function=lorenz63, dt=0.01, steps=6000, debug=1)
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

    filename = "plot_"+scheme+"_iv"+str(x0)+".pdf"
    title = 'Lorenz63 Model ( ' + scheme_fullname + ' )\n' + str(x0)
    result.integrate(scheme)
    ode_solver.plot3d(result.trajectory, ti=title, style='r-', lw=0.5, fn=filename)
