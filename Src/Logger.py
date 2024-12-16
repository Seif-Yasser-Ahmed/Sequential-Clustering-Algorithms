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
        plt.figure(figsize=(10, 6))
        means = []
        for cluster in clusters:
            cluster_id = cluster['Cluster']
            points = cluster['Members']
            mean = cluster['Mean']
            means.append(mean)
            points = np.array(points)
            plt.scatter(points[:, 0], points[:, 1],
                        label=f'Cluster {cluster_id}')
            plt.scatter(mean[0], mean[1], marker='x', color='red')
            plt.text(mean[0], mean[1], f'Mean {
                     cluster_id}', fontsize=9, color='red')

        plt.title(f'Clusters using {method}')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        for i, mean in enumerate(means):
            plt.scatter([], [], marker='x', color='red', label=f'Mean {
                        i+1}: ({mean[0]:.2f}, {mean[1]:.2f})')
        plt.legend()
        plt.savefig(f'Output/clusters_{method}.png')

    @staticmethod
    def log_clusters(data, clusters, distance_method='euclidean'):
        Logger.save_json(clusters, f'Output/clusters_{distance_method}.json')
        Logger.PlotClusters(data, clusters, distance_method)
