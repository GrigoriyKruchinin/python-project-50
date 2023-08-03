import pytest
import os
from gendiff.generate_diff import generate_diff
from test_utils import get_expected_result


FIXTURES_DIR = os.path.join('tests', 'fixtures')


def get_file_path(filename):
    return os.path.join(FIXTURES_DIR, filename)


@pytest.mark.parametrize('formatter', ['stylish', 'plain', 'json'])
@pytest.mark.parametrize('file1_name, file2_name', [
    ('file1.json', 'file2.json'),
    ('file1.yml', 'file2.yml')
])
def test_generate_diff(file1_name, file2_name, formatter):
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)
    expected_result = get_expected_result(f'exp_{formatter}.txt')

    actual_result = generate_diff(file1_path, file2_path, formatter)

    assert actual_result == expected_result


@pytest.mark.parametrize('formatter', ['stylish', 'plain', 'json'])
@pytest.mark.parametrize('file1_name, file2_name', [
    ('file1.json', 'file3.txt'),
    ('file2.yml', 'file3.txt')
])
def test_unsupported_formatter(file1_name, file2_name, formatter):
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)
    with pytest.raises(ValueError):
        generate_diff(file1_path, file2_path, formatter)
