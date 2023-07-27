import os
import yaml
import json


def parse_data(file_path):
    _, ext = os.path.splitext(file_path)

    with open(file_path) as file:
        if ext == '.json':
            return json.load(file)
        elif ext in ['.yml', '.yaml']:
            return yaml.safe_load(file)
        else:
            raise ValueError(f"Unsupported file format: {ext}")
