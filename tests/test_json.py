import os
import json
import pytest
from gendiff.formatters.json import format_diff_json


@pytest.fixture
def input_diff():
    fixture_path = os.path.join(
        'tests', 'fixtures', 'input_diff_for_json.json'
    )
    with open(fixture_path) as file:
        return json.load(file)


@pytest.fixture
def expected_result():
    fixture_path = os.path.join(
        'tests', 'fixtures', 'expected_result_for_json.txt'
    )
    with open(fixture_path) as file:
        return file.read()


def test_format_diff_json(input_diff, expected_result):
    assert format_diff_json(input_diff) == expected_result
