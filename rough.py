import skimage as ski
import numpy as np
import os

os.environ["SKIMAGE_DISPATCHING"] = "True"

from importlib.metadata import entry_points

print(entry_points(group="skimage_backends"))
print(entry_points(group="skimage_backend_infos"))

os.environ["SKIMAGE_BACKEND_PRIORITY"] = "fake"
print(ski.metrics.mean_squared_error(np.array([1, 2]), np.array([1, 2])))

print(ski.metrics.mean_squared_error(np.array([1, 2]), np.array([1, 2]), x=5))

os.environ["SKIMAGE_BACKEND_PRIORITY"] = "phony, j4f"

print(ski.metrics.mean_squared_error(np.array([1, 2]), np.array([1, 2])))

"""
os.environ["SKIMAGE_BACKEND_PRIORITY"] = "j4f"
print(ski.metrics.mean_squared_error(np.array([1, 2]), np.array([1, 2]), 5))

print(ski.util._backends.get_skimage_backends())
x = os.environ.get("SKIMAGE_DISPATCHING", False)
print(x)

print(ski.util._backends.all_backends_with_eps_combined())

n = ski.metrics.mean_squared_error.__name__
print(n)
print(ski.util._backends.public_api_name(ski.metrics.mean_squared_error))

os.environ["SKIMAGE_DISPATCHING"] = "False"
print((ski.util._backends.get_skimage_backends()))
print(ski.metrics.mean_squared_error(np.array([1, 2]), np.array([1, 2])))
"""
