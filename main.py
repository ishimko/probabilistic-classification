from sys import argv
from probabilistic_classification import generate_vectors, get_interval, \
    probabilistic_classification, get_areas
from drawer import draw_plots


STEP = 0.001
NUMBERS_COUNT = 10000


def print_result(detection_error, false_positive):
    print('Вероятность ложной тревоги для 1-го класса: {}'.format(detection_error))
    print('Вероятность пропуска обнаружения для 1-го класса: {}'.format(false_positive))
    print('Вероятность суммарной ошибки классификации: {}'.format(detection_error + false_positive))


def main():
    first_probability = float(argv[1])
    first_mean = float(argv[2])
    first_deviation = float(argv[3])
    second_mean = float(argv[4])
    second_deviation = float(argv[5])
    vectors = generate_vectors(first_mean, first_deviation, second_mean, second_deviation, NUMBERS_COUNT)
    first_vector, second_vector = vectors
    interval = get_interval(first_vector, second_vector)
    functions = probabilistic_classification(first_probability, first_vector, second_vector)
    first_function, second_function = functions
    detection_error, false_positive = get_areas(first_function, second_function, interval, STEP)
    print_result(detection_error, false_positive)
    draw_plots(first_function, second_function, interval, STEP)


if __name__ == '__main__':
    main()
