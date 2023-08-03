import pytest
from gendiff.formatters.stylish import format_value, make_stylish_result
from test_utils import get_input_data, get_expected_result


def test_format_value():
    assert 'null' == format_value(None, 0)
    assert 'true' == format_value(True, 0)
    assert 'string' == format_value('string', 0)
    assert '10' == format_value(10, 0)
    assert '10.0' == format_value(10.0, 0)
    assert f"{{'a': 'b'}}" == format_value({'a': 'b'}, 0)


@pytest.fixture
def input_diff():
    return get_input_data('input_diff_for_stylish.json')


@pytest.fixture
def expected_result():
    return get_expected_result('expected_result_for_stylish.txt')


def test_make_stylish_result(input_diff, expected_result):
    assert make_stylish_result(input_diff) == expected_result
