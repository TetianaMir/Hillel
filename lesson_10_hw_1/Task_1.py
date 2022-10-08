def deepcopy(values):
    if isinstance(values, list):
        return list(map(deepcopy, values))
    if isinstance(values, tuple):
        return tuple(map(deepcopy, values))
    if isinstance(values, dict):
        return {
            deepcopy(key): deepcopy(values)
            for key, value in values.items()
        }
    return values
