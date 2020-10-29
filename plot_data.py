#!/usr/bin/env python3.8
"""
Created on 28/10/2020
@author: Jiacheng Wu, jcwu@pku.edu.cn
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


def plot2d(data, dt, steps, lw=1.0, ti="Plot", fn="test2d.pdf", sa=True):
    x, y, z = data[:, 0], data[:, 1], data[:, 2]

    t = np.linspace(0, steps * dt, steps)
    plt.figure()
    plt.subplot(311)  # plot x-t
    plt.title(ti)
    plt.plot(t, x, color='red', linewidth=lw)
    plt.ylabel('x')
    ax = plt.gca()
    ax.set_xticklabels([])
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.tick_params(axis='y', labelsize=8)
    ax.set_xlim(0, steps * dt)

    plt.subplot(312)  # plot y-t
    plt.plot(t, y, color='blue', linewidth=lw)
    plt.ylabel('y')
    ax = plt.gca()
    ax.set_xticklabels([])
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.tick_params(axis='y', labelsize=8)
    ax.set_xlim(0, steps * dt)

    plt.subplot(313)  # plot z-t
    plt.plot(t, z, color='black', linewidth=lw)
    plt.xlabel('t')
    plt.ylabel('z')
    ax = plt.gca()
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.tick_params(axis='y', labelsize=8)
    ax.set_xlim(0, steps * dt)

    if sa:
        plt.savefig(fn)
    plt.show()
    plt.close()


def plot3d(data, style="-r", lw=1.0, ti="Plot", xl="X", yl="Y", zl="Z", fn="test3d.pdf", sa=True):
    x, y, z = data[:, 0], data[:, 1], data[:, 2]

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set(title=ti, xlabel=xl, ylabel=yl, zlabel=zl)
    ax.plot(x, y, z, style, linewidth=lw)
    if sa:
        plt.savefig(fn)
    plt.show()
    plt.close()
