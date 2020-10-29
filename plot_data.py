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


def plot2dcomp2(data1, data2, x10, x20, dt, steps, lw=1.0, ti="Plot", fn="test2d.pdf", sa=True):
    x1, y1, z1 = data1[:, 0], data1[:, 1], data1[:, 2]
    x2, y2, z2 = data2[:, 0], data2[:, 1], data2[:, 2]

    t = np.linspace(0, steps * dt, steps)
    plt.figure()
    plt.subplot(311)  # plot x-t
    plt.title(ti)
    plt.plot(t, x1, color='red', linewidth=lw, label=str(x10))
    plt.plot(t, x2, color='blue', linewidth=lw, label=str(x20))
    plt.legend(loc="upper right", fontsize=8, ncol=2)
    plt.ylabel('x')
    ax = plt.gca()
    ax.set_xticklabels([])
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.tick_params(axis='y', labelsize=8)
    ax.set_xlim(0, steps * dt)

    plt.subplot(312)  # plot y-t
    plt.plot(t, y1, color='red', linewidth=lw)
    plt.plot(t, y2, color='blue', linewidth=lw)
    plt.ylabel('y')
    ax = plt.gca()
    ax.set_xticklabels([])
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.tick_params(axis='y', labelsize=8)
    ax.set_xlim(0, steps * dt)

    plt.subplot(313)  # plot z-t
    plt.plot(t, z1, color='red', linewidth=lw)
    plt.plot(t, z2, color='blue', linewidth=lw)
    plt.xlabel('t')
    plt.ylabel('z')
    ax = plt.gca()
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.tick_params(axis='y', labelsize=8)
    ax.tick_params(axis='x', labelsize=8)
    ax.set_xlim(0, steps * dt)
    plt.tight_layout()

    if sa:
        plt.savefig(fn)
    plt.show()
    plt.close()


def plot2dcomp4(data1, data2, data3, data4, x10, x20, x30, x40,
                dt, steps, lw=1.0, ti="Plot", fn="test2d.pdf", sa=True):
    x1, y1, z1 = data1[:, 0], data1[:, 1], data1[:, 2]
    x2, y2, z2 = data2[:, 0], data2[:, 1], data2[:, 2]
    x3, y3, z3 = data3[:, 0], data3[:, 1], data3[:, 2]
    x4, y4, z4 = data4[:, 0], data4[:, 1], data4[:, 2]

    t = np.linspace(0, steps * dt, steps)
    plt.figure()
    plt.subplot(311)  # plot x-t
    plt.title(ti)
    plt.plot(t, x1, color='red', linewidth=lw, label=str(x10))
    plt.plot(t, x2, color='blue', linewidth=lw, label=str(x20))
    plt.plot(t, x3, color='green', linewidth=lw, label=str(x30))
    plt.plot(t, x4, color='black', linewidth=lw, label=str(x40))
    plt.legend(loc="upper right", fontsize=8, ncol=4)
    plt.ylabel('x')
    ax = plt.gca()
    ax.set_xticklabels([])
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.tick_params(axis='y', labelsize=8)
    ax.set_xlim(0, steps * dt)

    plt.subplot(312)  # plot y-t
    plt.plot(t, y1, color='red', linewidth=lw, label=str(x10))
    plt.plot(t, y2, color='blue', linewidth=lw, label=str(x20))
    plt.plot(t, y3, color='green', linewidth=lw, label=str(x30))
    plt.plot(t, y4, color='black', linewidth=lw, label=str(x40))
    plt.ylabel('y')
    ax = plt.gca()
    ax.set_xticklabels([])
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.tick_params(axis='y', labelsize=8)
    ax.set_xlim(0, steps * dt)

    plt.subplot(313)  # plot z-t
    plt.plot(t, z1, color='red', linewidth=lw, label=str(x10))
    plt.plot(t, z2, color='blue', linewidth=lw, label=str(x20))
    plt.plot(t, z3, color='green', linewidth=lw, label=str(x30))
    plt.plot(t, z4, color='black', linewidth=lw, label=str(x40))
    plt.xlabel('t')
    plt.ylabel('z')
    ax = plt.gca()
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.tick_params(axis='y', labelsize=8)
    ax.tick_params(axis='x', labelsize=8)
    ax.set_xlim(0, steps * dt)
    plt.tight_layout()

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
