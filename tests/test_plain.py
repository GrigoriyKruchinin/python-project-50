import pytest
from gendiff.formatters.plain import format_diff_plain, format_value
from test_utils import get_input_data, get_expected_result


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
    return get_input_data('input_diff_for_plain.json')


@pytest.fixture
def expected_result():
    return get_expected_result('expected_result_for_plain.txt')


def test_format_diff_plain(input_diff, expected_result):
    assert format_diff_plain(input_diff) == expected_result
