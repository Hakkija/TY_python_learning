import json
import os


def load_json_file(file_name):
    with open(file_name, "r") as file:
        return json.load(file)


def save_json_file(file_name, json_data):
    with open(file_name, "w") as file:
        json.dump(json_data, file, indent=4)


def json_diff(json1, json2):
    delta = {}
    for key, value in json2.items():
        if key not in json1:
            delta[key] = value
        elif isinstance(value, dict) and isinstance(json1[key], dict):
            sub_delta = json_diff(json1[key], value)
            if sub_delta:
                delta[key] = sub_delta
        elif value != json1[key]:
            delta[key] = value

    for key in json1.keys():
        if key not in json2:
            delta[key] = None

    return delta


def json_patch(json1, delta):
    for key, value in delta.items():
        if value is None:
            json1.pop(key, None)
        elif key not in json1 or not isinstance(value, dict) or not isinstance(json1[key], dict):
            json1[key] = value
        else:
            json_patch(json1[key], value)


print("Current working directory:", os.getcwd())

v1 = load_json_file("go1.json")
v2 = load_json_file("go1.0.1.json")

delta = json_diff(v1, v2)

save_json_file("delta.json", delta)

v2_reconstructed = json.loads(json.dumps(v1))  # DeepCopy of v1

json_patch(v2_reconstructed, delta)

save_json_file("go1.0.1_reconstructed.json", v2_reconstructed)
