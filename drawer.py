import matplotlib.pyplot as plt
import numpy as np


def draw_plots(first_function, second_function, interval, step):
    interval_start, interval_end = interval
    arange = np.arange(interval_start, interval_end, step)
    plt.plot(arange, first_function(arange), label='p(X / C1) * P(C1)')
    plt.plot(arange, second_function(arange), label='p(X / C2) * P(C2)')
    y1 = first_function(arange)
    y2 = second_function(arange)
    axis = plt.axes()
    axis.fill_between(arange, 0, y1, where=y2 >= y1, hatch='/', facecolor='None')
    axis.fill_between(arange, 0, y2, where=y1 >= y2, hatch='\\', facecolor='None')
    plt.legend(loc='upper left', shadow=True, fontsize='larger')
    plt.show()
