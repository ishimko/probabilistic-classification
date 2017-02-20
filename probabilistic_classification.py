from random import gauss
from statistics import mean as count_mean, stdev as count_deviation
from math import pi
import numpy as np


def get_gauss_randomizer(mean, deviation):
    def gauss_randomizer(count):
        for _ in range(count):
            yield gauss(mean, deviation)
    return gauss_randomizer


def get_gaussian(mean, deviation):
    def gaussian(x):
        return 1/(deviation * np.sqrt(2*pi)) * np.exp(-0.5*((x - mean)/deviation)**2)
    return gaussian


def get_probability_density_function(vector, probability):
    gaussian = get_gaussian(count_mean(vector), count_deviation(vector))
    return lambda x: gaussian(x) * probability


def get_random_vector(mean, deviation, count):
    randomizer = get_gauss_randomizer(mean, deviation)
    return list(randomizer(count))


def generate_vectors(first_mean, first_deviation, second_mean, second_deviation, count):
    first_vector = get_random_vector(first_mean, first_deviation, count)
    second_vector = get_random_vector(second_mean, second_deviation, count)
    return first_vector, second_vector


def probabilistic_classification(first_probability, first_vector, second_vector):
    second_probability = 1 - first_probability
    first_function = get_probability_density_function(first_vector, first_probability)
    second_function = get_probability_density_function(second_vector, second_probability)
    return first_function, second_function


def get_interval(first_vector, second_vector):
    all_points = first_vector + second_vector
    return min(all_points), max(all_points)


def get_areas(first_function, second_function, interval, step):
    start, stop = interval
    assert start < stop
    detection_error = 0
    false_positive = 0
    arange = list(np.arange(start, stop, step))
    for x in arange:
        first_function_value = first_function(x)
        second_function_value = second_function(x)
        if second_function_value < first_function_value:
            detection_error += second_function_value * step
        else:
            false_positive += first_function_value * step
    return detection_error, false_positive
 