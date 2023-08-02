import os
import json


def read_file(file_name):
    fixture_path = os.path.join('tests', 'fixtures', f'{file_name}')
    with open(fixture_path) as file:
        return file.read()


def get_input_data(file_name):
    return json.loads(read_file(file_name))


def get_expected_result(file_name):
    return read_file(file_name)
