import json

import numpy as np

from Src.BSAS import BSAS
from Src.NumpyEncoder import NumpyEncoder


class Logger:
    def save_json(data, file_name):
        with open(file_name, 'w') as file:
            json.dump(data, file, cls=NumpyEncoder)

    @staticmethod
    def log_clusters(data, max_no_clusters, threshold, distance_methods):
        for method in distance_methods:
            bsas = BSAS(max_no_clusters, threshold, method)
            clusters = bsas.fit(data)
            Logger.save_json(clusters, f'clusters_{method}.json')
