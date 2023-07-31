import os
import json
import pytest
from gendiff.formatters.stylish import format_value, make_stylish_result


def test_format_value():
    assert 'null' == format_value(None, 0)
    assert 'true' == format_value(True, 0)
    assert 'string' == format_value('string', 0)
    assert '10' == format_value(10, 0)
    assert '10.0' == format_value(10.0, 0)
    assert {'a': 'b'} == format_value({'a': 'b'}, 0)


@pytest.fixture
def input_diff():
    fixture_path = os.path.join(
        'tests', 'fixtures', 'input_diff_for_stylish.json'
    )
    with open(fixture_path) as file:
        return json.load(file)


@pytest.fixture
def expected_result():
    fixture_path = os.path.join(
        'tests', 'fixtures', 'expected_result_for_stylish.txt'
    )
    with open(fixture_path) as file:
        return file.read()


def test_make_stylish_result(input_diff, expected_result):
    assert make_stylish_result(input_diff) == expected_result
