__all__ = [
    "can_has",
    "info",
    "get_implementation",
]


def info():
    # print("info")
    from skimage.util._backends import BackendInformation

    backend_info = BackendInformation(
        [
            "skimage.metrics:mean_squared_error",
        ]
    )
    return backend_info


def can_has(name, *args, **kwargs):
    # print("can_has")
    return name == "skimage.metrics:mean_squared_error"


def get_implementation(name):
    # print("get_implementation")
    if name == "skimage.metrics:mean_squared_error":
        from skimage_j4f.metrics import simple_metrics

        return simple_metrics.mean_squared_error
    return None
