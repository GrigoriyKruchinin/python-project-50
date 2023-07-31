import os
import yaml
import json


def parse_json(file_path):
    with open(file_path) as file:
        return json.load(file)


def parse_yaml(file_path):
    with open(file_path) as file:
        return yaml.safe_load(file)


def parse_data(file_path):
    _, ext = os.path.splitext(file_path)

    if ext == '.json':
        return parse_json(file_path)
    elif ext in ['.yml', '.yaml']:
        return parse_yaml(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")
