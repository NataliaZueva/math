import matplotlib.pyplot as plt
import numpy as np


def draw_plot(x1, y1, x2, y2):
    """Отрисовка двух графиков, по точкам"""
    fig, ax = plt.subplots()

    ax.plot(x1, y1)
    ax.plot(x2, y2)
    ax.set_ylim(-5, 10)
    ax.set_xlim(-5, 10)
    ax.set_yticks(np.arange(-5, 10, 1))
    ax.set_xticks(np.arange(-5, 10, 1))
    ax.grid(color='grey', linewidth=0.5, linestyle='-')
    plt.show()


def draw_two_plots(x1, y1, x2, y2):
    pass
