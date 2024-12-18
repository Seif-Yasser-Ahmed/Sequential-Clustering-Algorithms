from Src.BSAS import BSAS
from Src.MBSAS import MBSAS
from Src.NumpyEncoder import NumpyEncoder
from Src.Logger import Logger
import json
import numpy as np


if __name__ == "__main__":

    data_bsas = np.array([[2, 3], [5, 4], [9, 2], [2, 5], [1, 4], [6, 4], [5, 3], [2, 2], [3, 3], [8, 2], [2, 4], [10, 2], [11, 2], [10, 3], [9, 1]
                          ])
    data_mbsas = np.array([[2, 5], [6, 4], [5, 3], [2, 2], [
                          1, 4], [5, 4], [3, 3], [2, 3]])
    max_no_clusters = 15
    threshold = 2.5
    distance_methods = ['euclidean', 'manhattan']
    for i in ['BSAS', 'MBSAS']:
        for distance_method in distance_methods:
            if i == 'BSAS':
                bsas = BSAS(max_no_clusters=max_no_clusters,
                            threshold=threshold, distance_method=distance_method)
                clusters = bsas.fit(data_bsas)
                Logger.log_clusters(data_bsas, clusters, distance_method)
            else:
                bsas = MBSAS(max_no_clusters=max_no_clusters,
                             threshold=threshold, distance_method=distance_method)
                clusters = bsas.fit(data_mbsas)
                Logger.log_clusters(data_mbsas, clusters, distance_method)
