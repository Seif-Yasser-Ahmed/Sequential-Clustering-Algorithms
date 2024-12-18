from .NumpyEncoder import NumpyEncoder
from .distances import DistanceCalculator
import json
import numpy as np


class MBSAS:
    def __init__(self, max_no_clusters, threshold, distance_method='euclidean'):
        self.max_no_clusters = max_no_clusters
        self.threshold = threshold
        self.distance_method = distance_method

    def fit(self, data):
        clusters = [{
            'Cluster': 1,
            'Members': [data[0]],
            'Mean': data[0]
        }]
        no_of_clusters = 1
        for i in range(1, len(data)):
            min_distance = float('inf')
            for cluster in clusters:
                mean = cluster['Mean']
                distance = DistanceCalculator.calculate_distance(
                    data[i], mean, self.distance_method)
                if distance < min_distance:
                    min_distance = distance
                    min_cluster = cluster
            print("point", data[i], "min distance=",
                  min_distance, "cluster->", min_cluster['Cluster'])
            if min_distance > self.threshold and no_of_clusters < self.max_no_clusters:
                no_of_clusters += 1
                clusters.append({'Cluster': no_of_clusters,
                                'Members': [data[i]], 'Mean': data[i]})
            # else:
            #     min_cluster['Members'].append(data[i])
            #     min_cluster['Mean'] = np.mean(min_cluster['Members'], axis=0)
            # print("Clusters Now", clusters)
            # print("="*50)
        for i in range(len(data)):
            if not any(np.array_equal(data[i], member) for cluster in clusters for member in cluster['Members']):
                min_distance = float('inf')
                for cluster in clusters:
                    mean = cluster['Mean']
                    distance = DistanceCalculator.calculate_distance(
                        data[i], mean, self.distance_method)
                    if distance < min_distance:
                        min_distance = distance
                        min_cluster = cluster
                min_cluster['Members'].append(data[i])
                min_cluster['Mean'] = np.mean(min_cluster['Members'], axis=0)
        return clusters
