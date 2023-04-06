import json


def json_diff(a, b, path=None):
    if path is None:
        path = []

    delta = {}

    for key in b.keys():
        if key not in a:
            delta[tuple(path + [key])] = b[key]
        else:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                sub_delta = json_diff(a[key], b[key], path + [key])
                delta.update(sub_delta)
            elif a[key] != b[key]:
                delta[tuple(path + [key])] = b[key]

    for key in a.keys():
        if key not in b:
            delta[tuple(path + [key])] = None

    return delta


def apply_delta(a, delta):
    result = a.copy()

    for path, value in delta.items():
        target = result
        for key in path[:-1]:
            target = target[key]

        if value is None:
            del target[path[-1]]
        else:
            target[path[-1]] = value

    return result


# Testimine
v1 = {
    "k1": {
        "k1": ["x1", "x2"],
        "k2": ["x1", "x2"],
        "k3": ["x1", "x2"]
    }
}

v2 = {
    "k1": {
        "k1": ["x1", "x2"],
        "k2": ["x1", "x2"],
        "k3": ["x1", "x3"],
        "k4": ["x1", "x1"]
    }
}

delta = json_diff(v1, v2)
print("Delta:", delta)

v2_reconstructed = apply_delta(v1, delta)
print("V2 taastatud:", v2_reconstructed)