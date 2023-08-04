import os
import yaml
import json


def get_file_format(file_path):
    _, ext = os.path.splitext(file_path)
    return ext[1:]


def get_file_content(file_path):
    with open(file_path) as file:
        return file.read()


def parse_data(content, format):
    if format == 'json':
        return json.loads(content)
    if format in ['yml', 'yaml']:
        return yaml.safe_load(content)
    raise ValueError(f"Unsupported file format: {format}")


def parse_data_from_file(file_path):
    format = get_file_format(file_path)
    content = get_file_content(file_path)
    return parse_data(content, format)
