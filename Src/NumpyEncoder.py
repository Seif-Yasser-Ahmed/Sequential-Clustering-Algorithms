import json
import numpy as np


# this class is not written by me, it just helps to encoding numpy arrays to json to save them in the json file
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NumpyEncoder, self).default(obj)
