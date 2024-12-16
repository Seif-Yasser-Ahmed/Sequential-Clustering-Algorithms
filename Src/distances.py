import numpy as np


class DistanceCalculator:
    @staticmethod
    def euclidean_distance(x, y):
        return np.linalg.norm(x - y)

    @staticmethod
    def manhattan_distance(x, y):
        return np.linalg.norm(x - y, ord=1)

    @staticmethod
    def calculate_distance(x, y, distance_method='euclidean'):
        if distance_method == 'euclidean':
            return DistanceCalculator.euclidean_distance(x, y)
        elif distance_method == 'manhattan':
            return DistanceCalculator.manhattan_distance(x, y)
        else:
            raise ValueError('Unknown distance method')
