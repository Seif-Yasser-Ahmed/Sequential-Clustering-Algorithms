from Src.BSAS import BSAS
from pyclustering.utils.metric import distance_metric, type_metric
from pyclustering.cluster.bsas import bsas
import numpy as np

data_points = np.array([
    [2, 5],
    [6, 4],
    [5, 3],
    [2, 2],
    [1, 4],
    [5, 4],
    [3, 3],
    [2, 3],
    [2, 4],
    [8, 2],
    [9, 2],
    [10, 2],
    [11, 2],
    [10, 3],
    [9, 1]
])

bsas_model = BSAS(threshold=1.5, max_no_clusters=3,
                  distance_method='manhattan')
clusters = bsas_model.fit(data_points)

print("Mine: ", clusters)

metric = distance_metric(type_metric.MANHATTAN)
bsas_instance = bsas(data_points, maximum_clusters=3,
                     threshold=1.5, metric=metric)
bsas_instance.process()
clusters = bsas_instance.get_clusters()
print("PyClustering Library: ", clusters)
