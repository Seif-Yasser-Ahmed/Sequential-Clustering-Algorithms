from Src.BSAS import BSAS
from Src.MBSAS import MBSAS
from Src.NumpyEncoder import NumpyEncoder
from Src.Logger import Logger
import json
import numpy as np


if __name__ == "__main__":
    max_no_clusters = 15
    threshold = 2.5

    distance_methods = ['euclidean', 'manhattan']

    data_bsas = np.array([
        [2, 3],  # x8
        [5, 4],  # x6
        [9, 2],  # x11
        [2, 5],  # x1
        [1, 4],  # x5
        [6, 4],  # x2
        [5, 3],  # x3
        [2, 2],  # x4
        [3, 3],  # x7
        [8, 2],  # x10
        [2, 4],  # x9
        [10, 2],  # x12
        [11, 2],  # x13
        [10, 3],  # x14
        [9, 1],  # x15

    ])
    data_mbsas = np.array([[2, 5], [6, 4], [5, 3], [2, 2], [
                          1, 4], [5, 4], [3, 3], [2, 3]])

    for i in ['BSAS', 'MBSAS']:
        for distance_method in distance_methods:
            if i == 'BSAS':
                bsas = BSAS(max_no_clusters=max_no_clusters,
                            threshold=threshold, distance_method=distance_method)
                clusters = bsas.fit(data_bsas)
                Logger.log_clusters(data_bsas, clusters,
                                    distance_method, algo=i)
            else:
                bsas = MBSAS(max_no_clusters=max_no_clusters,
                             threshold=threshold, distance_method=distance_method)
                clusters = bsas.fit(data_mbsas)
                Logger.log_clusters(data_mbsas, clusters,
                                    distance_method, algo=i)
