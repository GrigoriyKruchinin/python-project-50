import os
import json
import pytest
from gendiff.parse import parse_data


@pytest.fixture
def expected_data(file_name):
    file_path = os.path.join(
        'tests', 'fixtures', f'expected_for_parse_{file_name}.json'
        )
    with open(file_path) as file:
        return json.load(file)


@pytest.mark.parametrize('file_name', ['file1', 'file2'])
def test_parse(file_name, expected_data):
    file_path_json = f"tests/fixtures/{file_name}.json"
    file_path_yml = f"tests/fixtures/{file_name}.yml"

    actual_data_json = parse_data(file_path_json)
    actual_data_yml = parse_data(file_path_yml)

    assert actual_data_json == expected_data
    assert actual_data_yml == expected_data


def test_unsupported_format():
    with pytest.raises(ValueError):
        parse_data("tests/fixtures/file3.txt")
