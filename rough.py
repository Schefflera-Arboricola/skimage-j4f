import skimage as ski
import numpy as np
import os

os.environ["SKIMAGE_NO_DISPATCHING"] = "0"

from importlib.metadata import entry_points

print(entry_points(group="skimage_backends"))
print(entry_points(group="skimage_backend_infos"))

print(ski.metrics.mean_squared_error(np.array([1, 2]), np.array([1, 2]), x=7))
