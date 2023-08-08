import pytest
from gendiff.formatters.plain import format_diff_plain, to_str
from test_utils import get_input_data, get_expected_result


@pytest.mark.parametrize('input_value, expected_value', [
    ("hello", "'hello'"),
    (42, "42"),
    (3.14, "3.14"),
    (True, "true"),
    (False, "false"),
    (None, "null"),
    ({"key": "value"}, "[complex value]"),
    ([1, 2, 3], "[complex value]"),
    ([1, [2, 3], 4], "[complex value]"),
    ({"key": {"nested_key": "value"}}, "[complex value]"),
    ([], "[complex value]"),
    ({}, "[complex value]")
])
def test_to_str(input_value, expected_value):
    assert to_str(input_value) == expected_value


@pytest.fixture
def input_diff():
    return get_input_data('input_diff.json')


@pytest.fixture
def expected_result():
    return get_expected_result('exp_plain.txt')


def test_format_diff_plain(input_diff, expected_result):
    assert format_diff_plain(input_diff) == expected_result
