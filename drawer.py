import matplotlib.pyplot as plt
import numpy as np

FIRST_FUNCTION_LABEL = '$p(X | C_1) \cdot P(C_1)$'
SECOND_FUNCTION_LABEL = '$p(X | C_2) \cdot P(C_2)$'
LEFT_AREA_LABEL = 'Зона пропуска обнаружения для $C_1$'
RIGHT_AREA_LABEL = 'Зона ложной тревоги для $C_1$'

def draw_plots(first_function, second_function, interval, step, annotation):
    interval_start, interval_end = interval
    arange = np.arange(interval_start, interval_end, step)
    plt.plot(arange, first_function(arange), label=FIRST_FUNCTION_LABEL)
    plt.plot(arange, second_function(arange), label=SECOND_FUNCTION_LABEL)
    y1 = first_function(arange)
    y2 = second_function(arange)
    axis = plt.axes()
    axis.text(interval_start, axis.get_ylim()[1]/2, annotation, style='italic',
        bbox={'facecolor':'green', 'alpha':0.5, 'pad':10}, fontsize=12)
    axis.fill_between(arange, 0, y1, where=y2 >= y1, label=LEFT_AREA_LABEL)
    axis.fill_between(arange, 0, y2, where=y1 >= y2, label=RIGHT_AREA_LABEL)
    plt.legend(loc='upper left', shadow=True, fontsize='larger')
    plt.show()
