import os
import json


def get_input_data(file_name):
    fixture_path = os.path.join(
        'tests', 'fixtures', f'{file_name}'
    )
    with open(fixture_path) as file:
        return json.load(file)


def get_expected_result(file_name):
    fixture_path = os.path.join(
        'tests', 'fixtures', f'{file_name}'
    )
    with open(fixture_path) as file:
        return file.read()
