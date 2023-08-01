import os
import yaml
import json


def get_file_format(file_path):
    _, ext = os.path.splitext(file_path)
    return ext[1:]


def get_file_content(file_path):
    with open(file_path) as file:
        return file.read()


def parse_json(content):
    return json.loads(content)


def parse_yaml(content):
    return yaml.safe_load(content)


def parse_data(content, file_format):
    if file_format == 'json':
        return parse_json(content)
    elif file_format in ['yml', 'yaml']:
        return parse_yaml(content)
    else:
        raise ValueError(f"Unsupported file format: {file_format}")


def parse_data_from_file(file_path):
    file_format = get_file_format(file_path)
    content = get_file_content(file_path)
    return parse_data(content, file_format)
