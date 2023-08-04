import json
import pytest
from gendiff.parser import parse_data_from_file
from test_utils import get_expected_result


@pytest.fixture
def input_file_path(request):
    return request.param


@pytest.fixture
def expected_result(request):
    return get_expected_result(request.param)


@pytest.mark.parametrize('input_file_path, expected_result', [
    ('tests/fixtures/file1.json', 'expected_result_for_parse_file1.json'),
    ('tests/fixtures/file1.yml', 'expected_result_for_parse_file1.json'),
    ('tests/fixtures/file2.json', 'expected_result_for_parse_file2.json'),
    ('tests/fixtures/file2.yml', 'expected_result_for_parse_file2.json')
], indirect=['input_file_path', 'expected_result'])
def test_parse(input_file_path, expected_result):
    actual_data = parse_data_from_file(input_file_path)
    assert actual_data == json.loads(expected_result)


def test_unsupported_format():
    with pytest.raises(ValueError):
        parse_data_from_file("tests/fixtures/file3.txt")
