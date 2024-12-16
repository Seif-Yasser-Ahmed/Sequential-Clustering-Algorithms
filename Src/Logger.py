import json

import numpy as np

from Src.BSAS import BSAS
from Src.NumpyEncoder import NumpyEncoder
import matplotlib.pyplot as plt


class Logger:
    def save_json(data, file_name):
        with open(file_name, 'w') as file:
            json.dump(data, file, cls=NumpyEncoder)

    def PlotClusters(data, clusters, method):
        for cluster_id, points in clusters.items():
            points = np.array(points)
            plt.scatter(points[:, 0], points[:, 1],
                        label=f'Cluster {cluster_id}')

        plt.title(f'Clusters using {method}')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.legend()
        plt.savefig(f'clusters_{method}.png')

    @staticmethod
    def log_clusters(data, clusters, distance_method='euclidean'):
        Logger.save_json(clusters, f'clusters_{distance_method}.json')
        Logger.PlotClusters(data, clusters, distance_method)
