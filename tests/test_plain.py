import os
import json
import pytest
from gendiff.formatters.plain import format_diff_plain, format_value


def test_format_value():
    assert format_value("hello") == "'hello'"
    assert format_value(42) == "42"
    assert format_value(3.14) == "3.14"
    assert format_value(True) == "true"
    assert format_value(False) == "false"
    assert format_value(None) == "null"
    assert format_value({"key": "value"}) == "[complex value]"
    assert format_value([1, 2, 3]) == "[complex value]"
    assert format_value([1, [2, 3], 4]) == "[complex value]"
    assert format_value({"key": {"nested_key": "value"}}) == "[complex value]"
    assert format_value([]) == "[complex value]"
    assert format_value({}) == "[complex value]"


@pytest.fixture
def input_diff():
    fixture_path = os.path.join(
        'tests', 'fixtures', 'input_diff_for_plain.json'
    )
    with open(fixture_path) as file:
        return json.load(file)


@pytest.fixture
def expected_result():
    fixture_path = os.path.join(
        'tests', 'fixtures', 'expected_result_for_plain.txt'
    )
    with open(fixture_path) as file:
        return file.read()


def test_format_diff_plain(input_diff, expected_result):
    assert format_diff_plain(input_diff) == expected_result
