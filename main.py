from sys import argv
from probabilistic_classification import generate_vectors, get_interval, \
    probabilistic_classification, get_intercetion_point, get_area
from drawer import draw_plots


STEP = 0.001
NUMBERS_COUNT = 10000
FIRST_MEAN = 0
FIRST_DEVIATION = 1
SECOND_MEAN = 2
SECOND_DEVIATION = 1


def print_result(left_area, right_area):
    print('Вероятность ложной тревоги для 1-го класса: {}'.format(left_area))
    print('Вероятность пропуска обнаружения для 1-го класса: {}'.format(right_area))
    print('Вероятность суммарной ошибки классификации: {}'.format(left_area+right_area))


def main():
    first_probability = float(argv[1])
    vectors = generate_vectors(FIRST_MEAN, FIRST_DEVIATION, SECOND_MEAN, SECOND_DEVIATION, NUMBERS_COUNT)
    first_vector, second_vector = vectors
    interval = get_interval(first_vector, second_vector)
    functions = probabilistic_classification(first_probability, first_vector, second_vector)
    first_function, second_function = functions
    x_intersection = get_intercetion_point(first_function, second_function, (FIRST_MEAN, SECOND_DEVIATION), STEP)
    left_area = get_area(second_function, (interval[0], x_intersection), STEP)
    right_area = get_area(first_function, (x_intersection, interval[1]), STEP)
    print_result(left_area, right_area)
    draw_plots(first_function, second_function, interval, STEP)


if __name__ == '__main__':
    main()
