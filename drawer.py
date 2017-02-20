import matplotlib.pyplot as plt
import numpy as np

FIRST_FUNCTION_LABEL = 'p(X / C1) * P(C1)'
SECOND_FUNCTION_LABEL = 'p(X / C2) * P(C2)'
LEFT_AREA_LABEL = 'Зона пропуска обнаружения для C1'
RIGHT_AREA_LABEL = 'Зона ложной тревоги для C1'

def draw_plots(first_function, second_function, interval, step):
    interval_start, interval_end = interval
    arange = np.arange(interval_start, interval_end, step)
    plt.plot(arange, first_function(arange), label=FIRST_FUNCTION_LABEL)
    plt.plot(arange, second_function(arange), label=SECOND_FUNCTION_LABEL)
    y1 = first_function(arange)
    y2 = second_function(arange)
    axis = plt.axes()
    axis.fill_between(arange, 0, y1, where=y2 >= y1, label=LEFT_AREA_LABEL)
    axis.fill_between(arange, 0, y2, where=y1 >= y2, label=RIGHT_AREA_LABEL)
    plt.legend(loc='upper left', shadow=True, fontsize='larger')
    plt.show()
